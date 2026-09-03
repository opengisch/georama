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
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    MetaData as GGMetadata,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    WmsLayer as GGWmsLayer,
)
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
        return GGWmsLayer(
            id=self.identifier,
            name=self.metadata.title,
            metadata=GGMetadata(legend=True, isLegendExpanded=True),
            type="WMS",
            layers=self.identifier,
            imageType="image/png",
            minResolutionHint=self.min_resolution_hint,
            maxResolutionHint=self.max_resolution_hint,
            childLayers=[
                GGLayerSettings(
                    name=self.metadata.title,
                    minResolutionHint=self.min_resolution_hint,
                    maxResolutionHint=self.max_resolution_hint,
                    queryable=bool(self.is_queryable),
                )
            ],
            ogcServer=settings.WEBGIS_OGC_SERVER_NAME,
            dimensions=None,
            editable=False,
            style="default",
            time=None,
            path=None,
        )
