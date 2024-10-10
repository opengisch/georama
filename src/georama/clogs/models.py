from typing import List

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.qgis import WmtsSource, WmsSource
from simple_history.models import HistoricalRecords
from treebeard.mp_tree import MP_Node
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.clogs.interfaces.geomapfish import ThemesJson
from georama.clogs.interfaces.geomapfish.themes_json_2_8.dataclasses import Theme, MetaData, WmtsLayer, \
    WmsLayer, LayerSettings, LayerGroup, Dimensions
from georama.core.entities.models import PublishedAs, PermissionInterface
from georama.qmeleon.models import Project, CustomDataSet, RasterDataSet, Mandant
from georama.clogs.interfaces.geomapfish.themes_json_2_8 import dataclasses


class Interface(models.Model):

    """
    Model that matches a configuration with a interface configuration (desktop, mobile, api, ...)
    """

    name = models.CharField()
    description = models.CharField(blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("Interface")
        verbose_name_plural = _("Interfaces")

    def __str__(self):
        return f"{self.name}"


class PublishedAsTheme(PublishedAs):
    """
    Top item of layer tree organization
    """
    themes_json_id = models.IntegerField(null=True)
    published_as_type = 'geogirafe_theme'
    project = models.ForeignKey(
        Project,
        related_name="published_as_geogirafe_themes",
        related_query_name="published_as_geogirafe_theme",
        on_delete=models.CASCADE
    )
    metadata = models.JSONField()
    icon = models.CharField(blank=True, null=True)
    ordering = models.IntegerField()
    history = HistoricalRecords()

    class Meta:
        ordering = ["ordering"]
        verbose_name = _("Thème")
        verbose_name_plural = _("Thèmes")

    def __str__(self):
        return f"{self.name}"

    def as_dataclass(self) -> Theme:
        config = ParserConfig(fail_on_unknown_properties=False)
        return Theme(
            name=self.name,
            id=self.themes_json_id,
            icon=self.icon,
            metadata=DictDecoder(config).decode(self.metadata, MetaData)
        )

    @property
    def permissions(self) -> List[PermissionInterface]:
        if self.public:
            return []
        else:
            return self.read_permissions

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
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
        content_type = ContentType.objects.get_for_model(PublishedAsTheme)
        for permission in self.permissions:
            if Permission.objects.filter(codename=permission.codename).count() == 0:
                Permission(
                    codename=permission.codename,
                    name=f'{permission.readable_name} ({self.project.mandant.name}.{self.project.name})',
                    content_type=content_type
                ).save()

    def delete(self, using=None, keep_parents=False):
        Permission.objects.filter(codename__in=self.permission_codenames).delete()
        super().delete(
            using=using,
            keep_parents=keep_parents,
        )


class LayerGroupMp(MP_Node):
    """
    Recursive model from django-treebeard to handle children-parent relationships
    """
    themes_json_id = models.IntegerField(null=True)
    name = models.CharField(max_length=128)
    theme = models.ForeignKey(
        PublishedAsTheme,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="tree_elements",
        related_query_name="tree_element",
        on_delete=models.CASCADE
    )
    # TODO: add metadata ManyToManyField
    metadata = models.JSONField(default=None, null=True)
    mixed = models.BooleanField(default=None, null=True)
    ogc_server = models.CharField(max_length=2048, default=None, null=True)
    dimensions = models.JSONField(default=None, null=True)
    node_order_by = ["name"]

    class Meta:
        verbose_name = _("Groupe de de couche")
        verbose_name_plural = _("Groupes de couche")

    def __str__(self):
        return f"Groupe: {self.name}"

    def as_dataclass(self) -> LayerGroup:
        config = ParserConfig(fail_on_unknown_properties=False)
        metadata = None
        if self.metadata:
            metadata = DictDecoder(config).decode(self.metadata, MetaData)
        dimensions = None
        if self.dimensions:
            dimensions = DictDecoder(config).decode(self.dimensions, Dimensions)
        return LayerGroup(
            id=self.themes_json_id,
            name=self.name,
            metadata=metadata,
            dimensions=dimensions,
            mixed=self.mixed,
            ogcServer=self.ogc_server
        )


class Layer(PublishedAs):
    """
    Base model for geographic Layer
    """
    themes_json_id = models.IntegerField(null=True)
    metadata = models.JSONField(default=None, null=True)
    dimensions = models.JSONField(default=None, null=True)
    history = HistoricalRecords()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class PublishedAsLayerWms(Layer):
    """
    Layer extension for WMS layer
    """
    published_as_type = 'geogirafe_wms_layer'
    layer_group = models.OneToOneField(
        LayerGroupMp,
        related_name="wms_datasets",
        related_query_name="wms_dataset",
        on_delete=models.CASCADE
    )
    dataset = models.ForeignKey(
        RasterDataSet,
        related_name="published_as_geogirafe_wmss",
        related_query_name="published_as_geogirafe_wms",
        on_delete=models.CASCADE
    )
    ogc_server = models.CharField(null=True)
    min_resolution_hint = models.FloatField(default=None)
    max_resolution_hint = models.FloatField(default=None)
    # TODO: Make this a real model instead of JSON
    child_layers = models.JSONField(default=None)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("Couche WMS")
        verbose_name_plural = _("Couches WMS")

    def __str__(self):
        return f"{self.name}"

    def as_dataclass(self, geogirafe_config: ThemesJson) -> WmsLayer:
        config = ParserConfig(fail_on_unknown_properties=False)
        if self.dataset.source:
            source = DictDecoder(config).decode(self.dataset.source, WmsSource)
        metadata = None
        if self.metadata:
            metadata = DictDecoder(config).decode(self.metadata, MetaData)
        dimensions = None
        if self.dimensions:
            dimensions = DictDecoder(config).decode(self.dimensions, Dimensions)
        return WmsLayer(
            id=self.themes_json_id,
            name=self.name,
            # TODO: Fix layers, it has to written to the datasource
            layers=source.layers,
            type="WMS",
            imageType=geogirafe_config.get_ogc_server_by_name(
                self.ogc_server
            ).imageType,
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
            childLayers=DictDecoder(config).decode(self.child_layers, list[LayerSettings])
        )


class PublishedAsLayerWmts(Layer):
    """
    Layer extension for WMTS layer
    """
    published_as_type = 'geogirafe_wmts_layer'
    layer_group = models.OneToOneField(
        LayerGroupMp,
        related_name="wmts_datasets",
        related_query_name="wmts_dataset",
        on_delete=models.CASCADE
    )
    dataset = models.ForeignKey(
        RasterDataSet,
        related_name="published_as_geogirafe_wmtss",
        related_query_name="published_as_geogirafe_wmts",
        on_delete=models.CASCADE
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("WMTS Layer")
        verbose_name_plural = _("WMTS Layers")

    def __str__(self):
        return f"{self.name}"

    def as_dataclass(self):
        config = ParserConfig(fail_on_unknown_properties=False)
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
            path=""
        )


class OgcServer(models.Model):
    """
    Definition of cartographic servers that can be selected when configurating layers
    """
    mandant = models.ForeignKey(
        Mandant,
        related_name="ogc_servers",
        related_query_name="ogc_server",
        on_delete=models.CASCADE,
        null=True
    )
    url = models.URLField()
    type = models.CharField()
    credential = models.BooleanField(default=False)
    image_type = models.CharField()
    wfs_support = models.BooleanField(blank=True, null=True)
    is_single_tile = models.BooleanField(blank=True, null=True)
    namespace = models.CharField(null=True)
    name = models.CharField(null=True)
    description = models.CharField(blank=True, null=True)
    url_wfs = models.URLField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("Serveur OGC")
        verbose_name_plural = _("Serveurs OGC")

    def __str__(self):
        return f"{self.name}"

    def as_dataclass(self):
        attributes: list[dataclasses.LinkedLayer] = [
            DictDecoder().decode(attribute, dataclasses.LinkedLayer) for attribute in self.attributes
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
            namespace=self.namespace
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
            attributes=DictEncoder().encode(clazz.attributes)
        )
