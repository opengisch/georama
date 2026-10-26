from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from georama.integration.models import Custom, Raster, Vector
from georama.integration.models.datasource import Datasource
from georama.maps.models.wms_layer import WmsLayerAbstract
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerSettings as GGLayerSettings,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import MetaData as GGMetadata
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import WmsLayer as GGWmsLayer
from georama.webgis.managers.wms_layer import WmsLayerManager
from georama.webgis.models.metadata import Metadata


class WmsLayer(WmsLayerAbstract):
    ORGANISATION_FIELD_NAME = "datasource__project__organisation"

    class Meta:
        verbose_name = _("WMS Layer")
        verbose_name_plural = _("WMS Layers")
        permissions = [
            # permissions of WMS layers bound to themes are handled by the theme permission
            # automatically, so they don't need to be managed
            # ("manage_object_permissions", "Can manage object permissions"),
            # permission which is used for the object permission evaluation on the published themes
            ("view_published_layer", "Can view published layer"),
        ]

    datasource = models.ForeignKey(
        Datasource,
        related_name="webgis_wms_layers",
        on_delete=models.CASCADE,
    )

    metadata = models.OneToOneField(
        Metadata,
        related_name="webgis_wms_layers",
        on_delete=models.CASCADE,
    )
    theme = models.ForeignKey(
        "Theme",
        related_name="wms_layers",
        on_delete=models.CASCADE,
    )

    objects = WmsLayerManager()

    @property
    def get_metadata(self) -> Metadata:
        return self.metadata

    @property
    def get_datasource(self) -> Datasource:
        return self.datasource

    @property
    def get_raster_datasource(self) -> Raster:
        return self.datasource.raster

    @property
    def get_vector_datasource(self) -> Vector:
        return self.datasource.vector

    @property
    def get_custom_datasource(self) -> Custom:
        return self.datasource.custom

    def get_absolute_url(self):
        return reverse(f"{self._meta.app_label}:layer-detail", kwargs={"pk": self.pk})

    @property
    def as_gg_wms_layer(self):
        from georama.maps.services.wfs_2_0_0 import WfsOperation

        return GGWmsLayer(
            id=WfsOperation.encode_layer_name(self.identifier),
            name=WfsOperation.encode_layer_name(self.identifier),
            metadata=GGMetadata(legend=True, is_legend_expanded=True),
            type="WMS",
            layers=WfsOperation.encode_layer_name(self.identifier),
            image_type="image/png",
            min_resolution_hint=self.min_resolution_hint,
            max_resolution_hint=self.max_resolution_hint,
            child_layers=[
                GGLayerSettings(
                    # GeoGirafe uses the child layer name as WFS feature type name
                    name=WfsOperation.encode_layer_name(self.identifier),
                    min_resolution_hint=self.min_resolution_hint,
                    max_resolution_hint=self.max_resolution_hint,
                    queryable=self.is_queryable,
                )
            ],
            ogc_server=settings.WEBGIS_OGC_SERVER_NAME,
            dimensions=None,
            editable=False,
            style="default",
            time=None,
            path=None,
        )
