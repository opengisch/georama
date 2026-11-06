import json
import os.path
from functools import partial
from http import HTTPStatus
from typing import TYPE_CHECKING

import pygeoapi.api as core_api
import pygeoapi.api.itemtypes as itemtypes_api
from django.core.exceptions import BadRequest, PermissionDenied, ValidationError
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from guardian.core import ObjectPermissionChecker
from pygeoapi import l10n
from pygeoapi.api import API, APIRequest, apply_gzip
from pygeoapi.openapi import get_oas
from pygeoapi.util import to_json
from qgis_server_light.interface.exporter.extract import Range, Relation, ValueMap

from georama.features.apps import FeaturesConfig
from georama.features.config_server import ServerConfig
from georama.features.features_config import Config
from georama.features.geometry_type import UnsupportedGeometryTypeError, geojson_geometry_type
from georama.features.models import FeatureLayer, Field
from georama.features.references import ReferenceTarget, reference_keywords
from georama.integration.models import Vector

if TYPE_CHECKING:
    from georama.integration.models import VectorField as DatasourceField

api = None


# THIS IS A HACK, WE CREATE DICT WHICH BASICALLY NEVER STORES ANYTHING ON SET
# SO ITS THREAD SAFE
class _NoCache(dict):
    def __setitem__(self, key, value):
        pass


l10n._cfg_cache = _NoCache()


WORLD_BBOX = [-180.0, -90.0, 180.0, 90.0]
CRS84_URI = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"


def get_collection_schema_with_geometry_format(
    api: API, request: APIRequest, dataset: str, geometry_type_wkb: str
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

    The geometry type of QSL is mapped to its GeoJSON type.
    """
    geometry_format = None
    if geometry_type_wkb is not None:
        try:
            geometry_format = f"geometry-{geojson_geometry_type(geometry_type_wkb).lower()}"
        except UnsupportedGeometryTypeError as e:
            return api.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                request.get_response_headers(**api.api_headers),
                request.format,
                "NoApplicableCode",
                str(e),
            )

    headers, status, content = core_api.get_collection_schema(api, request, dataset)
    if status != HTTPStatus.OK or headers.get("Content-Type") != "application/schema+json":
        return headers, status, content

    schema = json.loads(content)
    schema["required"] = []
    geometry = schema["properties"].get("geometry")
    if geometry is not None and geometry_format is None:
        # geometryless datasources have no geometry property at all
        del schema["properties"]["geometry"]
    elif geometry is not None:
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
    landing_url_name = "features:landing"
    perm_view = "view_objects_on_published_layer"
    perm_create = "create_objects_on_published_layer"
    perm_update = "update_objects_on_published_layer"
    perm_delete = "delete_objects_on_published_layer"

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
            return self.model.objects.accessible_layers(
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
            collection_id, self.perm_view, include_public=True
        ).get()
        geom_type = (
            self.get_vector(feature_layer).geometry_type_wkb
            if self.get_vector(feature_layer).is_spatial
            else None
        )
        return self.execute_from_django(
            # a bit hacky, but we use
            # https://docs.python.org/3/library/functools.html#functools.partial
            # to force wat we want
            partial(get_collection_schema_with_geometry_format, geometry_type_wkb=geom_type),
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
        _ = self.get_collection_or_404_or_403(collection_id, self.perm_view, include_public=True)
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
                collection_id, self.perm_view, include_public=True
            )
            response_ = self.execute_from_django(
                itemtypes_api.get_collection_items,
                request,
                collection_id,
                skip_valid_check=True,
                collection_id=collection_id,
            )
        elif request.method == "POST":
            _ = self.get_collection_or_404_or_403(collection_id, self.perm_create)
            violation = self.get_value_violation(request, collection_id)
            if violation is not None:
                return violation
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
                collection_id, self.perm_view, include_public=True
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
                collection_id, self.perm_view, include_public=True
            )
            response_ = self.execute_from_django(
                itemtypes_api.get_collection_item,
                request,
                collection_id,
                item_id,
                collection_id=collection_id,
            )
        elif request.method == "PUT":
            _ = self.get_collection_or_404_or_403(collection_id, self.perm_update)
            violation = self.get_value_violation(request, collection_id)
            if violation is not None:
                return violation
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
            _ = self.get_collection_or_404_or_403(collection_id, self.perm_delete)
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
                collection_id, self.perm_view, include_public=True
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

    def get_value_violation(self, request: HttpRequest, collection_id: str) -> HttpResponse | None:
        """Answers 400 if a property of the written item is not in the `oneOf` / `enum`
        list of its field. The database does not check value lists, so this is the check.

        :returns: Django HTTP Response on violation, None otherwise
        """
        try:
            payload = json.loads(request.body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            # malformed bodies are answered by pygeoapi
            return None
        feature_layers = self.accessible_feature_layers(request, collection_id)
        if not feature_layers or not isinstance(payload, dict):
            return None

        feature_layer = feature_layers[0]
        constraints = get_dataset_field_constraints(
            self.get_visible_fields(feature_layer), self.get_vector(feature_layer).geometry_type_wkb
        )
        properties = payload.get("properties") or {}
        for name, schema in constraints.items():
            value = properties.get(name)
            if value is None:
                continue
            if "oneOf" in schema:
                allowed = [option["const"] for option in schema["oneOf"]]
            else:
                allowed = schema.get("enum")
            if allowed is not None and value not in allowed:
                return JsonResponse(
                    {
                        "code": "InvalidParameterValue",
                        "description": f"Value {value!r} is not allowed for {name}",
                    },
                    status=HTTPStatus.BAD_REQUEST,
                )
        return None

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
            f"{request.scheme}://{request.get_host()}{reverse(self.landing_url_name)}"
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
        feature_layers = self.model.objects.accessible_layers(
            self.request.georama_organisation,
            request.user,
            [self.perm_view],
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

    @staticmethod
    def get_primary_key_name(vector: Vector) -> str:
        """The OGR provider needs the name of the identifier column. OGR sources have no key
        in the QSL export, so it is taken from the primary key field of the datasource.
        """
        for vector_field in vector.fields.all():
            if vector_field.definition and vector_field.field_definition_qsl.is_primary_key:
                return vector_field.name
        return "fid"

    def create_ogr_provider(
        self,
        feature_layer: FeatureLayer,
        editable: bool,
        features_properties: list[Field],
    ) -> dict:
        source = self.get_vector(feature_layer).source_to_qsl

        crs = self.get_vector(feature_layer).crs_to_qsl
        available_crs_list = self.get_available_crs_list(crs)

        # TODO: make this configurable
        driver_lookup = {"SHP": "ESRI Shapefile", "GPKG": "GPKG", "GDB": "OpenFileGDB"}

        # The geometry column name may differ, setting it to None works for all cases
        geom_field = None
        geom_type = self.get_vector(feature_layer).geometry_type_wkb

        field_constraints = self.get_field_constraints(feature_layer, features_properties)

        provider_definition = {
            "type": "feature",
            "name": "OG_OGR",
            "data": {
                "source_type": driver_lookup[source.ogr.path.split(".")[-1].upper()],
                "source": os.path.join(
                    Config().path,
                    self.get_vector(feature_layer).project.organisation_folder,
                    os.path.dirname(self.get_vector(feature_layer).project.path),
                    source.ogr.path,
                ),
                "source_capabilities": {"paging": True},
            },
            "editable": editable,
            "crs": available_crs_list,
            "storage_crs": crs.ogc_uri if crs is not None else CRS84_URI,
            "id_field": self.get_primary_key_name(self.get_vector(feature_layer)),
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
        source = self.get_vector(feature_layer).source_to_qsl

        crs = self.get_vector(feature_layer).crs_to_qsl
        available_crs_list = self.get_available_crs_list(crs)

        geom_field = (
            source.postgres.geometry_column if self.get_vector(feature_layer).is_spatial else None
        )
        geom_type = self.get_vector(feature_layer).geometry_type_wkb

        field_constraints = self.get_field_constraints(feature_layer, features_properties)

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
            "storage_crs": crs.ogc_uri if crs is not None else CRS84_URI,
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
                self.perm_create,
                self.perm_update,
                self.perm_delete,
            )
        )

        features_properties = self.get_visible_fields(feature_layer)

        if self.get_vector(feature_layer).driver.upper() == "POSTGRES":
            provider = self.create_postgres_provider(feature_layer, editable, features_properties)
        elif self.get_vector(feature_layer).driver.upper() == "OGR":
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
                    # geometryless datasources have no bbox, pygeoapi needs an extent anyway
                    "bbox": self.get_vector(feature_layer).bbox_to_list or WORLD_BBOX,
                    "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84",
                }
            },
            "providers": [provider],
            "limits": self.get_limits(feature_layer),
        }

    def get_vector(self, feature_layer) -> Vector:
        """The vector datasource the collection is served from."""
        return feature_layer.datasource

    def get_field_constraints(self, feature_layer: FeatureLayer, features_properties: list) -> dict:
        datasource = self.get_vector(feature_layer)
        return get_dataset_field_constraints(
            features_properties,
            datasource.geometry_type_wkb,
            datasource.qgis_layer_id,
            self.get_relations(datasource.project),
            self.get_reference_targets(datasource.project),
        )

    @staticmethod
    def get_relations(project) -> list[Relation]:
        if not project.config:
            # a project without export has no relations
            return []
        return project.config_as_dataclass.relations

    @staticmethod
    def get_reference_targets(project) -> dict[str, ReferenceTarget]:
        """The feature layers of the project published on this mount, keyed by QGIS layer id.
        Only layers with a primary key field can be referenced.
        """
        targets: dict[str, ReferenceTarget] = {}
        layers = (
            FeatureLayer.objects.filter(datasource__project=project)
            .select_related("datasource")
            .prefetch_related("datasource__fields")
        )
        for layer in layers:
            key_field = next(
                (
                    f.name
                    for f in layer.datasource.fields.all()
                    if f.definition and f.field_definition_qsl.is_primary_key
                ),
                None,
            )
            if key_field is not None:
                targets[layer.datasource.qgis_layer_id] = ReferenceTarget(str(layer.id), key_field)
        return targets

    def get_visible_fields(self, feature_layer: FeatureLayer) -> list[Field]:
        return [p for p in feature_layer.fields.all() if p.visible]

    def get_limits(self, feature_layer: FeatureLayer) -> dict:
        return {
            "on_exceed": feature_layer.on_exceed,
            "max_items": feature_layer.max_items,
            "default_items": feature_layer.default_items,
        }

    def get_available_crs_list(self, crs):
        if crs is None:
            available_crs_list = []
        else:
            self.handle_crs_setting(crs.ogc_uri)
            available_crs_list = [crs.ogc_uri]
        available_crs_list += [
            "http://www.opengis.net/def/crs/OGC/0/CRS84",
            "https://www.opengis.net/def/crs/OGC/0/CRS84",
        ]

        if Config().default_crs not in available_crs_list:
            available_crs_list.append(Config().default_crs)

        return available_crs_list


def get_dataset_field_constraints(
    field_properties: list[Field],
    geom_type: str,
    layer_id: str,
    relations: list[Relation],
    targets: dict[str, ReferenceTarget],
):
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

        if field.definition:
            qsl_field = field.field_definition_qsl
            if qsl_field.is_primary_key and qsl_field.is_generated:
                # generated identifier, the client must not send it
                schema.pop("required", None)
                schema["readOnly"] = True
            widget = qsl_field.editor_widget
            if widget is not None and widget.value_map is not None:
                schema.update(value_map_constraints(widget.value_map, field.type_oapif))
            if widget is not None and widget.range is not None:
                schema.update(range_constraints(widget.range))
            schema.update(
                reference_keywords(str(properties.name), layer_id, widget, relations, targets)
            )

        field_constraints[str(properties.name)] = schema

    return field_constraints


VALUE_MAP_CASTS = {"integer": int, "number": float}


def value_map_constraints(value_map: "ValueMap", type_oapif: str) -> dict:
    """Maps a QGIS ValueMap to `oneOf`, `enum` only where key and description are equal.

    Keys are cast to the schema type, a key which does not fit is left out of the list.
    """
    cast = VALUE_MAP_CASTS.get(type_oapif, str)
    entries = []
    for entry in value_map.entries:
        try:
            entries.append((cast(entry.key), entry))
        except ValueError:
            continue

    constraints: dict = {
        "oneOf": [{"const": key, "title": entry.description} for key, entry in entries],
    }
    if entries and all(entry.key == entry.description for _, entry in entries):
        constraints["enum"] = [key for key, _ in entries]
    return constraints


def range_constraints(widget_range: "Range") -> dict:
    constraints = {}
    if widget_range.minimum is not None:
        constraints["minimum"] = widget_range.minimum
    if widget_range.maximum is not None:
        constraints["maximum"] = widget_range.maximum
    return constraints
