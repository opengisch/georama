from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, renderers, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from georama.core.common.api import (
    GeoramaManagerWithPermissionsViewSet,
    GeoramaModelPermissions,
    GeoramaObjPermViewSetReadOnly,
)
from georama.core.common.menu import ActionType, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.integration.models import Datasource
from georama.maps.adapter.qsl import generate_preview_image
from georama.maps.api.serializers import (
    PreviewGeneratorBulkResult,
    PreviewGeneratorInput,
    PreviewGeneratorResult,
    PublishFromDatasourceInput,
    WmsLayerObjectPermissionSerializer,
    WmsLayerPermissionActionSerializer,
    WmsLayerSerializer,
)
from georama.maps.forms.wms_layer import WmsLayerModelForm
from georama.maps.models import Metadata, WmsLayer


class ManageWmsLayerViewSet(GeoramaManagerWithPermissionsViewSet):
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
    show_template_name = "maps/drf/wms_layer/detail.html"

    permissions_serializer_class = WmsLayerObjectPermissionSerializer
    permissions_action_serializer_class = WmsLayerPermissionActionSerializer

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

    @extend_schema(
        description="Publishes a layer from a datasource, meaning, "
        "it creates a new layer and corresponding metadata.",
        request=PublishFromDatasourceInput,
    )
    @action(detail=False, methods=["post"], url_path="publish_from_datasource")
    async def publish_from_datasource(self, request: GeoramaDrfRequest, *args, **kwargs):
        perms = await self._get_model_permissions()
        if perms["can_add"]:
            pfdi = PublishFromDatasourceInput(data=request.data)
            pfdi.is_valid()
            qs = Datasource.objects.organisation_objects(request.georama_organisation)
            ds: Datasource = await qs.aget(id=pfdi.validated_data["pk"])
            md = Metadata(title=ds.name)
            await md.asave()
            fl = WmsLayer(datasource=ds, metadata=md, extent=ds.bbox, extent_wgs84=ds.bbox_wgs84)
            if pfdi.validated_data["create_preview"]:
                image: bytes = await generate_preview_image(fl)
                fl.preview = image
            await fl.asave()
            return redirect(reverse(self.url_name_list))
        else:
            raise PermissionDenied()

    def url_name_generate_preview_image(self):
        return self.url_name("generate_preview_image")

    @extend_schema(
        responses={201: PreviewGeneratorResult},
        methods=["POST"],
        description="Generates preview image for the layer.",
    )
    @action(detail=True, methods=["post"], url_name="generate_preview_image")
    async def generate_preview_image(self, request: GeoramaDrfRequest, *args, **kwargs):
        perms = await self._get_model_permissions()
        if perms["can_change"]:
            wms_layer: WmsLayer = await self.aget_object()
            image: bytes = await generate_preview_image(wms_layer)
            wms_layer.preview = image
            await wms_layer.asave()
            if request.accepted_renderer.format == "html":
                return Response(
                    data={"item": wms_layer},
                    template_name="maps/drf/wms_layer/partials/preview.html",
                    status=status.HTTP_200_OK,
                )
            else:
                data = PreviewGeneratorResult({"layer_id": wms_layer.id})
                return Response(data, status=status.HTTP_201_CREATED)
        else:
            raise PermissionDenied()

    def url_name_generate_preview_image_bulk(self):
        return self.url_name("generate_preview_image_bulk")

    @extend_schema(
        responses={201: PreviewGeneratorBulkResult},
        request=PreviewGeneratorInput,
        description="Generates preview images for multiple layers in a single request.",
    )
    @action(
        detail=False,
        methods=["post"],
        url_name="generate_preview_image_bulk",
        renderer_classes=[renderers.JSONRenderer, renderers.BrowsableAPIRenderer],
    )
    async def generate_preview_image_bulk(self, request: GeoramaDrfRequest, *args, **kwargs):
        perms = await self._get_model_permissions()
        if perms["can_change"]:
            pgi = PreviewGeneratorInput(data=request.data)
            pgi.is_valid()
            if not pgi.validated_data["layer_ids"]:
                return Response(
                    {"error": "Provide product_ids in your request body."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            results: list[dict] = []
            async for layer in self.get_queryset().filter(id__in=pgi.validated_data["layer_ids"]):
                image: bytes = await generate_preview_image(layer)
                layer.preview = image
                await layer.asave()
                results.append({"layer_id": layer.id})

            data = PreviewGeneratorBulkResult({"results": results}).data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            raise PermissionDenied()


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
    show_template_name = "maps/drf/wms_layer/detail.html"
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []
