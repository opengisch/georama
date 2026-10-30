import json
import os.path
from functools import partial
from http import HTTPStatus
from typing import TYPE_CHECKING

import pygeoapi.api as core_api
import pygeoapi.api.itemtypes as itemtypes_api
from django.core.exceptions import BadRequest, PermissionDenied, ValidationError
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from guardian.core import ObjectPermissionChecker
from pygeoapi import l10n
from pygeoapi.api import API, APIRequest, apply_gzip
from pygeoapi.openapi import get_oas
from pygeoapi.util import to_json

from georama.features.apps import FeaturesConfig
from georama.features.config_server import ServerConfig
from georama.features.features_config import Config
from georama.features.models import FeatureLayer, Field

if TYPE_CHECKING:
    from georama.integration.models import VectorField as DatasourceField

api = None


# THIS IS A HACK, WE CREATE DICT WHICH BASICALLY NEVER STORES ANYTHING ON SET
# SO ITS THREAD SAFE
class _NoCache(dict):
    def __setitem__(self, key, value):
        pass


l10n._cfg_cache = _NoCache()


def get_geometry_format(geom_type: str) -> str:
    return f"geometry-{geom_type.lower() if geom_type != 'UNSET' else 'any'}"


def get_collection_schema_with_geometry_format(
    api: API, request: APIRequest, dataset: str, geometry_format: str
) -> tuple[dict, int, str]:
    """THIS IS A TEMPORARY FIX TO ALLOW PYGEOAPI EXPOSE CORRECT GEOMETRY TYPES IN SCHEMA.

    Wraps the pygeoapi collection schema to expose the actual geometry type.

    pygeoapi always exposes the primary geometry as `geometry` with
    `geometry-any`. It can't be passed through the provider fields: pygeoapi 0.21
    requires a `type` for each field, and clients like QGIS treat every property
    with a `type` as attribute.

    We let pygeoapi generate the schema (result is a JSON string). After that we
    dict encode it again to change the "format" of geometry if exists to the correct
    type.
    """
    headers, status, content = core_api.get_collection_schema(api, request, dataset)
    if status != HTTPStatus.OK or headers.get("Content-Type") != "application/schema+json":
        return headers, status, content

    schema = json.loads(content)
    schema["required"] = []
    geometry = schema["properties"].get("geometry")
    if geometry is not None:
        geometry["format"] = geometry_format
    for key in schema["properties"]:
        v = schema["properties"][key]
        if v.get("required"):
            schema["required"].append(key)

    return headers, status, to_json(schema, api.pretty_print)


@method_decorator(csrf_exempt, name="dispatch")
class PygeoapiServer(View):
    action = None
    model = FeatureLayer

    @classmethod
    def urls(cls):
        """Prepares a tuple of 2 elements which can be used directly with django.urls.include."""
        patterns = []
        return (patterns, FeaturesConfig.label)

    def dispatch(self, request, *args, **kwargs):
        handler = getattr(self, f"{self.action}", None)

        if callable(handler):
            return handler(request, *args, **kwargs)

        raise Http404(f"Unknown action: {self.action!r}")

    def execute_from_django(
        self,
        api_function,
        request: HttpRequest,
        *args,
        skip_valid_check=False,
        collection_id: str | None = None,
        with_openapi=False,
    ) -> HttpResponse:
        server_config, openapi_config = self.handle_runtime_config(
            request, collection_id, with_openapi
        )
        api = API(server_config, openapi_config)

        api_request = APIRequest.from_django(request, api.locales)
        content: str | bytes
        if not skip_valid_check and not api_request.is_valid():
            headers, status, content = api.get_format_exception(api_request)
        else:
            headers, status, content = api_function(api, api_request, *args)
            content = apply_gzip(headers, content)

        # Convert API payload to a django response
        response = HttpResponse(content, status=status)

        for key, value in headers.items():
            response[key] = value
        return response

    def get_collection_or_404_or_403(
        self, collection_id: str, perm: str, include_public: bool = False
    ):
        try:
            return self.model.objects.accessible_objects(
                self.request.georama_organisation,
                self.request.user,
                [perm],
                [collection_id],
                include_public,
            )
        except self.model.DoesNotExist as e:
            raise Http404(e) from e
        except PermissionError as e:
            raise PermissionDenied(e) from e

    def landing(self, request: HttpRequest) -> HttpResponse:
        """OGC API landing page endpoint.

        :request Django HTTP Request

        :returns: Django HTTP Response
        """
        return self.execute_from_django(core_api.landing_page, request)

    def openapi(self, request: HttpRequest) -> HttpResponse:
        """OpenAPI endpoint.

        :request Django HTTP Request

        :returns: Django HTTP Response
        """
        return self.execute_from_django(core_api.openapi_, request, with_openapi=True)

    def conformance(self, request: HttpRequest) -> HttpResponse:
        """OGC API conformance endpoint.

        :request Django HTTP Request

        :returns: Django HTTP Response
        """
        return self.execute_from_django(core_api.conformance, request)

    def collections(self, request: HttpRequest, collection_id: str | None = None) -> HttpResponse:
        """OGC API collections endpoint.

        :request Django HTTP Request
        :param collection_id: collection identifier

        :returns: Django HTTP Response
        """
        return self.execute_from_django(
            core_api.describe_collections, request, collection_id, collection_id=collection_id
        )

    def collection_schema(
        self, request: HttpRequest, collection_id: str | None = None
    ) -> HttpResponse:
        """OGC API collections schema endpoint.

        :request Django HTTP Request
        :param collection_id: collection identifier

        :returns: Django HTTP Response
        """
        feature_layer = self.get_collection_or_404_or_403(
            collection_id, "view_objects_on_published_layer", include_public=True
        ).get()
        geom_type = feature_layer.datasource.geometry_type_wkb
        geometry_format = get_geometry_format(geom_type)
        return self.execute_from_django(
            # a bit hacky, but we use
            # https://docs.python.org/3/library/functools.html#functools.partial
            # to force wat we want
            partial(get_collection_schema_with_geometry_format, geometry_format=geometry_format),
            request,
            collection_id,
        )

    def collection_queryables(
        self, request: HttpRequest, collection_id: str | None = None
    ) -> HttpResponse:
        """OGC API collections queryables endpoint.

        :request Django HTTP Request
        :param collection_id: collection identifier

        :returns: Django HTTP Response
        """
        _ = self.get_collection_or_404_or_403(
            collection_id, "view_objects_on_published_layer", include_public=True
        )
        return self.execute_from_django(
            itemtypes_api.get_collection_queryables,
            request,
            collection_id,
            collection_id=collection_id,
        )

    def collection_items(self, request: HttpRequest, collection_id: str) -> HttpResponse:
        """OGC API collections items endpoint.

        :request Django HTTP Request
        :param collection_id: collection identifier

        :returns: Django HTTP response
        """
        if request.method == "GET":
            _ = self.get_collection_or_404_or_403(
                collection_id, "view_objects_on_published_layer", include_public=True
            )
            response_ = self.execute_from_django(
                itemtypes_api.get_collection_items,
                request,
                collection_id,
                skip_valid_check=True,
                collection_id=collection_id,
            )
        elif request.method == "POST":
            _ = self.get_collection_or_404_or_403(
                collection_id, "create_objects_on_published_layer"
            )
            if request.content_type is not None:
                if request.content_type == "application/geo+json":
                    response_ = self.execute_from_django(
                        itemtypes_api.manage_collection_item,
                        request,
                        "create",
                        collection_id,
                        skip_valid_check=True,
                        collection_id=collection_id,
                    )
                else:
                    response_ = self.execute_from_django(
                        itemtypes_api.manage_collection_item,
                        request,
                        "create",
                        collection_id,
                        skip_valid_check=True,
                        collection_id=collection_id,
                    )
            else:
                raise BadRequest()
        elif request.method == "OPTIONS":
            _ = self.get_collection_or_404_or_403(
                collection_id, "view_objects_on_published_layer", include_public=True
            )
            response_ = self.execute_from_django(
                itemtypes_api.manage_collection_item,
                request,
                "options",
                collection_id,
                skip_valid_check=True,
                collection_id=collection_id,
            )
        else:
            raise BadRequest()

        return response_

    def collection_item(
        self, request: HttpRequest, collection_id: str, item_id: str
    ) -> HttpResponse:
        """OGC API collections items endpoint.

        :request Django HTTP Request
        :param collection_id: collection identifier
        :param item_id: item identifier

        :returns: Django HTTP response
        """
        if request.method == "GET":
            _ = self.get_collection_or_404_or_403(
                collection_id, "view_objects_on_published_layer", include_public=True
            )
            response_ = self.execute_from_django(
                itemtypes_api.get_collection_item,
                request,
                collection_id,
                item_id,
                collection_id=collection_id,
            )
        elif request.method == "PUT":
            _ = self.get_collection_or_404_or_403(
                collection_id, "update_objects_on_published_layer"
            )
            response_ = self.execute_from_django(
                itemtypes_api.manage_collection_item,
                request,
                "update",
                collection_id,
                item_id,
                skip_valid_check=True,
                collection_id=collection_id,
            )
        elif request.method == "DELETE":
            _ = self.get_collection_or_404_or_403(
                collection_id, "delete_objects_on_published_layer"
            )
            response_ = self.execute_from_django(
                itemtypes_api.manage_collection_item,
                request,
                "delete",
                collection_id,
                item_id,
                skip_valid_check=True,
                collection_id=collection_id,
            )
        elif request.method == "OPTIONS":
            _ = self.get_collection_or_404_or_403(
                collection_id, "view_objects_on_published_layer", include_public=True
            )
            response_ = self.execute_from_django(
                itemtypes_api.manage_collection_item,
                request,
                "options",
                collection_id,
                item_id,
                skip_valid_check=True,
                collection_id=collection_id,
            )
        else:
            raise BadRequest()

        return response_

    def handle_runtime_config(
        self, request: HttpRequest, collection_id: str | None = None, with_openapi=False
    ) -> tuple[dict, dict]:
        """Builds the pygeoapi config for the accessible feature layers of the request.


        Args:
            request: Django HTTP Request
            collection_id: restricts the config to this collection if set
            with_openapi: builds the OpenAPI document, it is only read by the openapi
                endpoint and loads every provider

        Returns:
            pygeoapi server config and OpenAPI document
        """
        server_config = ServerConfig().get()
        server_config["server"]["url"] = (
            f"{request.scheme}://{request.get_host()}{reverse('features:landing')}"
        )
        feature_layers = self.accessible_feature_layers(request, collection_id)
        permission_checker = ObjectPermissionChecker(request.user)
        if feature_layers:
            permission_checker.prefetch_perms(feature_layers)
        for feature_layer in feature_layers:
            server_config["resources"][feature_layer.identifier] = self.create_resource(
                feature_layer, permission_checker
            )
        openapi_config = get_oas(server_config) if with_openapi else {}
        return server_config, openapi_config

    def accessible_feature_layers(
        self, request: HttpRequest, collection_id: str | None = None
    ) -> list[FeatureLayer]:
        feature_layers = self.model.objects.accessible_objects(
            self.request.georama_organisation,
            request.user,
            ["view_objects_on_published_layer"],
            include_public=True,
        ).prefetch_related("fields__datasource_field")
        if collection_id is not None:
            try:
                feature_layers = feature_layers.filter(id=collection_id)
            except ValidationError:
                # not a valid identifier, pygeoapi answers with 404
                return []
        return list(feature_layers)

    @staticmethod
    def handle_crs_setting(crs: str):
        import pygeoapi.api as runtime_api

        if crs not in runtime_api.DEFAULT_CRS_LIST:
            runtime_api.DEFAULT_CRS_LIST.append(crs)

    def create_ogr_provider(
        self,
        feature_layer: FeatureLayer,
        editable: bool,
        features_properties: list[Field],
    ) -> dict:
        source = feature_layer.datasource.source_to_qsl

        crs = feature_layer.datasource.crs_to_qsl
        available_crs_list = self.get_available_crs_list(crs)

        # TODO: make this configurable
        driver_lookup = {"SHP": "ESRI Shapefile", "GPKG": "GPKG", "GDB": "OpenFileGDB"}

        # The geometry column name may differ, setting it to None works for all cases
        geom_field = None
        geom_type = feature_layer.datasource.geometry_type_wkb

        field_constraints = get_dataset_field_constraints(features_properties, geom_type)

        provider_definition = {
            "type": "feature",
            "name": "OG_OGR",
            "data": {
                "source_type": driver_lookup[source.ogr.path.split(".")[-1].upper()],
                "source": os.path.join(
                    Config().path,
                    feature_layer.datasource.project.organisation_folder,
                    os.path.dirname(feature_layer.datasource.project.path),
                    source.ogr.path,
                ),
                "source_capabilities": {"paging": True},
            },
            "editable": editable,
            "crs": available_crs_list,
            "storage_crs": crs.ogc_uri,
            "id_field": "fid",
            "layer": (
                source.ogr.layer_name
                if source.ogr.layer_name is not None
                else os.path.basename(source.ogr.path).split(".")[0]
            ),
            "geom_field": geom_field,
            "geom_type": geom_type,
            "properties": [f.name for f in features_properties],
            "field_constraints": field_constraints,
        }

        return provider_definition

    def create_postgres_provider(
        self,
        feature_layer: FeatureLayer,
        editable: bool,
        features_properties: list[Field],
    ) -> dict:
        source = feature_layer.datasource.source_to_qsl

        crs = feature_layer.datasource.crs_to_qsl
        available_crs_list = self.get_available_crs_list(crs)

        geom_field = source.postgres.geometry_column
        geom_type = feature_layer.datasource.geometry_type_wkb

        field_constraints = get_dataset_field_constraints(features_properties, geom_type)

        # Layers using a pg_service only carry the service name: QSL does not resolve it
        # at export so that no credentials end up stored in the database. The connection
        # info is therefore resolved by libpq at connection time.
        # None values are dropped by SQLAlchemy/psycopg2, so libpq falls back to the
        # pg_service (PGSERVICEFILE) for everything not set explicitly in the project
        data = {
            "host": source.postgres.host,
            "dbname": source.postgres.dbname,
            "user": source.postgres.username,
            "password": source.postgres.password,
            "search_path": [source.postgres.schema],
        }
        if source.postgres.port is not None:
            data["port"] = source.postgres.port

        # pygeoapi passes "options" as psycopg2 connect args
        options = {}
        if source.postgres.ssl_mode_text:
            options["sslmode"] = source.postgres.ssl_mode_text
        if source.postgres.service is not None:
            options["service"] = source.postgres.service
            if source.postgres.port is None:
                # pygeoapi defaults a missing port to 5432 which would override the one
                # of the service, SQLAlchemy omits a port 0 from the connection args
                data["port"] = 0

        provider_definition = {
            "type": "feature",
            "name": "OG_SQL",
            "data": data,
            "options": options,
            "editable": editable,
            "crs": available_crs_list,
            "storage_crs": crs.ogc_uri,
            "id_field": source.postgres.key,
            "table": source.postgres.table,
            "geom_field": geom_field,
            "geom_type": geom_type,
            "properties": [f.name for f in features_properties],
            "field_constraints": field_constraints,
        }

        return provider_definition

    def create_resource(
        self, feature_layer: FeatureLayer, permission_checker: ObjectPermissionChecker
    ) -> dict:
        editable = any(
            p in permission_checker.get_perms(feature_layer)
            for p in (
                "create_objects_on_published_layer",
                "update_objects_on_published_layer",
                "delete_objects_on_published_layer",
            )
        )

        features_properties = [p for p in feature_layer.fields.all() if p.visible]

        if feature_layer.datasource.driver.upper() == "POSTGRES":
            provider = self.create_postgres_provider(feature_layer, editable, features_properties)
        elif feature_layer.datasource.driver.upper() == "OGR":
            provider = self.create_ogr_provider(feature_layer, editable, features_properties)
        else:
            raise NotImplementedError

        return {
            "type": "collection",
            "title": feature_layer.metadata.title,
            "description": feature_layer.metadata.description,
            # TODO: add keywords into models
            "keywords": [],
            "linked-data": {
                "context": [
                    {"datetime": "https://schema.org/DateTime"},
                    {
                        "vocab": "https://example.com/vocab#",
                        "stn_id": "vocab:stn_id",
                        "value": "vocab:value",
                    },
                ]
            },
            "links": [],
            "extents": {
                "spatial": {
                    "bbox": feature_layer.datasource.bbox_to_list,
                    "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84",
                }
            },
            "providers": [provider],
            "limits": {
                "on_exceed": feature_layer.on_exceed,
                "max_items": feature_layer.max_items,
                "default_items": feature_layer.default_items,
            },
        }

    def get_available_crs_list(self, crs):
        self.handle_crs_setting(crs.ogc_uri)
        available_crs_list = [
            crs.ogc_uri,
            "http://www.opengis.net/def/crs/OGC/0/CRS84",
            "https://www.opengis.net/def/crs/OGC/0/CRS84",
        ]

        if Config().default_crs not in available_crs_list:
            available_crs_list.append(Config().default_crs)

        return available_crs_list


def get_dataset_field_constraints(field_properties: list[Field], geom_type: str):
    field_constraints: dict[str, dict] = {}

    for properties in field_properties:
        field: DatasourceField = properties.datasource_field

        schema: dict[str, str | int | float | bool] = {
            "title": field.alias or properties.name,
            "type": field.type_oapif,
        }

        if field.type_oapif_format:
            schema["format"] = field.type_oapif_format

        if field.comment:
            schema["description"] = field.comment

        if not field.nullable:
            schema["required"] = True

        if field.precision and field.precision > 0 and field.type_oapif == "number":
            # Specify how many decimal places are allowed
            try:  # noqa: SIM105
                schema["multipleOf"] = 1 / 10**field.precision
            except ValueError:
                pass

        if field.length and field.type_oapif == "string":
            schema["maxLength"] = field.length

        if field.length and (field.type_oapif in ["number", "integer"]):
            try:
                # Set max digits, e.g. 9999 for length=4
                schema["maximum"] = 10**field.length - 1
                if schema["multipleOf"]:
                    # Add decimal places, e.g. 9999.99
                    schema["maximum"] += 1 - schema["multipleOf"]
            except ValueError:
                pass
            except KeyError:
                pass

        field_constraints[str(properties.name)] = schema

    return field_constraints
