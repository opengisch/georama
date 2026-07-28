import json

from adrf import mixins, viewsets
from adrf.mixins import get_data
from asgiref.sync import sync_to_async
from django.apps import apps
from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import router as djdb_router
from django.db.models import Exists, Min, OuterRef, Q
from django.db.models.functions import JSONObject
from django.forms import ModelForm
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from drf_spectacular.plumbing import build_mock_request as original_build_mock_request
from guardian.shortcuts import assign_perm, get_objects_for_user, remove_perm
from rest_framework import filters, renderers, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from rest_framework.response import Response

from georama.core.common.menu import ActionType, Breadcrumb, BreadcrumbAction
from georama.core.common.remote_actions import RemoteAction, get_remote_action
from georama.core.common.request import GeoramaDrfRequest
from georama.core.common.serializers import (
    GroupObjectPermissionSerializer,
    GroupPermissionBulkActionSerializer,
    UserObjectPermissionSerializer,
    UserPermissionBulkActionSerializer,
)
from georama.core.patches.adrf import pagination

User = get_user_model()


class GeoramaModelPermissions(DjangoModelPermissions):
    """A permission which also checks view permission on read endpoints."""

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": ["%(app_label)s.view_%(model_name)s"],
        "HEAD": ["%(app_label)s.view_%(model_name)s"],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


def build_mock_request(method, path, view, original_request, **kwargs):
    """we need to hook in here since the generator for schemas seem to not
    transport all attributes (DRF SPectacular), this method is configured in the
    settings py then!
    """
    request = original_build_mock_request(method, path, view, original_request, **kwargs)
    if original_request:
        request.georama_organisation = original_request.georama_organisation
    return request


class GeoramaOrganisationalMixin:
    """Mixin class to add organisational filtering to viewsets"""

    request: GeoramaDrfRequest

    def get_queryset(self):
        """
        The queryset is automatically filtered by the organisation.

        Returns:
            The filtered queryset.
        """
        qs = super().get_queryset()
        return qs.organisation_objects(self.request.georama_organisation)


class GeoramaTemplateViewSetReadOnly(
    viewsets.ReadOnlyModelViewSet,
):
    """ """

    pagination_class = pagination.LimitOffsetPagination
    renderer_classes = [
        renderers.TemplateHTMLRenderer,
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
    ]
    list_template_name: str = "core/drf/default/list.html"
    list_partial_template_name: str = "core/drf/default/partials/list.html"
    list_body_partial_template_name: str = "core/drf/default/partials/list_body.html"
    show_template_name: str = "core/drf/default/detail.html"

    def url_name(self, action_name: str, manager: bool = False) -> str:
        """Creates a qualified view name of an action. Qualified means,
        it contains the app name too.

        We are aware that DRF offers a mechanism to
        [reverse actions](https://www.django-rest-framework.org/api-guide/viewsets/#reversing-action-urls).
        However, this does not include our manager pattern, and it does not work reliably.

        Args:
            action_name: The name of the action the string should be constructed for. For
                information about actions see the
                [restframework docs](https://www.django-rest-framework.org/api-guide/routers/#simplerouter)
            manager: Switch to create the manager version of the action instead.
        Returns:
            The constructed view name.
        """
        name_parts = [self.basename]
        if manager:
            name_parts.append("manager")
        name_parts.append(action_name)
        view_name = "-".join(name_parts)
        view_name_qualified = f"{self.queryset.model._meta.app_label}:{view_name}"
        return view_name_qualified

    async def _prepare_many_context(self) -> dict:
        search_fields = getattr(self, "search_fields", [])
        context = {
            "per_page_options": settings.LIST_PAGE_SIZES,
            # this is how the filters.SearchFilter does it too
            "search_fields": search_fields,
            "search_param": filters.SearchFilter.search_param,
            "search_fields_hint": _(f"searchable fields: {', '.join(search_fields)}"),
            "ordering_param": filters.OrderingFilter.ordering_param,
            "breadcrumbs": await self.get_breadcrumbs(),
            "view": self,
            "model_name_verbose": self.queryset.model._meta.verbose_name,
            "list_partial": self.list_partial_template_name,
            "list_body_partial": self.list_body_partial_template_name,
        }
        context.update(await self.bread_crumb_action_context)
        return context

    @property
    async def bread_crumb_action_context(self):
        """
        We leve it to the baseclass here to point to a specific action if needed.

        Returns:
            Empty action context. So no button will be shown by default.
        """
        return {}

    async def _prepare_single_context(self):
        instance = await self.aget_object()
        breadcrumbs = await self.get_breadcrumbs()
        breadcrumbs[-1].view_name = self.reverse_action("list")
        breadcrumbs += [Breadcrumb(str(instance))]
        context = {
            "object": instance,
            "view": self,
            "breadcrumbs": breadcrumbs,
        }
        context.update(await self._get_model_permissions())
        return context

    async def _get_model_permissions(self) -> dict:
        """Since this is readonly, no permissions for editing
        is granted at all.

        Returns:
            The permission dict, granting no editing at all.
        """
        return {
            "can_add": False,
            "can_change": False,
            "can_delete": False,
            "can_manage_permissions": False,
        }

    @property
    def url_name_list(self):
        return self.url_name("list")

    async def alist(self, request, *args, **kwargs):
        if request.accepted_renderer.format in ["html"]:
            qs = await self.afilter_queryset(self.get_queryset())
            context = await self._prepare_many_context()
            ordering = filters.OrderingFilter()
            ordering_current_direction = ordering.get_ordering(request, qs, self) or []
            ordering_context = {}
            for o in ordering_current_direction:
                direction = "descending" if o.startswith("-") else "ascending"
                field = o.removeprefix("-")
                ordering_context[field] = {
                    "name": field,
                    "label": field.split("_")[-1],
                    "direction": direction,
                }
            # this is how the filters.OrderingFilter does it too
            for field in getattr(self, "ordering_fields", []):
                if field not in ordering_context:
                    ordering_context[field] = {
                        "name": field,
                        "label": field.split("_")[-1],
                        "direction": None,
                    }
            pqs = await self.apaginate_queryset(qs)
            context["object_list"] = pqs
            context["limit"] = self.paginator.limit
            ordering_context_list = [v for _, v in ordering_context.items()]
            ordering_context_list.sort(key=lambda d: d["name"])
            context["ordering_context"] = ordering_context_list
            context["ordering_context_json"] = json.dumps(ordering_context)
            context.update(await self._get_model_permissions())
            context.update(self.paginator.get_html_context())
            if request.META.get("HTTP_HX_REQUEST") == "true":
                return Response(context, template_name=context[request.META.get("HTTP_HX_TARGET")])
            else:
                return Response(context, template_name=self.list_template_name)
        else:
            return await super().alist(request, *args, **kwargs)

    @property
    def url_name_show(self):
        return self.url_name("ashow")

    @action(
        detail=True,
        methods=["get"],
        name="Show instance read only",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def ashow(self, request, *args, **kwargs):
        """Shows a read only representation of the detail."""
        context = await self._prepare_single_context()
        return Response(context, template_name=self.show_template_name)

    async def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.queryset.model._meta.app_label).app_menu()
        return [
            Breadcrumb(app_menu.title),
            Breadcrumb(self.queryset.model._meta.verbose_name_plural),
        ]


class GeoramaTemplateViewSet(
    GeoramaTemplateViewSetReadOnly,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    """A viewset which offers writable actions in addition to the read-only variant it
    inherits from.

    Attributes:
        form_template_name: The path of the template which is used to render the form for
            update, create actions.
        form: The form which is used to be rendered in the `form_template_name`. This
            has no default and must be set.
        delete_template_name: The path of the template which use used to render the delete
            preview. This is an intermediate step to let the user confirm the delete action.

    """

    form_template_name: str = "core/drf/default/form.html"
    form: ModelForm
    delete_template_name: str = "core/drf/default/delete_preview.html"

    def bound_remote_actions(self) -> list[RemoteAction]:
        """Gets the registered remote actions for the model of this viewset.

        In addition,
        it checks if it was a remote request (a request which came from another app via
        HTMX) and filters to have the remote actions for this app only.

        In addition, it filters the actions to the ones the requesting user has access
        to.

        Returns:
             The remote actions filtered by the before mentioned criteria.
        """
        remote_actions = get_remote_action(self.queryset.model)
        if self.request.META.get("GR-Src"):
            # call came from another app, we filter for only the fitting ones:
            remote_actions = [
                ra for ra in remote_actions if ra.name == self.request.resolver_match.app_name
            ]
        remote_actions = [
            ra
            for ra in remote_actions
            if any(self.request.user.has_perm(perm) for perm in ra.permissions)
        ]
        return remote_actions

    async def _prepare_many_context(self) -> dict:
        context = await super()._prepare_many_context()
        context.update(
            {
                "remote_actions": self.bound_remote_actions(),
            }
        )
        return context

    async def _prepare_single_context(self):
        context = await super()._prepare_single_context()
        context.update(
            {
                "remote_actions": self.bound_remote_actions(),
            }
        )
        return context

    async def _get_model_permissions(self) -> dict[str, bool]:
        """We are calculating the permissions based on the DRF permission class.

        Returns:
            The permission dict, containing the information about the users edit
            permissions on the model of this viewset.
        """
        perm_checker = GeoramaModelPermissions()
        return {
            "can_add": await self.request.user.ahas_perms(
                perm_checker.get_required_permissions("POST", self.queryset.model)
            ),
            "can_change": await self.request.user.ahas_perms(
                perm_checker.get_required_permissions("PATCH", self.queryset.model)
            ),
            "can_delete": await self.request.user.ahas_perms(
                perm_checker.get_required_permissions("DELETE", self.queryset.model)
            ),
            "can_manage_permissions": self.request.user.has_perm(
                f"{self.queryset.model._meta.app_label}.manage_object_permissions"
            ),
        }

    @property
    def url_name_retrieve(self):
        return self.url_name("detail")

    async def aretrieve(self, request: GeoramaDrfRequest, *args, **kwargs):
        """Handles the standard retrieve of a model view
        but returns a form in case of HTML format
        """
        if request.accepted_renderer.format == "html":
            context = await self._prepare_single_context()
            context["form"] = self.form(instance=context["object"])
            return Response(context, template_name=self.form_template_name)
        else:
            return await super().aretrieve(request, *args, **kwargs)

    @property
    def url_name_update(self):
        return self.url_name("aform-update")

    @action(
        detail=True,
        methods=["post"],
        name="Update instance with a form request",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def aform_update(self, request, *args, **kwargs):
        await self.aupdate(request, *args, **kwargs)
        instance = await self.aget_object()
        return redirect(reverse(self.url_name_retrieve, kwargs={"pk": instance.pk}))

    @action(
        detail=False,
        methods=["get"],
        name="Add new instance",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def aadd(self, request, *args, **kwargs):
        """Shows an empty form to create a new item or the default list."""
        context = {
            "view": self,
            "breadcrumbs": await self.get_breadcrumbs(),
        }
        context.update(await self._get_model_permissions())
        context["form"] = self.form()
        return Response(context, template_name=self.form_template_name)

    @property
    def url_name_add(self):
        return self.url_name("aadd")

    @action(
        detail=True,
        methods=["get", "post"],
        name="Delete an instance",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def adelete_confirm(self, request, *args, **kwargs):
        """Shows a confirmation dialog before data is actually deleted"""
        context = await self._prepare_single_context()
        using = djdb_router.db_for_write(self.queryset.model)
        collector = NestedObjects(using=using)
        await sync_to_async(collector.collect)([context["object"]])
        context["expected_status"] = status.HTTP_204_NO_CONTENT
        context["related_objects"] = collector.nested()
        context["protected"] = collector.protected
        return Response(context, template_name=self.delete_template_name)

    @property
    def url_name_delete_confirm(self):
        return self.url_name("adelete-confirm")

    @property
    def url_name_destroy(self):
        return self.url_name("detail")

    async def adestroy(self, request, *args, **kwargs):
        response = await super().adestroy(request, *args, **kwargs)
        if request.accepted_renderer.format == "html":
            if response.status_code == status.HTTP_204_NO_CONTENT:
                response = redirect(self.url_name_list)
            else:
                response = redirect(self.url_name_delete_confirm, self.get_object().pk)
            # we set this, so the browser can change http method to get
            # (https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Redirections#temporary_redirections)
            response.status_code = status.HTTP_303_SEE_OTHER
            return response
        else:
            return response


class GeoramaManageableMixin:
    """This mixin adds a dedicated breadcrumb action to viewsets which should offer
    a manager sidecar api. Convention of the basename of the manager is:
        `manager-<model_name>`
    So for the model Theme it would be:
    `manager-theme`
    """

    @property
    async def bread_crumb_action_context(self):
        """This adds an action button to the breadcrumbs to link to the management view,
        if the user has the permissions to look at it.

        We check if the user has the permission to see actually the button.

        Returns:
            The context with the button settings.
        """
        context = {}
        perm_checker = GeoramaModelPermissions()
        if await sync_to_async(perm_checker.has_permission)(self.request, self):
            context["breadcrumb_action"] = BreadcrumbAction(
                url=reverse(self.url_name("list", manager=True)),
                tooltip=f"{_('Switch to the management GUI of .')} {
                    self.queryset.model._meta.verbose_name
                }",
                hint=_("Manage items on this list."),
                title=_("Manage"),
                type=ActionType.LINKED,
                icon="fa fa-wrench",
            )
        return context


class GeoramaObjPermMixin:
    """This mixin ensures filtering for object permissions. The permissions
    have to be configured.

    Attributes:
        required_obj_perms: The list of permission codenames which should be checked. This
            permissions must be different from the standard model permissions
            (view, add, change, delete) of Django. Because there is a fundamental
            difference if a user can add/delete/change/view e.g a FeatureLayer-Object and
            if a user can add/delete/change/view elements on a FeatureLayer-Object.
            The first are the permissions necessary for handling things on the Georama
            internal DB and the others are the permissions to handle things in the configured
            underlying datasource.
    """

    required_obj_perms: list[str]

    async def public_or_object_permission(self, queryset):
        if self.request.user.is_superuser:
            return queryset
        if self.request.user.is_authenticated:
            qs = await sync_to_async(get_objects_for_user, thread_sensitive=True)(
                self.request.user, self.required_obj_perms, klass=queryset, any_perm=True
            ) | queryset.filter(public=True)
        else:
            qs = queryset.filter(public=True)
        return qs

    async def afilter_queryset(self, queryset):
        """Additionally to the filters applied we always filter for the
        object permissions configured on the class level.

        Returns:
            The queryset filtered for all objects by object permission the requesting user
            has combined by those which are public.
        """
        queryset = await super().afilter_queryset(queryset)
        return await self.public_or_object_permission(queryset)


class OrganisationalModelViewSet(GeoramaOrganisationalMixin, viewsets.ModelViewSet):
    """
    A DRF ViewSet which uses organisational bound tables to filter automatically for
    only organisations defined by the request.

    Attributes:
        request: The normal rest_framework.request.Request which is extended by the
            georama.core.middleware.organisation.OrganisationMiddleware with the
            georama_organisation attribute.
    """

    pass


class GeoramaObjPermViewSetReadOnly(
    GeoramaObjPermMixin,
    GeoramaManageableMixin,
    GeoramaOrganisationalMixin,
    GeoramaTemplateViewSetReadOnly,
):
    """This viewset offers a read-only variant which is filtered for object
    permissions on the configured permissions. The content is filtered based on objects
    only! Since we have objects which can be `public` we generally allow anyone to access
    the endpoints.

    Attributes:
        permission_classes: The only allowed permission class here is `AllowAny` to allow
            access to anyone.
    """

    permission_classes = [AllowAny]


class GeoramaObjPermViewSet(
    GeoramaObjPermMixin, GeoramaManageableMixin, GeoramaOrganisationalMixin, GeoramaTemplateViewSet
):
    """This viewset offers a full CRUD variant which is filtered for object
    permissions on the configured permissions. The content is filtered based on objects
    only! Since we have objects which can be `public` we generally allow anyone to access
    the endpoints. All sensible not-safe endpoints (CRUD) are checked specifically.

    Attributes:
        permission_classes: The only allowed permission class here is `AllowAny` to allow
            readonly access to anyone.
    """

    permission_classes = [AllowAny]


class GeoramaManagerViewSet(GeoramaOrganisationalMixin, GeoramaTemplateViewSet):
    """This viewset is meant to be used when permissions are based on the model itself.
    meaning the normal behaviour Django and DRF offer. It is explicitly not ment to be used
    for object permissions. It is prepared to be used as a management GUI/API for a model.

    Attributes:
        permission_classes: This view should only have one
            permission class - `GeoramaModelPermissions` this permission class is used
            to check for permissions on different places of the viewset.
    """

    permission_classes = [GeoramaModelPermissions]

    async def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.queryset.model._meta.app_label).app_menu()
        return [
            Breadcrumb(app_menu.title),
            Breadcrumb(
                self.queryset.model._meta.verbose_name_plural,
                reverse(self.url_name_list.replace("manager-", "")),
            ),
            Breadcrumb(_("Manage")),
        ]


class GeoramaManagerWithPermissionsViewSet(GeoramaManagerViewSet):
    """This viewset is meant to be used when permissions are based on the model itself.
    meaning the normal behaviour Django and DRF offer. It is explicitly not ment to be used
    for object permissions. It is prepared to be used as a management GUI/API for a model.

    Attributes:
        permission_classes: This view should only have one
            permission class - `GeoramaModelPermissions` this permission class is used
            to check for permissions on different places of the viewset.
    """

    permissions_template_name: str = "core/drf/default/permissions.html"
    permissions_list_template_name: str = "core/drf/default/includes/permissions_list_htmx.html"
    permissions_inherited_template_name: str = (
        "core/drf/default/includes/permissions_inherited_htmx.html"
    )

    user_permissions_serializer_class = UserObjectPermissionSerializer
    group_permissions_serializer_class = GroupObjectPermissionSerializer
    user_permissions_bulk_action_serializer_class = UserPermissionBulkActionSerializer
    group_permissions_bulk_action_serializer_class = GroupPermissionBulkActionSerializer

    @property
    def url_name_user_permissions(self):
        return self.url_name("user-permissions")

    @property
    def url_name_group_permissions(self):
        return self.url_name("group-permissions")

    def _permission_exist(self, perm_model, entity_id, codename, pk):
        return Exists(
            perm_model.objects.filter(
                **{entity_id: OuterRef("pk")},
                content_object_id=pk,
                permission__codename=codename,
            )
        )

    def _permission_time_created(self, perm_model, pk):
        perm_model_name = perm_model._meta.model_name
        return Min(
            f"{perm_model_name}__time_created",
            filter=Q(
                **{
                    f"{perm_model_name}__content_object_id": pk,
                    f"{perm_model_name}__permission__codename__in": list(
                        self.queryset.model.PERMISSIONS.values()
                    ),
                },
            ),
        )

    @action(detail=True, methods=["get", "post"], url_path="permissions/users")
    async def user_permissions(self, request: GeoramaDrfRequest, pk: str):
        context = await self._prepare_single_context()

        if request.method == "POST":
            action_map = self.queryset.model.ACTION_MAP

            payload_serializer = self.user_permissions_bulk_action_serializer_class(
                data=request.data
            )
            if not payload_serializer.is_valid():
                # TODO: handle html
                return Response(payload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            action_name = payload_serializer.validated_data["action"]
            users = payload_serializer.validated_data["users"]

            add, permission_names, _action_label = action_map[action_name]
            permission_action = sync_to_async(assign_perm) if add else sync_to_async(remove_perm)
            found_users = []

            # TODO: some validation ?
            async for user in User.objects.filter(id__in=users):
                found_users.append(str(user.id))
                for permission_name in permission_names:
                    full_permission = f"{self.queryset.model._meta.app_label}.{permission_name}"
                    await permission_action(full_permission, user, context["object"])

            if request.accepted_renderer.format == "html":
                target_url = reverse(self.url_name_user_permissions, kwargs={"pk": pk})
                query_string = request.GET.urlencode()
                if query_string:
                    target_url = f"{target_url}?{query_string}"
                return redirect(target_url)

            return Response(
                {
                    "detail": "Permissions assigned.",
                    "action": action_name,
                    "users": found_users,
                },
                status=status.HTTP_200_OK,
            )

        group_perm_model = self.queryset.model.group_object_permissions.rel.related_model
        user_perm_model = self.queryset.model.user_object_permissions.rel.related_model

        qs = User.objects.annotate(
            entity_permissions=JSONObject(
                **{
                    permission: self._permission_exist(user_perm_model, "user_id", codename, pk)
                    for permission, codename in self.queryset.model.PERMISSIONS.items()
                }
            ),
            inherited_permissions=JSONObject(
                **{
                    permission: self._permission_exist(
                        group_perm_model, "group__user", codename, pk
                    )
                    for permission, codename in self.queryset.model.PERMISSIONS.items()
                }
            ),
            permission_time_created=self._permission_time_created(user_perm_model, pk),
        )

        sort_by_latest = "sort_by_latest" in request.query_params
        if sort_by_latest:
            qs = qs.order_by("permission_time_created", "username")
        else:
            qs = qs.order_by("username")

        permission_filters = {
            permission: True
            for permission in self.queryset.model.PERMISSIONS
            if f"filter_{permission}" in request.query_params
        }
        qs = qs.filter(
            *(
                self._permission_exist(
                    user_perm_model, "user_id", self.queryset.model.PERMISSIONS[filter], pk
                )
                for filter in permission_filters
            )
        )

        search_param = "filter_name"
        search_term = request.query_params.get(search_param, "")

        if search_term:
            qs = qs.filter(username__icontains=search_term)

        pqs = await self.apaginate_queryset(qs)
        serializer = self.user_permissions_serializer_class(pqs, many=True)
        data = await get_data(serializer)

        if request.accepted_renderer.format == "html":
            context.update(await self._get_model_permissions())
            context["permissions_url_name"] = self.url_name_user_permissions
            context["permissions_entity_field"] = "users"
            context["available_permissions"] = self.queryset.model.PERMISSIONS.keys()
            context["search_term"] = search_term
            context["search_param"] = search_param
            context["search_fields_hint"] = _("searchable fields: user name")
            context["permission_filters"] = permission_filters
            context["sort_by_latest"] = sort_by_latest
            context["object_list"] = data
            context["limit"] = self.paginator.limit
            context.update(self.paginator.get_html_context())
            context["per_page_options"] = settings.LIST_PAGE_SIZES
            context["breadcrumbs"][-1].view_name = self.reverse_action("detail", [pk])
            context["breadcrumbs"].append(Breadcrumb("Permissions"))
            context["breadcrumbs"].append(Breadcrumb("Users"))
            context["btn_grant_access"] = _("override access")
            context["action_choices"] = list(
                self.user_permissions_bulk_action_serializer_class()
                .fields["action"]
                .choices.items()
            )

            if request.META.get("HTTP_HX_REQUEST") == "true":
                template_name = self.permissions_list_template_name
            else:
                template_name = self.permissions_template_name

            return Response(context, template_name=template_name)
        else:
            return await self.get_apaginated_response(data)

    @action(detail=True, methods=["get", "post"], url_path="permissions/groups")
    async def group_permissions(self, request: GeoramaDrfRequest, pk: str):
        context = await self._prepare_single_context()

        if request.method == "POST":
            action_map = self.queryset.model.ACTION_MAP

            payload_serializer = self.group_permissions_bulk_action_serializer_class(
                data=request.data
            )
            if not payload_serializer.is_valid():
                raise Exception(payload_serializer.errors)
                # TODO: handle html
                return Response(payload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            action_name = payload_serializer.validated_data["action"]
            groups = payload_serializer.validated_data["groups"]

            add, permission_names, _action_label = action_map[action_name]
            permission_action = sync_to_async(assign_perm) if add else sync_to_async(remove_perm)
            found_groups = []

            # TODO: some validation ?
            async for group in Group.objects.filter(id__in=groups):
                found_groups.append(str(group.id))
                for permission_name in permission_names:
                    full_permission = f"{self.queryset.model._meta.app_label}.{permission_name}"
                    await permission_action(full_permission, group, context["object"])

            if request.accepted_renderer.format == "html":
                target_url = reverse(self.url_name_group_permissions, kwargs={"pk": pk})
                query_string = request.GET.urlencode()
                if query_string:
                    target_url = f"{target_url}?{query_string}"
                return redirect(target_url)

            return Response(
                {
                    "detail": "Permissions assigned.",
                    "action": action_name,
                    "groups": found_groups,
                },
                status=status.HTTP_200_OK,
            )

        group_perm_model = self.queryset.model.group_object_permissions.rel.related_model

        qs = Group.objects.annotate(
            entity_permissions=JSONObject(
                **{
                    permission: self._permission_exist(group_perm_model, "group_id", codename, pk)
                    for permission, codename in self.queryset.model.PERMISSIONS.items()
                }
            ),
            permission_time_created=self._permission_time_created(group_perm_model, pk),
        )

        sort_by_latest = "sort_by_latest" in request.query_params
        if sort_by_latest:
            qs = qs.order_by("permission_time_created", "name")
        else:
            qs = qs.order_by("name")

        permission_filters = {
            permission: True
            for permission in self.queryset.model.PERMISSIONS
            if f"filter_{permission}" in request.query_params
        }
        qs = qs.filter(
            *(
                self._permission_exist(
                    group_perm_model, "group_id", self.queryset.model.PERMISSIONS[filter], pk
                )
                for filter in permission_filters
            )
        )

        search_param = "filter_name"
        search_term = request.query_params.get(search_param, "")

        if search_term:
            qs = qs.filter(name__icontains=search_term)

        pqs = await self.apaginate_queryset(qs)
        serializer = self.group_permissions_serializer_class(pqs, many=True)
        data = await get_data(serializer)

        if request.accepted_renderer.format == "html":
            context.update(await self._get_model_permissions())
            context["permissions_url_name"] = self.url_name_group_permissions
            context["permissions_entity_field"] = "groups"
            context["available_permissions"] = self.queryset.model.PERMISSIONS.keys()
            context["search_term"] = search_term
            context["search_param"] = search_param
            context["search_fields_hint"] = _("searchable fields: group name")
            context["permission_filters"] = permission_filters
            context["sort_by_latest"] = sort_by_latest
            context["object_list"] = data
            context["limit"] = self.paginator.limit
            context.update(self.paginator.get_html_context())
            context["per_page_options"] = settings.LIST_PAGE_SIZES
            context["breadcrumbs"][-1].view_name = self.reverse_action("detail", [pk])
            context["breadcrumbs"].append(Breadcrumb("Permissions"))
            context["breadcrumbs"].append(Breadcrumb("Groups"))
            context["btn_grant_access"] = _("grant access")
            context["action_choices"] = list(
                self.group_permissions_bulk_action_serializer_class()
                .fields["action"]
                .choices.items()
            )
            if request.META.get("HTTP_HX_REQUEST") == "true":
                template_name = self.permissions_list_template_name
            else:
                template_name = self.permissions_template_name

            return Response(context, template_name=template_name)
        else:
            return await self.get_apaginated_response(data)
