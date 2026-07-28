from adrf.mixins import get_data
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from georama.core.common.api import (
    GeoramaManagerWithPermissionsViewSet,
    GeoramaModelPermissions,
    GeoramaObjPermViewSetReadOnly,
)
from georama.core.common.menu import ActionType, Breadcrumb, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.features.api.serializers import (
    FeatureLayerObjectPermissionSerializer,
    FeatureLayerPermissionActionSerializer,
    FeatureLayerSerializer,
    FieldSerializer,
)
from georama.features.forms.feature_layer import FeatureLayerModelForm
from georama.features.forms.field import FieldFormSet
from georama.features.models import FeatureLayer, Field, Metadata
from georama.integration.models import Vector

User = get_user_model()


class ManageFeatureLayerViewSet(GeoramaManagerWithPermissionsViewSet):
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

    permissions_serializer_class = FeatureLayerObjectPermissionSerializer
    permissions_action_serializer_class = FeatureLayerPermissionActionSerializer

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
