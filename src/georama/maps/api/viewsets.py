from asgiref.sync import sync_to_async
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from georama.core.common.api import (
    GeoramaManagerViewSet,
    GeoramaModelPermissions,
    GeoramaObjPermViewSetReadOnly,
)
from georama.core.common.menu import ActionType, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.integration.models import Datasource
from georama.maps.adapter.qsl import generate_preview_image
from georama.maps.api.serializers import WmsLayerSerializer
from georama.maps.forms.wms_layer import WmsLayerModelForm
from georama.maps.models import Metadata, WmsLayer


class ManageWmsLayerViewSet(GeoramaManagerViewSet):
    queryset = WmsLayer.objects.all()
    serializer_class = WmsLayerSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []
    form = WmsLayerModelForm
    list_body_partial_template_name = "maps/drf/wms_layer/partials/list_body.html"

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
        remote_perms = perm_checker.get_required_permissions("GET", Datasource)
        if all(
            [
                await self.request.user.ahas_perms(local_perms),
                await self.request.user.ahas_perms(remote_perms),
            ]
        ):
            context["breadcrumb_action"] = BreadcrumbAction(
                url=reverse("integration:manager-datasource-list"),
                tooltip=_("Publish a Datasource as WmsLayer"),
                hint=_("Select a Datasource to publish it as a new WmsLayer"),
                title=_("WmsLayer"),
                type=ActionType.EMBEDDED,
                icon="fa fa-circle-plus",
            )
        return context

    @action(detail=False, methods=["post"], url_path="publish_from_datasource")
    async def publish_from_datasource(self, request: GeoramaDrfRequest, *args, **kwargs):
        qs = Datasource.objects.organisation_objects(request.georama_organisation)
        ds = await qs.aget(id=request.data["pk"])
        md = Metadata(title=ds.name)
        await md.asave()
        fl = WmsLayer(datasource=ds, metadata=md)
        await sync_to_async(fl.save)()
        return redirect(reverse(self.url_name_list))

    def url_name_generate_preview_image(self):
        return self.url_name("generate_preview_image")

    @action(detail=True, methods=["post"], url_name="generate_preview_image")
    async def generate_preview_image(self, request: GeoramaDrfRequest, *args, **kwargs):
        wms_layer: WmsLayer = await self.aget_object()
        image: bytes = await generate_preview_image(wms_layer)
        wms_layer.preview = image
        await wms_layer.asave()
        return Response(
            data={"item": wms_layer},
            template_name="maps/drf/wms_layer/partials/preview.html",
            status=status.HTTP_200_OK,
        )


class WmsLayerViewSet(GeoramaObjPermViewSetReadOnly):
    queryset = WmsLayer.objects.all()
    serializer_class = WmsLayerSerializer
    required_obj_perms = [
        "maps.view_published_wms_layer",
    ]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    list_body_partial_template_name: str = "maps/drf/wms_layer/partials/list_body.html"
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []
