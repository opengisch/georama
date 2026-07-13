from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from georama.integration.models import Custom, Raster, Vector
from georama.integration.models.datasource import Datasource
from georama.maps.models.wms_layer import WmsLayerAbstract
from georama.webgis.managers.wms_layer import WmsLayerManager
from georama.webgis.models.metadata import Metadata


class WmsLayer(WmsLayerAbstract):
    ORGANISATION_FIELD_NAME = "datasource__project__organisation"

    class Meta:
        verbose_name = _("WMS Layer")
        verbose_name_plural = _("WMS Layers")

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
