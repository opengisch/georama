import os.path

import pygeoapi.api as core_api
import pygeoapi.api.itemtypes as itemtypes_api
from django.core.exceptions import BadRequest, PermissionDenied
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse
from django.views import View
from guardian.shortcuts import get_objects_for_user, get_perms
from pygeoapi import l10n
from pygeoapi.api import API, APIRequest, apply_gzip
from pygeoapi.openapi import get_oas

from georama.features.apps import FeaturesConfig
from georama.features.config_server import ServerConfig
from georama.features.features_config import Config
from georama.features.models import FeatureLayer, Field
from georama.integration.models import VectorField as DatasourceField

api = None


class PygeoapiServer(View):
    action = None
    model = FeatureLayer

    @classmethod
    def urls(cls):
        """
        Prepares a tuple of 2 elements which can be used directly with django.urls.include.
        """

        patterns = []
        return (patterns, FeaturesConfig.label)

    def dispatch(self, request, *args, **kwargs):
        handler = getattr(self, f"{self.action}", None)

        if callable(handler):
            return handler(request, *args, **kwargs)

        raise Http404(f"Unknown action: {self.action!r}")

    def execute_from_django(
        self, api_function, request: HttpRequest, *args, skip_valid_check=False
    ) -> HttpResponse:
        # TODO: This has to be stored somewhere, maybe a session store might be good
        server_config, openapi_config = self.handle_runtime_config(request)
        api = API(server_config, openapi_config)
        # TODO: this only needs to be done once the config actually changes aka
        #  published features are added or deleted!
        l10n._cfg_cache = {}

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

    def get_collection_or_404(self, collection_id: str):
        try:
            return self.model.objects.get(id=collection_id)
        except self.model.DoesNotExist as e:
            raise Http404("Collection not found") from e

    def landing(self, request: HttpRequest) -> HttpResponse:
        """
        OGC API landing page endpoint

        :request Django HTTP Request

        :returns: Django HTTP Response
        """
        return self.execute_from_django(core_api.landing_page, request)

    def openapi(self, request: HttpRequest) -> HttpResponse:
        """
        OpenAPI endpoint

        :request Django HTTP Request

        :returns: Django HTTP Response
        """
        return self.execute_from_django(core_api.openapi_, request)

    def conformance(self, request: HttpRequest) -> HttpResponse:
        """
        OGC API conformance endpoint

        :request Django HTTP Request

        :returns: Django HTTP Response
        """
        return self.execute_from_django(core_api.conformance, request)

    def collections(self, request: HttpRequest, collection_id: str | None = None) -> HttpResponse:
        """
        OGC API collections endpoint

        :request Django HTTP Request
        :param collection_id: collection identifier

        :returns: Django HTTP Response
        """
        return self.execute_from_django(core_api.describe_collections, request, collection_id)

    def collection_schema(
        self, request: HttpRequest, collection_id: str | None = None
    ) -> HttpResponse:
        """
        OGC API collections schema endpoint

        :request Django HTTP Request
        :param collection_id: collection identifier

        :returns: Django HTTP Response
        """
        feature_layer = self.get_collection_or_404(collection_id)
        if "view_featurelayer" in get_perms(request.user, feature_layer):
            return self.execute_from_django(core_api.get_collection_schema, request, collection_id)
        else:
            raise PermissionDenied()

    def collection_queryables(
        self, request: HttpRequest, collection_id: str | None = None
    ) -> HttpResponse:
        """
        OGC API collections queryables endpoint

        :request Django HTTP Request
        :param collection_id: collection identifier

        :returns: Django HTTP Response
        """
        feature_layer = self.get_collection_or_404(collection_id)
        if "view_featurelayer" in get_perms(request.user, feature_layer):
            return self.execute_from_django(
                itemtypes_api.get_collection_queryables, request, collection_id
            )
        else:
            raise PermissionDenied()

    def collection_items(self, request: HttpRequest, collection_id: str) -> HttpResponse:
        """
        OGC API collections items endpoint

        :request Django HTTP Request
        :param collection_id: collection identifier

        :returns: Django HTTP response
        """

        feature_layer = self.get_collection_or_404(collection_id)

        if request.method == "GET":
            if "view_featurelayer" in get_perms(request.user, feature_layer):
                response_ = self.execute_from_django(
                    itemtypes_api.get_collection_items,
                    request,
                    collection_id,
                    skip_valid_check=True,
                )
            else:
                raise PermissionDenied()
        elif request.method == "POST":
            if "add_featurelayer" in get_perms(request.user, feature_layer):
                if request.content_type is not None:
                    if request.content_type == "application/geo+json":
                        response_ = self.execute_from_django(
                            itemtypes_api.manage_collection_item,
                            request,
                            "create",
                            collection_id,
                            skip_valid_check=True,
                        )
                    else:
                        response_ = self.execute_from_django(
                            itemtypes_api.post_collection_items,
                            request,
                            collection_id,
                            skip_valid_check=True,
                        )
            else:
                raise PermissionDenied()
        elif request.method == "OPTIONS":
            if "view_featurelayer" in get_perms(request.user, feature_layer):
                response_ = self.execute_from_django(
                    itemtypes_api.manage_collection_item,
                    request,
                    "options",
                    collection_id,
                    skip_valid_check=True,
                )
            else:
                raise PermissionDenied()
        else:
            raise BadRequest()

        return response_

    def collection_item(
        self, request: HttpRequest, collection_id: str, item_id: str
    ) -> HttpResponse:
        """
        OGC API collections items endpoint

        :request Django HTTP Request
        :param collection_id: collection identifier
        :param item_id: item identifier

        :returns: Django HTTP response
        """
        feature_layer = self.get_collection_or_404(collection_id)
        if request.method == "GET":
            if "view_featurelayer" in get_perms(request.user, feature_layer):
                response_ = self.execute_from_django(
                    itemtypes_api.get_collection_item, request, collection_id, item_id
                )
            else:
                raise PermissionDenied()
        elif request.method == "PUT":
            if "change_featurelayer" in get_perms(request.user, feature_layer):
                response_ = self.execute_from_django(
                    itemtypes_api.manage_collection_item,
                    request,
                    "update",
                    collection_id,
                    item_id,
                    skip_valid_check=True,
                )
            else:
                raise PermissionDenied()
        elif request.method == "DELETE":
            if "delete_featurelayer" in get_perms(request.user, feature_layer):
                response_ = self.execute_from_django(
                    itemtypes_api.manage_collection_item,
                    request,
                    "delete",
                    collection_id,
                    item_id,
                    skip_valid_check=True,
                )
            else:
                raise PermissionDenied()
        elif request.method == "OPTIONS":
            if "view_featurelayer" in get_perms(request.user, feature_layer):
                response_ = self.execute_from_django(
                    itemtypes_api.manage_collection_item,
                    request,
                    "options",
                    collection_id,
                    item_id,
                    skip_valid_check=True,
                )
            else:
                raise PermissionDenied()
        else:
            raise BadRequest()

        return response_

    def handle_runtime_config(self, request: HttpRequest) -> tuple[dict, dict]:
        server_config = ServerConfig().get()
        server_config["server"]["url"] = (
            f"{request.scheme}://{request.get_host()}{reverse('features:index')}"
        )
        for feature_layer in get_objects_for_user(request.user, ["view_featurelayer"], self.model):
            server_config["resources"][str(feature_layer.id)] = self.create_resource(
                feature_layer, request
            )
        return server_config, get_oas(server_config)

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
        available_crs_list = self.getAvailableCrsList(crs)

        # TODO: make this configurable
        driver_lookup = {"SHP": "ESRI Shapefile", "GPKG": "GPKG", "GDB": "OpenFileGDB"}

        # The geometry column name may differ, setting it to None works for all cases
        geom_field = None
        geom_type = feature_layer.datasource.geometry_type_wkb

        field_constraints = getDatasetFieldConstraints(features_properties, geom_type)

        provider_definition = {
            "type": "feature",
            "name": "OG_OGR",
            "data": {
                "source_type": driver_lookup[source.ogr.path.split(".")[-1].upper()],
                "source": os.path.join(
                    Config().path, feature_layer.datasource.project.collection.name, source.ogr.path
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
        available_crs_list = self.getAvailableCrsList(crs)

        geom_field = source.postgres.geometry_column
        geom_type = feature_layer.datasource.geometry_type_wkb

        field_constraints = getDatasetFieldConstraints(features_properties, geom_type)

        provider_definition = {
            "type": "feature",
            "name": "OG_SQL",
            "data": {
                "host": source.postgres.host,
                "port": source.postgres.port,
                "dbname": source.postgres.dbname,
                "user": source.postgres.username,
                "password": source.postgres.password,
                "search_path": [source.postgres.schema],
                "options": {"sslmode": source.postgres.sslmode},
            },
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

    def create_resource(self, feature_layer: FeatureLayer, request: HttpRequest) -> dict:
        editable = any(
            p in get_perms(request.user, feature_layer)
            for p in ("add_featurelayer", "change_featurelayer", "delete_featurelayer")
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

    def getAvailableCrsList(self, crs):
        self.handle_crs_setting(crs.ogc_uri)
        available_crs_list = [
            crs.ogc_uri,
            "http://www.opengis.net/def/crs/OGC/0/CRS84",
            "https://www.opengis.net/def/crs/OGC/0/CRS84",
        ]

        if Config().default_crs not in available_crs_list:
            available_crs_list.append(Config().default_crs)

        return available_crs_list


def getDatasetFieldConstraints(field_properties: list[Field], geom_type: str):
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

    # In the schema, the geometry column is always called
    # `geometry`, independent of the actual column name in the DB
    api_geom_type = f"geometry-{geom_type if geom_type != 'UNSET' else 'any'}"
    field_constraints["geometry"] = {
        "type": api_geom_type,
        "format": api_geom_type,
        "x-ogc-role": "primary-geometry",
    }
    return field_constraints
