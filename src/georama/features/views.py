import os.path
import typing

import pygeoapi.api as core_api
import pygeoapi.api.itemtypes as itemtypes_api
from django.core.exceptions import BadRequest, PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from pygeoapi import l10n
from pygeoapi.api import API, APIRequest, apply_gzip
from pygeoapi.openapi import get_oas
from qgis_server_light.interface.qgis import BBox

from georama.data_integration.models import VectorDataSet
from georama.features.apps import appname
from georama.features.config_server import ServerConfig
from georama.features.features_config import Config
from georama.features.models import PublishedAsOgcApiFeatures

api = None


def landing_page(request: HttpRequest) -> HttpResponse:
    """
    OGC API landing page endpoint

    :request Django HTTP Request

    :returns: Django HTTP Response
    """
    return execute_from_django(core_api.landing_page, request)


def openapi(request: HttpRequest) -> HttpResponse:
    """
    OpenAPI endpoint

    :request Django HTTP Request

    :returns: Django HTTP Response
    """
    return execute_from_django(core_api.openapi_, request)


def conformance(request: HttpRequest) -> HttpResponse:
    """
    OGC API conformance endpoint

    :request Django HTTP Request

    :returns: Django HTTP Response
    """
    return execute_from_django(core_api.conformance, request)


def collections(
    request: HttpRequest, collection_id: typing.Optional[str] = None
) -> HttpResponse:
    """
    OGC API collections endpoint

    :request Django HTTP Request
    :param collection_id: collection identifier

    :returns: Django HTTP Response
    """
    return execute_from_django(core_api.describe_collections, request, collection_id)


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
        return execute_from_django(core_api.get_collection_schema, request, collection_id)
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
    else:
        raise BadRequest()

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
    else:
        raise BadRequest()

    return response_


def handle_runtime_config(request: HttpRequest) -> tuple[dict, dict]:
    server_config = ServerConfig().get()
    server_config["server"]["url"] = f"{request.scheme}://{request.get_host()}/features"
    for published_as in PublishedAsOgcApiFeatures.objects.all():
        if published_as.has_general_permission(request.user, appname):
            server_config["resources"][str(published_as.identifier)] = create_resource(
                published_as, request
            )
    return server_config, get_oas(server_config)


def execute_from_django(
    api_function, request: HttpRequest, *args, skip_valid_check=False
) -> HttpResponse:
    # TODO: This has to be stored somewhere, maybe a session store might be good
    server_config, openapi_config = handle_runtime_config(request)
    api = API(server_config, openapi_config)
    # TODO: this only needs to be done once the config actually changes aka published features are added or
    #       deleted!
    l10n._cfg_cache = {}

    api_request = APIRequest.from_django(request, api.locales)
    content: typing.Union[str, bytes]
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


def handle_crs_setting(crs: str):
    import pygeoapi.api as runtime_api

    if crs not in runtime_api.DEFAULT_CRS_LIST:
        runtime_api.DEFAULT_CRS_LIST.append(crs)


def create_ogr_provider(
    published_as: PublishedAsOgcApiFeatures,
    editable: bool,
    features_properties: typing.List[str],
) -> dict:
    source, path = published_as.dataset.source_to_qsl
    crs = published_as.dataset.crs_to_qsl
    handle_crs_setting(crs.ogc_uri),
    config = Config()
    # TODO: make this configurable
    driver_lookup = {"SHP": "ESRI Shapefile", "GPKG": "GPKG", "GDB": "OpenFileGDB"}
    available_crs_list = [crs.ogc_uri, "https://www.opengis.net/def/crs/OGC/0/CRS84"]
    if config.default_crs not in available_crs_list:
        available_crs_list.append(config.default_crs)
    provider_definition = {
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
        else os.path.basename(source.ogr.path).split(".")[0],
        # TODO:
        # "id_field": "fid",
        # "title_field": "kantonsname",
    }
    if published_as.column_permission:
        if len(features_properties) == 0:
            # for OGR `geom` is the standard geometry column
            features_properties = ["geom"]
        provider_definition["properties"] = features_properties

    return provider_definition


def create_postgres_provider(
    published_as: PublishedAsOgcApiFeatures,
    editable: bool,
    features_properties: typing.List[str],
) -> dict:
    source, path = published_as.dataset.source_to_qsl
    crs = published_as.dataset.crs_to_qsl
    handle_crs_setting(crs.ogc_uri)

    available_crs_list = [crs.ogc_uri, "https://www.opengis.net/def/crs/OGC/0/CRS84"]

    if Config().default_crs not in available_crs_list:
        available_crs_list.append(Config().default_crs)

    provider_definition = {
        "type": "feature",
        "name": "OG_POSTGRES",
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
    if published_as.column_permission:
        if len(features_properties) == 0:
            features_properties = [source.postgres.geometry_column]
        provider_definition["properties"] = features_properties

    return provider_definition


def create_resource(published_as: PublishedAsOgcApiFeatures, request: HttpRequest) -> dict:
    editable = (
        published_as.has_update_permission(request.user)
        or published_as.has_create_permission(request.user)
        or published_as.has_delete_permission(request.user)
    )

    features_properties = []
    if published_as.column_permission:
        features_properties = [
            c.name
            for c in published_as.columns.all()
            if c.has_general_permission(request.user)
        ]

    if published_as.dataset.driver.upper() == "POSTGRES":
        provider = create_postgres_provider(published_as, editable, features_properties)
    elif published_as.dataset.driver.upper() == "OGR":
        provider = create_ogr_provider(published_as, editable, features_properties)
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


def admin_publish_as_oapif(request: HttpRequest, vector_dataset_id: str):
    """
    helper function to hide actual connection in the database but make publishing straight forward.
    """
    vd = VectorDataSet.objects.filter(id=vector_dataset_id)[0]
    published_as_oapi = PublishedAsOgcApiFeatures(dataset=vd)
    published_as_oapi.save()
    return redirect("admin:features_publishedasogcapifeatures_changelist")
