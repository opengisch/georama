import uuid
from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.qgis import WmtsSource
from treebeard.mp_tree import MP_Node
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.entities.models import PermissionInterface, PublishedAs
from georama.data_integration.models import (
    CustomDataSet,
    Mandant,
    Project,
    RasterDataSet,
    VectorDataSet,
)
from georama.maps.models import PublishedAsWmsAbstract
from georama.webgis.interfaces.geomapfish import ThemesJson
from georama.webgis.interfaces.geomapfish.themes_json_2_8 import dataclasses
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    Dimensions,
    LayerGroup,
    LayerSettings,
    MetaData,
    Theme,
    WmsLayer,
    WmtsLayer,
)


class Interface(models.Model):

    """
    Model that matches a configuration with a interface configuration (desktop, mobile, api, ...)
    """

    name = models.CharField()
    description = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name = _("Interface")
        verbose_name_plural = _("Interfaces")

    def __str__(self):
        return f"{self.name}"


class PublishedAsTheme(PublishedAs):
    """
    Top item of layer tree organization
    """

    project = models.ForeignKey(
        Project,
        related_name="published_as_geogirafe_themes",
        related_query_name="published_as_geogirafe_theme",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    themes_json_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    published_as_type = "geogirafe_theme"
    metadata = models.JSONField()
    icon = models.CharField(blank=True, null=True)
    ordering = models.IntegerField()

    @property
    def readable_identifier(self) -> str:
        return f"{self.name}.{self.name}.{self.identifier}"

    class Meta:
        ordering = ["ordering"]
        verbose_name = _("Theme")
        verbose_name_plural = _("Themes")

    def __str__(self):
        return f"{self.name}"

    def as_dataclass(self) -> Theme:
        config = ParserConfig(fail_on_unknown_properties=False)
        return Theme(
            name=self.name,
            id=str(self.themes_json_uuid),
            icon=self.icon,
            metadata=DictDecoder(config).decode(self.metadata, MetaData),
        )

    @property
    def permissions(self) -> List[PermissionInterface]:
        if self.public:
            return []
        else:
            return self.read_permissions

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name is None:
            # TODO: maybe we want this to be configurable?
            self.name = self.project.name
        if self.title is None:
            self.title = self.project.title
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


class LayerGroupMp(MP_Node):
    """
    Recursive model from django-treebeard to handle children-parent relationships
    """

    themes_json_uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=1000, null=True, default=None, blank=True)
    theme = models.ForeignKey(
        PublishedAsTheme,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="tree_elements",
        related_query_name="tree_element",
        on_delete=models.CASCADE,
    )
    # TODO: add metadata ManyToManyField
    metadata = models.JSONField(default=None, null=True)
    mixed = models.BooleanField(default=None, null=True)
    ogc_server = models.CharField(max_length=2048, default=None, null=True)
    dimensions = models.JSONField(default=None, null=True)
    node_order_by = ["name"]

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    def __str__(self):
        return f"{_('Group')}: {self.name}"

    def as_dataclass(self) -> LayerGroup:
        config = ParserConfig(fail_on_unknown_properties=False)
        metadata = None
        if self.metadata:
            metadata = DictDecoder(config).decode(self.metadata, MetaData)
        dimensions = None
        if self.dimensions:
            dimensions = DictDecoder(config).decode(self.dimensions, Dimensions)
        return LayerGroup(
            id=str(self.themes_json_uuid),
            name=self.name,
            metadata=metadata,
            dimensions=dimensions,
            mixed=self.mixed,
            ogcServer=self.ogc_server,
        )


class Layer(PublishedAs):
    """
    Base model for geographic Layer
    """

    themes_json_uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    metadata = models.JSONField(default=None, null=True, blank=True)
    dimensions = models.JSONField(default=None, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class PublishedAsLayerWms(Layer, PublishedAsWmsAbstract):
    """
    Layer extension for WMS layer
    """

    published_as_type = "geogirafe_wms_layer"
    # TODO: This means we currently can add a layer only once into the tree. It is not allowed
    #       in two different groups. Is that what we want?
    layer_group = models.OneToOneField(
        LayerGroupMp,
        related_name="wms_datasets",
        related_query_name="wms_dataset",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    raster_dataset = models.ForeignKey(
        RasterDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms_webgis",
        related_query_name="published_ogc_wms_webgis",
        on_delete=models.CASCADE,
        blank=True,
    )
    vector_dataset = models.ForeignKey(
        VectorDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms_webgis",
        related_query_name="published_ogc_wms_webgis",
        on_delete=models.CASCADE,
        blank=True,
    )
    custom_dataset = models.ForeignKey(
        CustomDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms_webgis",
        related_query_name="published_ogc_wms_webgis",
        on_delete=models.CASCADE,
        blank=True,
    )
    ogc_server = models.CharField(null=True)
    min_resolution_hint = models.FloatField(default=0.0)
    max_resolution_hint = models.FloatField(default=999999999.0)
    queryable = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        verbose_name = f'WMS {_("Layer")}'
        verbose_name_plural = f'WMS {_("Layers")}'

    def __str__(self):
        return f"{self.name}"

    @property
    def get_raster_dataset(self) -> RasterDataSet:
        return self.raster_dataset

    @property
    def get_vector_dataset(self) -> VectorDataSet:
        return self.vector_dataset

    @property
    def get_custom_dataset(self) -> CustomDataSet:
        return self.custom_dataset

    def as_dataclass(self, geogirafe_config: ThemesJson) -> WmsLayer:
        config = ParserConfig(
            fail_on_unknown_properties=False, fail_on_unknown_attributes=False
        )
        metadata = None
        if self.metadata:
            metadata = DictDecoder(config).decode(self.metadata, MetaData)
        dimensions = None
        if self.dimensions:
            dimensions = DictDecoder(config).decode(self.dimensions, Dimensions)
        return WmsLayer(
            id=str(self.themes_json_uuid),
            name=self.name,
            # TODO: Fix layers, it has to written to the datasource
            layers=self.name,
            type="WMS",
            imageType=geogirafe_config.get_ogc_server_by_name(self.ogc_server).imageType,
            metadata=metadata,
            # TODO: Fix that, its not stored correctly
            style="default",
            # TODO: fix that
            dimensions=dimensions,
            # TODO: Fix that, it does not seem correct
            editable=False,
            path="",
            minResolutionHint=self.min_resolution_hint,
            maxResolutionHint=self.max_resolution_hint,
            ogcServer=self.ogc_server,
            childLayers=[
                LayerSettings(
                    name=self.name,
                    minResolutionHint=self.min_resolution_hint,
                    maxResolutionHint=self.max_resolution_hint,
                    queryable=bool(self.queryable),
                )
            ],
        )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


class PublishedAsLayerWmts(Layer):
    """
    Layer extension for WMTS layer
    """

    published_as_type = "geogirafe_wmts_layer"
    layer_group = models.OneToOneField(
        LayerGroupMp,
        related_name="wmts_datasets",
        related_query_name="wmts_dataset",
        on_delete=models.CASCADE,
    )
    dataset = models.ForeignKey(
        RasterDataSet,
        related_name="published_as_geogirafe_wmtss",
        related_query_name="published_as_geogirafe_wmts",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = f'WMTS {_("Layer")}'
        verbose_name_plural = f'WMTS {_("Layers")}'

    def __str__(self):
        return f"{self.name}"

    def as_dataclass(self):
        config = ParserConfig(
            fail_on_unknown_properties=False, fail_on_unknown_attributes=False
        )
        source = DictDecoder(config).decode(self.dataset.source, WmtsSource)
        metadata = None
        if self.metadata:
            metadata = DictDecoder(config).decode(self.metadata, MetaData)
        dimensions = None
        if self.dimensions:
            dimensions = DictDecoder(config).decode(self.dimensions, Dimensions)
        return WmtsLayer(
            id=self.themes_json_id,
            name=self.name,
            url=source.url,
            layer=source.layers,
            type="WMTS",
            imageType=source.format,
            metadata=metadata,
            # TODO: Fix that, its not stored correctly
            style="default",
            matrix_set=source.tile_matrix_set,
            # TODO: fix that
            dimensions=dimensions,
            # TODO: Fix that, it does not seem correct
            editable=False,
            path="",
        )


class OgcServer(models.Model):
    """
    Definition of cartographic servers that can be selected when configurating layers
    """

    url = models.URLField()
    type = models.CharField()
    credential = models.BooleanField(default=False)
    image_type = models.CharField()
    wfs_support = models.BooleanField(blank=True, null=True)
    is_single_tile = models.BooleanField(blank=True, null=True)
    namespace = models.CharField(null=True)
    name = models.CharField(null=True, unique=True)
    description = models.CharField(blank=True, null=True)
    url_wfs = models.URLField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)

    class Meta:
        verbose_name = _("OGC Server")
        verbose_name_plural = _("OGC Servers")

    def __str__(self):
        return f"{self.name}"

    def as_dataclass(self):
        attributes: list[dataclasses.LinkedLayer] = [
            DictDecoder().decode(attribute, dataclasses.LinkedLayer)
            for attribute in self.attributes
        ]
        return dataclasses.OgcServer(
            name=self.name,
            url=self.url,
            urlWfs=self.url_wfs,
            type=self.type,
            imageType=self.image_type,
            wfsSupport=self.wfs_support,
            isSingleTile=self.is_single_tile,
            attributes=attributes,
            # TODO: Find a useful way how to set this
            credential=False,
            namespace=self.namespace,
        )

    @classmethod
    def from_dataclass(cls, clazz: dataclasses.OgcServer, mandant: Mandant) -> "OgcServer":
        return cls(
            mandant=mandant,
            url=clazz.url,
            type=clazz.type,
            credential=clazz.credential,
            image_type=clazz.imageType,
            wfs_support=clazz.wfsSupport,
            is_single_tile=clazz.isSingleTile,
            namespace=clazz.namespace,
            name=clazz.name,
            url_wfs=clazz.urlWfs,
            attributes=DictEncoder().encode(clazz.attributes),
        )
