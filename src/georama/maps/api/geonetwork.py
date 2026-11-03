from collections.abc import Awaitable, Callable

from asgiref.sync import sync_to_async
from django.contrib import messages
from django.utils.translation import gettext as _
from drf_spectacular.utils import extend_schema
from rest_framework import renderers, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from georama.core.common.request import GeoramaDrfRequest
from georama.maps.adapter.geonetwork import (
    PROTOCOL_WFS,
    PROTOCOL_WMS,
    OnlineResource,
    RecordContent,
    delete_record,
    fetch_record_state,
    push_record,
    sync_record_visibility,
)
from georama.maps.exception.geonetwork import GeoNetworkError
from georama.maps.models.wms_layer import WmsLayerAbstract
from georama.maps.services.wfs_2_0_0 import WfsOperation


def wms_layer_online_resources(layer: WmsLayerAbstract, url: str) -> list[OnlineResource]:
    """The WMS and WFS endpoints of a layer, named as in the capabilities.

    Args:
        layer: The layer, ORM access is allowed.
        url: Absolute url of the OGC endpoint the layer is served by.

    Returns:
        WMS always, WFS only for queryable layers (same rule as WFS GetMetadata).
    """
    online_resources = [
        OnlineResource(
            url=url, protocol=PROTOCOL_WMS, name=layer.identifier, description="WMS 1.3.0"
        )
    ]
    if layer.is_queryable:
        online_resources.append(
            OnlineResource(
                url=url,
                protocol=PROTOCOL_WFS,
                name=f"{WfsOperation.own_namespace}:"
                f"{WfsOperation.encode_layer_name(layer.identifier)}",
                description="WFS 2.0.0",
            )
        )
    return online_resources


async def no_operation(item):
    pass


class GeoNetworkRecordActionsMixin:
    """POC: Actions to manage the GeoNetwork records of a published item from its list.

    Mixed into the manager viewsets of items which have a `metadata` and a `public`
    field (WmsLayer, FeatureLayer, Theme). Every action answers with the same partial,
    it shows the state of the record and the buttons fitting it, so htmx swaps it in
    place. The list loads the state per item with one request each, the browser runs
    them in parallel. The `public` switch of the item is mirrored to existing records on
    update.

    The viewset provides the records of an item with `catalogue_records`. The first one
    is the record of the item itself and defines the state shown in the list.

    The planned metadata app replaces this mixin.
    """

    geonetwork_record_template_name = "maps/drf/geonetwork/record.html"

    def url_name_geonetwork_record(self):
        return self.url_name("geonetwork_record")

    def url_name_push_metadata_to_geonetwork(self):
        return self.url_name("push_metadata_to_geonetwork")

    def url_name_delete_metadata_from_geonetwork(self):
        return self.url_name("delete_metadata_from_geonetwork")

    def catalogue_records(self, item) -> list[RecordContent]:
        """The records the item forwards to GeoNetwork, with absolute urls of the
        current request.

        Args:
            item: The published item, ORM access is allowed (called in a sync context).

        Returns:
            The record of the item first, followed by records of its parts if any.
        """
        raise NotImplementedError()

    async def _catalogue_records(self, item) -> list[RecordContent]:
        return await sync_to_async(self.catalogue_records)(item)

    async def _push_records(self, item):
        for record in await self._catalogue_records(item):
            await push_record(record.metadata, item.public, record.online_resources)

    async def _delete_records(self, item):
        for record in await self._catalogue_records(item):
            await delete_record(str(record.metadata.id))

    async def perform_aupdate(self, serializer):
        """Saves the item, a changed `public` publishes or unpublishes its records.

        A failing GeoNetwork does not fail the update, it is reported as message.
        """
        was_public = serializer.instance.public
        await super().perform_aupdate(serializer)
        item = serializer.instance
        if item.public == was_public:
            return
        try:
            for record in await self._catalogue_records(item):
                await sync_record_visibility(str(record.metadata.id), item.public)
        except GeoNetworkError as e:
            messages.warning(
                self.request,
                _("The visibility of the GeoNetwork record was not changed: {error}").format(
                    error=e
                ),
            )

    async def _geonetwork_record_response(
        self, operation: Callable[[object], Awaitable]
    ) -> Response:
        """Executes the operation on the item and renders the resulting record state.

        Errors of GeoNetwork are rendered into the partial instead of failing the
        request, so the list stays usable.

        Args:
            operation: Async callable which gets the item.

        Returns:
            The rendered partial.
        """
        perms = await self._get_model_permissions()
        if not perms["can_change"]:
            raise PermissionDenied()
        item = await self.get_queryset().select_related("metadata").aget(pk=self.kwargs["pk"])
        context = {"item": item, "view": self, "record": None, "error": None}
        try:
            await operation(item)
            context["record"] = await fetch_record_state(str(item.metadata.id))
        except GeoNetworkError as e:
            context["error"] = str(e)
        return Response(
            context, template_name=self.geonetwork_record_template_name, status=status.HTTP_200_OK
        )

    @extend_schema(description="POC: Renders the state of the GeoNetwork record of the item.")
    @action(
        detail=True,
        methods=["get"],
        url_name="geonetwork_record",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def geonetwork_record(self, request: GeoramaDrfRequest, *args, **kwargs):
        return await self._geonetwork_record_response(no_operation)

    @extend_schema(description="POC: Pushes the metadata of the item as ISO 19139 records.")
    @action(
        detail=True,
        methods=["post"],
        url_name="push_metadata_to_geonetwork",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def push_metadata_to_geonetwork(self, request: GeoramaDrfRequest, *args, **kwargs):
        return await self._geonetwork_record_response(self._push_records)

    @extend_schema(description="POC: Deletes the GeoNetwork records of the item.")
    @action(
        detail=True,
        methods=["post"],
        url_name="delete_metadata_from_geonetwork",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def delete_metadata_from_geonetwork(self, request: GeoramaDrfRequest, *args, **kwargs):
        return await self._geonetwork_record_response(self._delete_records)
