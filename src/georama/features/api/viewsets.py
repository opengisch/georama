from adrf.mixins import get_data
from asgiref.sync import sync_to_async
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, Min, Q, Value
from django.db.models.functions import Coalesce
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from guardian.shortcuts import assign_perm, remove_perm
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from georama.core.common.api import (
    GeoramaManagerViewSet,
    GeoramaModelPermissions,
    GeoramaObjPermViewSetReadOnly,
)
from georama.core.common.menu import ActionType, Breadcrumb, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.features.api.serializers import (
    FeatureLayerSerializer,
    FeatureLayerUserObjectPermissionSerializer,
    FeatureLayerUserPermissionBulkActionSerializer,
    FieldSerializer,
)
from georama.features.forms.feature_layer import FeatureLayerModelForm
from georama.features.forms.field import FieldFormSet
from georama.features.models import FeatureLayer, Field, Metadata
from georama.integration.models import Vector

User = get_user_model()


class ManageFeatureLayerViewSet(GeoramaManagerViewSet):
    queryset = FeatureLayer.objects.all()
    serializer_class = FeatureLayerSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []
    form = FeatureLayerModelForm

    show_template_name = "features/drf/feature_layer/detail.html"
    form_template_name: str = "features/drf/feature_layer/form.html"

    @property
    async def bread_crumb_action_context(self):
        """Prepares the breadcrumb action to add a theme.

        Returns:
            The context with an action to add a new theme in case the user has add-permission
            on the theme model and is permitted to view projects.
        """
        context = {}
        perm_checker = GeoramaModelPermissions()
        # post is the DRF method which is used for add/create a new object
        local_perms = perm_checker.get_required_permissions("POST", self.queryset.model)
        # we also check if the remote data can be used (view)
        remote_perms = perm_checker.get_required_permissions("GET", Vector)
        if all(
            [
                await self.request.user.ahas_perms(local_perms),
                await self.request.user.ahas_perms(remote_perms),
            ]
        ):
            context["breadcrumb_action"] = BreadcrumbAction(
                url=reverse("integration:manager-vector-list"),
                tooltip=_("Publish a Vector Datasource as FeatureLayer"),
                hint=_("Select a Vector Datasource to publish it as a new FeatureLayer"),
                title=_("FeatureLayer"),
                type=ActionType.EMBEDDED,
                icon="fa fa-circle-plus",
            )
        return context

    @action(detail=False, methods=["post"], url_path="publish_from_vector")
    async def publish_from_vector(self, request: GeoramaDrfRequest, *args, **kwargs):
        qs = Vector.objects.organisation_objects(request.georama_organisation)
        vector = await qs.aget(id=request.data["pk"])
        md = Metadata(title=vector.name)
        await md.asave()
        fl = FeatureLayer(datasource=vector, metadata=md)
        await sync_to_async(fl.save)()
        return redirect(reverse(self.url_name_list))

    @property
    def url_name_fields(self):
        return self.url_name("fields")

    @property
    def url_name_permissions_users(self):
        return self.url_name("permissions-users")

    @action(detail=True, methods=["get", "post"], url_path="permissions/users")
    async def permissions_users(self, request: GeoramaDrfRequest, pk: str):
        try:
            layer = await self.get_queryset().aget(pk=pk)
        except FeatureLayer.DoesNotExist as exc:
            raise Http404 from exc

        if request.method == "POST":
            action_map = {
                "grant": (
                    sync_to_async(assign_perm),
                    ["features.view_objects_on_published_layer"],
                ),
                "allow_create": (
                    sync_to_async(assign_perm),
                    [
                        "features.view_objects_on_published_layer",
                        "features.create_objects_on_published_layer",
                    ],
                ),
                "allow_update": (
                    sync_to_async(assign_perm),
                    [
                        "features.view_objects_on_published_layer",
                        "features.update_objects_on_published_layer",
                    ],
                ),
                "allow_delete": (
                    sync_to_async(assign_perm),
                    [
                        "features.view_objects_on_published_layer",
                        "features.delete_objects_on_published_layer",
                    ],
                ),
                "prevent_create": (
                    sync_to_async(remove_perm),
                    ["features.create_objects_on_published_layer"],
                ),
                "prevent_update": (
                    sync_to_async(remove_perm),
                    ["features.update_objects_on_published_layer"],
                ),
                "prevent_delete": (
                    sync_to_async(remove_perm),
                    ["features.delete_objects_on_published_layer"],
                ),
                "revoke": (
                    sync_to_async(remove_perm),
                    [
                        "features.view_objects_on_published_layer",
                        "features.create_objects_on_published_layer",
                        "features.delete_objects_on_published_layer",
                        "features.update_objects_on_published_layer",
                    ],
                ),
            }

            payload_serializer = FeatureLayerUserPermissionBulkActionSerializer(data=request.data)
            if not payload_serializer.is_valid():
                # TODO: handle html
                # if request.accepted_renderer.format == "html":
                #     return redirect(
                #         reverse(self.url_name_permissions_users, kwargs={"pk": pk})
                #     )
                return Response(payload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            action_name = payload_serializer.validated_data["action"]
            users = payload_serializer.validated_data["users"]

            permission_action, permission_names = action_map[action_name]
            found_users = []

            # TODO: some validation ?
            async for user in User.objects.filter(id__in=users):
                found_users.append(str(user.id))
                for permission_name in permission_names:
                    await permission_action(permission_name, user, layer)

            if request.accepted_renderer.format == "html":
                return redirect(reverse(self.url_name_permissions_users, kwargs={"pk": pk}))

            return Response(
                {
                    "detail": "Permissions assigned.",
                    "action": action_name,
                    "users": found_users,
                },
                status=status.HTTP_200_OK,
            )

        qs = User.objects.annotate(
            permission_codenames=Coalesce(
                ArrayAgg(
                    "featurelayeruserobjectpermission__permission__codename",
                    filter=Q(
                        featurelayeruserobjectpermission__content_object_id=pk,
                        featurelayeruserobjectpermission__permission__codename__in=[
                            "view_objects_on_published_layer",
                            "create_objects_on_published_layer",
                            "delete_objects_on_published_layer",
                            "update_objects_on_published_layer",
                        ],
                    ),
                ),
                Value([], output_field=ArrayField(CharField())),
            ),
            permission_time_created=Min(
                "featurelayeruserobjectpermission__time_created",
                filter=Q(
                    featurelayeruserobjectpermission__content_object_id=pk,
                    featurelayeruserobjectpermission__permission__codename__in=[
                        "view_objects_on_published_layer",
                        "create_objects_on_published_layer",
                        "delete_objects_on_published_layer",
                        "update_objects_on_published_layer",
                    ],
                ),
            ),
        ).order_by("username")

        search_param = "username"
        search_term = request.query_params.get("username", "")

        if search_term:
            qs = qs.filter(username__icontains=search_term)

        # TODO: improve performance by collecting the codenames in a set instead of a list

        pqs = await self.apaginate_queryset(qs)
        serializer = FeatureLayerUserObjectPermissionSerializer(pqs, many=True)
        data = await get_data(serializer)

        if request.accepted_renderer.format == "html":
            context = await self._prepare_single_context()
            context.update(await self._get_model_permissions())
            context["search_term"] = search_term
            context["search_param"] = search_param
            context["search_fields_hint"] = _("searchable fields: username")
            context["object_list"] = data
            context["limit"] = self.paginator.limit
            context.update(self.paginator.get_html_context())
            context["per_page_options"] = settings.LIST_PAGE_SIZES
            context["breadcrumbs"][-1].view_name = self.reverse_action("detail", [pk])
            context["breadcrumbs"].append(Breadcrumb("Permissions"))
            context["breadcrumbs"].append(Breadcrumb("Users"))
            context["action_choices"] = list(
                FeatureLayerUserPermissionBulkActionSerializer().fields["action"].choices.items()
            )
            return Response(
                context,
                template_name="features/drf/feature_layer/permissions_users.html",
            )
        else:
            return await self.get_apaginated_response(data)

    @action(detail=True, methods=["get", "post"])
    async def fields(self, request: GeoramaDrfRequest, pk: str):
        context = await self._prepare_single_context()
        layer = context["object"]
        if request.POST:
            if request.content_type == "application/json":
                serializer = FieldSerializer(data=request.data, many=True)
                if serializer.is_valid():
                    await serializer.asave()
            else:
                # Formset-Data (application/x-www-form-urlencoded or multipart/form-data)
                formset = FieldFormSet(request.POST, request.FILES)
                if await sync_to_async(formset.is_valid)():
                    await sync_to_async(formset.save)()

        if request.accepted_renderer.format in ["html"]:
            context = await self._prepare_single_context()
            fs = FieldFormSet(queryset=Field.objects.filter(feature_layer=layer))
            context["form"] = fs
            context["breadcrumbs"][-1].view_name = reverse(
                self.url_name_show, kwargs={"pk": layer.pk}
            )

            context["breadcrumbs"].append(Breadcrumb("Fields"))
            return Response(context, template_name="features/drf/field/form.html")
        else:
            fields = layer.fields.all()
            serializer = FieldSerializer(fields, many=True)
            data = await get_data(serializer)
            return Response(data, status=status.HTTP_200_OK)


class FeatureLayerViewSet(GeoramaObjPermViewSetReadOnly):
    queryset = FeatureLayer.objects.all()
    serializer_class = FeatureLayerSerializer
    required_obj_perms = [
        "features.view_objects_on_published_layer",
        "features.create_objects_on_published_layer",
        "features.delete_objects_on_published_layer",
        "features.update_objects_on_published_layer",
    ]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []
