import os.path

import pygeoapi.api as core_api
import pygeoapi.api.itemtypes as itemtypes_api
from django.apps import apps
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group, Permission, User
from django.core.exceptions import BadRequest, PermissionDenied
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext as _
from django.views import View
from pygeoapi import l10n
from pygeoapi.api import API, APIRequest, apply_gzip
from pygeoapi.openapi import get_oas
from qgis_server_light.interface.qgis import BBox

from georama.core.menu import BreadCrumb
from georama.core.services.permission import DBService
from georama.core.views.generic.delete import GeoramaDeleteView
from georama.core.views.generic.detail import GeoramaDetailView
from georama.core.views.generic.list import GeoramaListView
from georama.core.views.generic.mixins import (
    GeoramaAnyPermissionRequiredMixin,
    GeoramaLoginRequiredMixin,
)
from georama.core.views.generic.update import GeoramaUpdateView
from georama.data_integration.models import Field, VectorDataSet
from georama.features.apps import central_app_label
from georama.features.config_server import ServerConfig
from georama.features.features_config import Config
from georama.features.models import ColumnOgcApiFeatures, PublishedAsOgcApiFeatures

api = None


class PygeoapiServer(View):
    action = None
    model = PublishedAsOgcApiFeatures

    @classmethod
    def urls(cls):
        """
        Prepares a tuple of 2 elements which can be used directly with django.urls.include.
        """

        patterns = []
        return (patterns, central_app_label)

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

    def collections(
        self, request: HttpRequest, collection_id: str | None = None
    ) -> HttpResponse:
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
        if self.model.objects.get(identifier=collection_id).has_read_permission(
            request.user, central_app_label
        ):
            return self.execute_from_django(
                core_api.get_collection_schema, request, collection_id
            )
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
        if self.model.objects.get(identifier=collection_id).has_read_permission(
            request.user, central_app_label
        ):
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

        published_as = self.model.objects.get(identifier=collection_id)

        if request.method == "GET":
            if published_as.has_read_permission(request.user, central_app_label):
                response_ = self.execute_from_django(
                    itemtypes_api.get_collection_items,
                    request,
                    collection_id,
                    skip_valid_check=True,
                )
            else:
                raise PermissionDenied()
        elif request.method == "POST":
            if published_as.has_create_permission(request.user, central_app_label):
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
            if published_as.has_read_permission(request.user, central_app_label):
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
        published_as = self.model.objects.get(identifier=collection_id)

        if request.method == "GET":
            if published_as.has_read_permission(request.user, central_app_label):
                response_ = self.execute_from_django(
                    itemtypes_api.get_collection_item, request, collection_id, item_id
                )
            else:
                raise PermissionDenied()
        elif request.method == "PUT":
            if published_as.has_update_permission(request.user, central_app_label):
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
            if published_as.has_delete_permission(request.user, central_app_label):
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
            if published_as.has_read_permission(request.user, central_app_label):
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
        server_config["server"][
            "url"
        ] = f"{request.scheme}://{request.get_host()}/features/pygeoapi"
        for published_as in self.model.objects.all():
            if published_as.has_general_permission(request.user, central_app_label):
                server_config["resources"][str(published_as.identifier)] = (
                    self.create_resource(published_as, request)
                )
        return server_config, get_oas(server_config)

    @staticmethod
    def handle_crs_setting(crs: str):
        import pygeoapi.api as runtime_api

        if crs not in runtime_api.DEFAULT_CRS_LIST:
            runtime_api.DEFAULT_CRS_LIST.append(crs)

    def create_ogr_provider(
        self,
        published_as: PublishedAsOgcApiFeatures,
        editable: bool,
        features_properties: list[ColumnOgcApiFeatures],
    ) -> dict:
        source, _ = published_as.dataset.source_to_qsl

        crs = published_as.dataset.crs_to_qsl
        available_crs_list = self.getAvailableCrsList(crs)

        # TODO: make this configurable
        driver_lookup = {"SHP": "ESRI Shapefile", "GPKG": "GPKG", "GDB": "OpenFileGDB"}

        # for OGR `geom` is the standard geometry column
        geom_field = "geom"
        geom_type = published_as.dataset.geometry_type_wkb

        field_constraints = getDatasetFieldConstraints(
            features_properties, geom_field, geom_type
        )

        provider_definition = {
            "type": "feature",
            "name": "OG_OGR",
            "data": {
                "source_type": driver_lookup[source.ogr.path.split(".")[-1].upper()],
                "source": os.path.join(
                    Config().path, published_as.dataset.project.mandant.name, source.ogr.path
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
            "properties": features_properties,
            "field_constraints": field_constraints,
        }

        return provider_definition

    def create_postgres_provider(
        self,
        published_as: PublishedAsOgcApiFeatures,
        editable: bool,
        features_properties: list[ColumnOgcApiFeatures],
    ) -> dict:
        source, _ = published_as.dataset.source_to_qsl

        crs = published_as.dataset.crs_to_qsl
        available_crs_list = self.getAvailableCrsList(crs)

        geom_field = source.postgres.geometry_column
        geom_type = published_as.dataset.geometry_type_wkb

        field_constraints = getDatasetFieldConstraints(
            features_properties, geom_field, geom_type
        )

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
            "properties": features_properties,
            "field_constraints": field_constraints,
        }

        return provider_definition

    def create_resource(
        self, published_as: PublishedAsOgcApiFeatures, request: HttpRequest
    ) -> dict:
        editable = (
            published_as.has_update_permission(request.user, central_app_label)
            or published_as.has_create_permission(request.user, central_app_label)
            or published_as.has_delete_permission(request.user, central_app_label)
        )

        features_properties = [
            p
            for p in published_as.columns.all()
            if not published_as.column_permission
            or p.has_general_permission(request.user, central_app_label)
        ]

        if published_as.dataset.driver.upper() == "POSTGRES":
            provider = self.create_postgres_provider(
                published_as, editable, features_properties
            )
        elif published_as.dataset.driver.upper() == "OGR":
            provider = self.create_ogr_provider(published_as, editable, features_properties)
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
            "limits": {
                "on_exceed": published_as.on_exceed,
                "max_items": published_as.max_items,
                "default_items": published_as.default_items,
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


def getDatasetFieldConstraints(
    field_properties: list[ColumnOgcApiFeatures], geom_field: str, geom_type: str
):
    field_constraints: dict[str, dict] = {}

    for properties in field_properties:
        field: Field = properties.dataset_column

        # Handle geom separately
        if properties.name == geom_field:
            continue

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
    field_constraints["geometry"] = {
        "format": f'geometry-{geom_type if geom_type != "UNSET" else "any"}',
        "x-ogc-role": "primary-geometry",
    }
    return field_constraints


class PublishLayer(GeoramaLoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = PublishedAsOgcApiFeatures.perm_add()

    def get(self, request: HttpRequest, vector_dataset_id: str):
        """
        helper function to hide actual connection in the database but make publishing
        straight forward.
        """
        vd = VectorDataSet.objects.filter(pk=vector_dataset_id).get()
        published_as_oapi = PublishedAsOgcApiFeatures(dataset=vd)
        published_as_oapi.save()

        next_url = request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
        ):
            return redirect(next_url)
        return redirect(f"{central_app_label}:layer-list")


class Index(GeoramaListView):
    """
    This view is the apps landing page. It shows the available published
    layers a user can access. This is also available in public and shows
    layers which are public too. However, the important part is, that we
    use the Georama inherent ObjectPermissionSystem `PublishedAs` here.
    Not the Django model permission system.
    """

    model = PublishedAsOgcApiFeatures
    template_name = "features/index.html"

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title),
        ]

    def get_queryset(self):
        permitted_layers = []
        layers = self.model.objects.all()
        for layer in layers:
            if layer.has_general_permission(self.request.user, central_app_label):
                permitted_layers.append(layer)
        return permitted_layers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (
            self.request.user.has_perm(self.model.perm_view())
            or self.request.user.has_perm(self.model.perm_change())
            or self.request.user.has_perm(self.model.perm_delete())
            or self.request.user.has_perm(self.model.perm_add())
            or self.request.user.has_perm(self.model.perm_manage_permissions())
        ):
            context["breadcrumb_action_url"] = f"{central_app_label}:layer-list"
            context["breadcrumb_action_icon"] = "fa fa-wrench"
            context["breadcrumb_action_title"] = _("Manage Layers")
            context["breadcrumb_action_tooltip"] = _("Manage published layers")
        return context


class LayerListView(
    GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, GeoramaListView
):
    model = PublishedAsOgcApiFeatures
    template_name = "features/list.html"
    permission_required = [
        model.perm_view(),
        model.perm_change(),
        model.perm_delete(),
        model.perm_add(),
        model.perm_manage_permissions(),
    ]

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers")),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.has_perm(self.model.perm_add()):
            context["breadcrumb_action_url"] = f"{central_app_label}:layer-source-list"
            context["breadcrumb_action_icon"] = "fa fa-circle-plus"
            context["breadcrumb_action_title"] = _("publish layer")
            context["breadcrumb_action_tooltip"] = _("Publish a new features layer")
        return context


class PublishListView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaListView):
    model = VectorDataSet
    template_name = "features/publish.html"
    permission_required = PublishedAsOgcApiFeatures.perm_add()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(_("Add")),
        ]


class FeatureDetailView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDetailView):
    model = PublishedAsOgcApiFeatures
    permission_required = model.perm_view()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(self.object.title or self.object.name),
        ]

    def get_context_data(self, **kwargs):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        context = super().get_context_data(**kwargs)
        context["update_view_name"] = f"{app_menu.app_label}:layer-update"
        context["delete_view_name"] = f"{app_menu.app_label}:layer-delete"
        context["permission_view_name"] = f"{app_menu.app_label}:layer-permission-list"
        context["perm_change"] = self.request.user.has_perm(self.model.perm_change())
        context["perm_manage_permission"] = self.request.user.has_perm(
            self.model.perm_manage_permissions()
        )
        context["perm_delete"] = self.request.user.has_perm(self.model.perm_delete())
        return context


class FeatureUpdateView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaUpdateView):
    model = PublishedAsOgcApiFeatures
    fields = [
        "title",
        "name",
        "description",
        "default_items",
        "max_items",
        "on_exceed",
        "public",
        "license",
        "fees",
        "access_constraints",
    ]
    permission_required = model.perm_change()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                self.object.title or self.object.name,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs["pk"]}
                ),
            ),
        ]

    def get_context_data(self, **kwargs):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        context = super().get_context_data(**kwargs)
        context["delete_view_name"] = f"{app_menu.app_label}:layer-delete"
        context["permission_view_name"] = f"{app_menu.app_label}:layer-permission-list"
        context["perm_manage_permission"] = self.request.user.has_perm(
            self.model.perm_manage_permissions()
        )
        context["perm_delete"] = self.request.user.has_perm(self.model.perm_delete())
        return context


class FeatureDeleteView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDeleteView):
    model = PublishedAsOgcApiFeatures
    success_url = reverse_lazy(f"{central_app_label}:layer-list")
    permission_required = model.perm_delete()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                self.object.title or self.object.name,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs["pk"]}
                ),
            ),
        ]


class PermissionView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDetailView):
    model = Permission
    template_name = "core/permission.html"
    permission_required = PublishedAsOgcApiFeatures.perm_manage_permissions()

    def get_object(self, queryset=None):
        object_pk = self.kwargs.get("pk")
        dbs_permission = DBService(PublishedAsOgcApiFeatures, central_app_label)
        return dbs_permission.get_permission_lookup(object_pk)

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                PublishedAsOgcApiFeatures.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_user_url"] = reverse(
            f"{central_app_label}:layer-permission-user-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        context["add_group_url"] = reverse(
            f"{central_app_label}:layer-permission-group-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        return context


class UserListView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaListView):
    model = User
    template_name = "core/user.html"
    permission_required = PublishedAsOgcApiFeatures.perm_manage_permissions()

    def get_queryset(self):
        return (
            User.objects.exclude(
                user_permissions__codename__icontains=str(self.kwargs.get("pk"))
            )
            .exclude(pk=None)
            .filter(is_superuser=False)
        )

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                PublishedAsOgcApiFeatures.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(
                PermissionView.model._meta.verbose_name,
                reverse(
                    f"{app_menu.app_label}:layer-permission-list",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dbs_permission = DBService(PublishedAsOgcApiFeatures, central_app_label)
        context["read_permission_id"] = (
            dbs_permission.get_by_object_pk(self.kwargs.get("pk"))
            .filter(codename__icontains="read")
            .get()
            .pk
        )
        context["success_url"] = reverse(
            "features:layer-permission-list", kwargs={"pk": self.kwargs.get("pk")}
        )
        return context


class GroupListView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaListView):
    model = Group
    template_name = "core/group.html"
    permission_required = PublishedAsOgcApiFeatures.perm_manage_permissions()

    def get_queryset(self):
        return Group.objects.exclude(
            permissions__codename__icontains=str(self.kwargs.get("pk"))
        )

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                PublishedAsOgcApiFeatures.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(
                PermissionView.model._meta.verbose_name,
                reverse(
                    f"{app_menu.app_label}:layer-permission-list",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dbs_permission = DBService(PublishedAsOgcApiFeatures, central_app_label)
        context["read_permission_id"] = (
            dbs_permission.get_by_object_pk(self.kwargs.get("pk"))
            .filter(codename__icontains="read")
            .get()
            .pk
        )
        context["success_url"] = reverse(
            "features:layer-permission-list", kwargs={"pk": self.kwargs.get("pk")}
        )
        return context
