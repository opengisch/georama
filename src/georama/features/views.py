import pygeoapi.api as inittime_api
from django.core.exceptions import PermissionDenied

from georama.features.features_config import Config

inittime_api.DEFAULT_CRS = Config().default_crs

import os.path
import typing

import pygeoapi.api.itemtypes as itemtypes_api
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from pygeoapi.api import API, APIRequest, apply_gzip
from qgis_server_light.interface.qgis import BBox

from georama.data_integration.models import VectorDataSet
from georama.features.apps import appname
from georama.features.config_openapi import config_openapi
from georama.features.config_server import config_server
from georama.features.models import PublishedAsOgcApiFeatures


def landing_page(request: HttpRequest) -> HttpResponse:
    """
    OGC API landing page endpoint

    :request Django HTTP Request

    :returns: Django HTTP Response
    """
    response_ = _feed_response(request, "landing_page")
    response = _to_django_response(*response_)

    return response


def openapi(request: HttpRequest) -> HttpResponse:
    """
    OpenAPI endpoint

    :request Django HTTP Request

    :returns: Django HTTP Response
    """
    response_ = _feed_response(request, "openapi_")
    response = _to_django_response(*response_)

    return response


def conformance(request: HttpRequest) -> HttpResponse:
    """
    OGC API conformance endpoint

    :request Django HTTP Request

    :returns: Django HTTP Response
    """
    response_ = _feed_response(request, "conformance")
    response = _to_django_response(*response_)

    return response


def collections(
    request: HttpRequest, collection_id: typing.Optional[str] = None
) -> HttpResponse:
    """
    OGC API collections endpoint

    :request Django HTTP Request
    :param collection_id: collection identifier

    :returns: Django HTTP Response
    """
    response_ = _feed_response(request, "describe_collections", collection_id)
    response = _to_django_response(*response_)
    return response


def collection_schema(
    request: HttpRequest, collection_id: typing.Optional[str] = None
) -> HttpResponse:
    """
    OGC API collections schema endpoint

    :request Django HTTP Request
    :param collection_id: collection identifier

    :returns: Django HTTP Response
    """
    if PublishedAsOgcApiFeatures.objects.get(identifier=collection_id).has_read_permission(
        request.user, appname
    ):
        response_ = _feed_response(request, "get_collection_schema", collection_id)
        response = _to_django_response(*response_)

        return response
    else:
        raise PermissionDenied()


def collection_queryables(
    request: HttpRequest, collection_id: typing.Optional[str] = None
) -> HttpResponse:
    """
    OGC API collections queryables endpoint

    :request Django HTTP Request
    :param collection_id: collection identifier

    :returns: Django HTTP Response
    """
    if PublishedAsOgcApiFeatures.objects.get(identifier=collection_id).has_read_permission(
        request.user, appname
    ):
        return execute_from_django(
            itemtypes_api.get_collection_queryables, request, collection_id
        )
    else:
        raise PermissionDenied()


def collection_items(request: HttpRequest, collection_id: str) -> HttpResponse:
    """
    OGC API collections items endpoint

    :request Django HTTP Request
    :param collection_id: collection identifier

    :returns: Django HTTP response
    """

    published_as = PublishedAsOgcApiFeatures.objects.get(identifier=collection_id)

    if request.method == "GET":
        if published_as.has_read_permission(request.user, appname):
            response_ = execute_from_django(
                itemtypes_api.get_collection_items,
                request,
                collection_id,
                skip_valid_check=True,
            )
        else:
            raise PermissionDenied()
    elif request.method == "POST":
        if published_as.has_create_permission(request.user, appname):
            if request.content_type is not None:
                if request.content_type == "application/geo+json":
                    response_ = execute_from_django(
                        itemtypes_api.manage_collection_item,
                        request,
                        "create",
                        collection_id,
                        skip_valid_check=True,
                    )
                else:
                    response_ = execute_from_django(
                        itemtypes_api.post_collection_items,
                        request,
                        collection_id,
                        skip_valid_check=True,
                    )
        else:
            raise PermissionDenied()
    elif request.method == "OPTIONS":
        if published_as.has_read_permission(request.user, appname):
            response_ = execute_from_django(
                itemtypes_api.manage_collection_item,
                request,
                "options",
                collection_id,
                skip_valid_check=True,
            )
        else:
            raise PermissionDenied()

    return response_


def collection_item(request: HttpRequest, collection_id: str, item_id: str) -> HttpResponse:
    """
    OGC API collections items endpoint

    :request Django HTTP Request
    :param collection_id: collection identifier
    :param item_id: item identifier

    :returns: Django HTTP response
    """
    published_as = PublishedAsOgcApiFeatures.objects.get(identifier=collection_id)

    if request.method == "GET":
        if published_as.has_read_permission(request.user, appname):
            response_ = execute_from_django(
                itemtypes_api.get_collection_item, request, collection_id, item_id
            )
        else:
            raise PermissionDenied()
    elif request.method == "PUT":
        if published_as.has_update_permission(request.user, appname):
            response_ = execute_from_django(
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
        if published_as.has_delete_permission(request.user, appname):
            response_ = execute_from_django(
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
        if published_as.has_read_permission(request.user, appname):
            response_ = execute_from_django(
                itemtypes_api.manage_collection_item,
                request,
                "options",
                collection_id,
                item_id,
                skip_valid_check=True,
            )
        else:
            raise PermissionDenied()

    return response_


def handle_runtime_config(request: HttpRequest) -> tuple[dict, dict]:
    server_config = config_server()
    openapi_config = config_openapi()
    server_config["server"]["url"] = f"http://{request.get_host()}/features"
    openapi_config["servers"][0]["url"] = server_config["server"]["url"]
    for published_as in PublishedAsOgcApiFeatures.objects.all():
        if published_as.has_general_permission(request.user, appname):
            server_config["resources"][str(published_as.identifier)] = create_resource(
                published_as, request
            )
            for path in create_oapi_cfg(published_as):
                openapi_config["paths"].update(path)
    return server_config, openapi_config


def _to_django_response(
    headers: typing.Mapping, status_code: int, content: str
) -> HttpResponse:
    """Convert API payload to a django response"""

    response = HttpResponse(content, status=status_code)

    for key, value in headers.items():
        response[key] = value
    return response


def _feed_response(
    request: HttpRequest, api_definition: str, *args, **kwargs
) -> typing.Tuple[typing.Dict, int, str]:
    """Use pygeoapi api to process the input request"""
    # TODO: make all this directly available from data integration and config DB
    server_config, openapi_config = handle_runtime_config(request)
    api = getattr(API(server_config, openapi_config), api_definition)

    return api(request, *args, **kwargs)


def execute_from_django(
    api_function, request: HttpRequest, *args, skip_valid_check=False
) -> HttpResponse:

    api_: API
    # TODO: make all this directly available from data integration and config DB
    server_config, openapi_config = handle_runtime_config(request)
    api_ = API(server_config, openapi_config)
    api_request = APIRequest.from_django(request, api_.locales)
    content: typing.Union[str, bytes]
    if not skip_valid_check and not api_request.is_valid():
        headers, status, content = api_.get_format_exception(api_request)
    else:

        headers, status, content = api_function(api_, api_request, *args)
        content = apply_gzip(headers, content)
    return _to_django_response(headers, status, content)


def handle_crs_setting(crs: str):
    import pygeoapi.api as runtime_api

    if crs not in runtime_api.DEFAULT_CRS_LIST:
        runtime_api.DEFAULT_CRS_LIST.append(crs)


def create_ogr_provider(published_as: PublishedAsOgcApiFeatures, editable: bool) -> dict:
    source, path = published_as.dataset.source_to_qsl
    crs = published_as.dataset.crs_to_qsl
    handle_crs_setting(crs.ogc_uri),
    config = Config()
    driver_lookup = {"SHP": "ESRI Shapefile", "GPKG": "GPKG"}
    available_crs_list = [crs.ogc_uri, "https://www.opengis.net/def/crs/OGC/0/CRS84"]
    if config.default_crs not in available_crs_list:
        available_crs_list.append(config.default_crs)
    return {
        "type": "feature",
        "name": "OGR",
        "data": {
            "source_type": driver_lookup[source.ogr.path.split(".")[-1].upper()],
            "source": os.path.join(
                config.path, published_as.dataset.project.mandant.name, source.ogr.path
            ),
            "source_capabilities": {"paging": True},
        },
        "editable": editable,
        "crs": available_crs_list,
        "storage_crs": crs.ogc_uri,
        "id_field": "fid",
        "layer": source.ogr.layer_name
        if source.ogr.layer_name is not None
        else os.path.basename(source.ogr.path).split(".")[0]
        # TODO:
        # "id_field": "fid",
        # "title_field": "kantonsname",
    }


def create_postgres_provider(published_as: PublishedAsOgcApiFeatures, editable: bool) -> dict:
    source, path = published_as.dataset.source_to_qsl
    crs = published_as.dataset.crs_to_qsl
    handle_crs_setting(crs.ogc_uri)

    available_crs_list = [crs.ogc_uri, "https://www.opengis.net/def/crs/OGC/0/CRS84"]

    if Config().default_crs not in available_crs_list:
        available_crs_list.append(Config().default_crs)

    return {
        "type": "feature",
        "name": "PostgreSQL",
        "data": {
            "host": source.postgres.host,
            "port": source.postgres.port,
            "dbname": source.postgres.dbname,
            "user": source.postgres.username,
            "password": source.postgres.password,
            "search_path": [source.postgres.schema],
        },
        "editable": editable,
        "crs": available_crs_list,
        "storage_crs": crs.ogc_uri,
        "id_field": source.postgres.key,
        "table": source.postgres.table,
        "geom_field": source.postgres.geometry_column
        # TODO:
        # "id_field": "fid",
        # "title_field": "kantonsname",
    }


def create_resource(published_as: PublishedAsOgcApiFeatures, request: HttpRequest) -> dict:
    editable = (
        published_as.has_update_permission(request.user, appname)
        or published_as.has_create_permission(request.user, appname)
        or published_as.has_delete_permission(request.user, appname)
    )
    if published_as.dataset.driver.upper() == "POSTGRES":
        provider = create_postgres_provider(published_as, editable)
    elif published_as.dataset.driver.upper() == "OGR":
        provider = create_ogr_provider(published_as, editable)
    else:
        raise NotImplementedError

    return {
        "type": "collection",
        "title": published_as.title,
        "description": published_as.description,
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
                "bbox": BBox.from_string(published_as.dataset.bbox).to_list(),
                "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84",
            }
        },
        "providers": [provider],
    }


def create_oapi_cfg(published_as: PublishedAsOgcApiFeatures) -> list[dict]:
    dataset_name = str(published_as.identifier)
    return [
        {
            f"/collections/{dataset_name}": {
                "get": {
                    "description": published_as.description,
                    "operationId": f"describe{dataset_name}Collection",
                    "parameters": [
                        {"$ref": "#/components/parameters/f"},
                        {"$ref": "#/components/parameters/lang"},
                    ],
                    "responses": {
                        "200": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/Collection"
                        },
                        "400": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/InvalidParameter"
                        },
                        "404": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/NotFound"
                        },
                        "500": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/ServerError"
                        },
                    },
                    "summary": "Get feature collection metadata",
                    "tags": [published_as.name],
                }
            }
        },
        {
            f"/collections/{dataset_name}/items": {
                "get": {
                    "description": published_as.description,
                    "operationId": f"get{dataset_name}Features",
                    "parameters": [
                        {
                            "description": "The optional f parameter indicates the output format which the "
                            "server shall provide as part of the response document. "
                            "The default format is GeoJSON.",
                            "explode": False,
                            "in": "query",
                            "name": "f",
                            "required": False,
                            "schema": {
                                "default": "json",
                                "enum": ["json", "html", "csv"],
                                "type": "string",
                            },
                            "style": "form",
                        },
                        {"$ref": "#/components/parameters/f"},
                        {"$ref": "#/components/parameters/lang"},
                        {"$ref": "#/components/parameters/bbox"},
                        {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/parameters/limit"
                        },
                        {"$ref": "#/components/parameters/crs"},
                        {"$ref": "#/components/parameters/bbox-crs"},
                        {"$ref": "#/components/parameters/vendorSpecificParameters"},
                        {
                            "$ref": "https://raw.githubusercontent.com/opengeospatial/ogcapi-records/master/core/openapi/parameters/sortby.yaml"
                        },
                        {"$ref": "#/components/parameters/offset"}
                        # TODO: add definition per column (we need to do a proper mapping from qgis infos)
                        # {
                        #     "explode": False,
                        #     "in": "query",
                        #     "name": "id",
                        #     "required": False,
                        #     "schema": {
                        #         "type": "string"
                        #     },
                        #     "style": "form"
                        # }
                    ],
                    "responses": {
                        "200": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/Features"
                        },
                        "400": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/InvalidParameter"
                        },
                        "404": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/NotFound"
                        },
                        "500": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/ServerError"
                        },
                    },
                    "summary": f"Get {published_as.name} features",
                    "tags": [published_as.name],
                    "options": {
                        "description": published_as.description,
                        "operationId": f"options{dataset_name}Features",
                        "responses": {"200": {"description": "options response"}},
                        "summary": "Options for Observations items",
                        "tags": ["obs"],
                    },
                }
            }
        },
        {
            f"/collections/{dataset_name}/items/{'{featureId}'}": {
                "get": {
                    "description": published_as.description,
                    "operationId": f"get{dataset_name}Feature",
                    "parameters": [
                        {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/parameters/featureId"
                        },
                        {"$ref": "#/components/parameters/crs"},
                        {"$ref": "#/components/parameters/f"},
                        {"$ref": "#/components/parameters/lang"},
                    ],
                    "responses": {
                        "200": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/Feature"
                        },
                        "400": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/InvalidParameter"
                        },
                        "404": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/NotFound"
                        },
                        "500": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/ServerError"
                        },
                    },
                    "summary": f"Get {published_as.name} feature by id",
                    "tags": [published_as.name],
                    "options": {
                        "description": published_as.description,
                        "operationId": f"options{published_as.name}Feature",
                        "parameters": [
                            {
                                "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/parameters/featureId"
                            }
                        ],
                        "responses": {"200": {"description": "options response"}},
                        "summary": "Options for Observations item by id",
                        "tags": ["obs"],
                    },
                }
            }
        },
        {
            f"/collections/{dataset_name}/queryables": {
                "get": {
                    "description": published_as.description,
                    "operationId": f"get{published_as.name}Queryables",
                    "parameters": [
                        {"$ref": "#/components/parameters/f"},
                        {"$ref": "#/components/parameters/lang"},
                    ],
                    "responses": {
                        "200": {"$ref": "#/components/responses/Queryables"},
                        "400": {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/InvalidParameter"
                        },
                        "404": {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/NotFound"
                        },
                        "500": {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/ServerError"
                        },
                    },
                    "summary": "Get Observations queryables",
                    "tags": ["obs"],
                }
            }
        },
        {
            f"/collections/{dataset_name}/schema": {
                "get": {
                    "description": published_as.description,
                    "operationId": f"get{published_as.name}Schema",
                    "parameters": [
                        {"$ref": "#/components/parameters/f"},
                        {"$ref": "#/components/parameters/lang"},
                    ],
                    "responses": {
                        "200": {"$ref": "#/components/responses/Queryables"},
                        "400": {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/InvalidParameter"
                        },
                        "404": {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/NotFound"
                        },
                        "500": {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/ServerError"
                        },
                    },
                    "summary": "Get Observations schema",
                    "tags": ["obs"],
                }
            }
        },
    ]


def admin_publish_as_oapif(request: HttpRequest, vector_dataset_id: str):
    """
    helper function to hide actual connection in the database but make publishing straight forward.
    """
    vd = VectorDataSet.objects.filter(id=vector_dataset_id)[0]
    published_as_oapi = PublishedAsOgcApiFeatures(dataset=vd)
    published_as_oapi.save()
    return redirect("admin:features_publishedasogcapifeatures_changelist")
