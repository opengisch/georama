from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.core.entities.models import PermissionInterface, PublishedAs
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet


class PublishedAsWmsAbstract(PublishedAs):
    class Meta:
        abstract = True

    published_as_type = "maps"
    extent_buffer = models.FloatField(default=0.0, null=False)
    queryable = models.BooleanField(default=True, null=True, blank=True)
    
    extent = models.CharField(max_length=1000, blank=True)
    preview = models.BinaryField(blank=True, null=True)

    @property
    def get_raster_dataset(self) -> RasterDataSet:
        raise NotImplementedError()

    @property
    def get_vector_dataset(self) -> VectorDataSet:
        raise NotImplementedError()

    @property
    def get_custom_dataset(self) -> CustomDataSet:
        raise NotImplementedError()

    @property
    def bound_dataset(self) -> VectorDataSet | RasterDataSet | CustomDataSet:
        if isinstance(self.get_raster_dataset, RasterDataSet):
            return self.get_raster_dataset
        elif isinstance(self.get_vector_dataset, VectorDataSet):
            return self.get_vector_dataset
        elif isinstance(self.get_custom_dataset, CustomDataSet):
            return self.get_custom_dataset
        else:
            raise NotImplementedError(
                "linked dataset has to be RasterDataSet|VectorDataSet|CustomDataSet!"
            )

    @property
    def readable_identifier(self) -> str:
        dataset = self.bound_dataset
        return f"{dataset.project.mandant.name}.{dataset.project.name}.{dataset.name}.{self.identifier}"

    @property
    def permissions(self) -> List[PermissionInterface]:
        # No need for Update or delete with WMS...
        return self.read_permissions

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        dataset = self.bound_dataset
        if self.name is None:
            # TODO: maybe we want this to be configurable?
            self.name = dataset.name
        if self.title is None:
            self.title = dataset.title
        if not self.extent:
            self.extent = dataset.bbox
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


class PublishedAsWms(PublishedAsWmsAbstract):
    class Meta:
        verbose_name = f'WMS {_("Layer")}'
        verbose_name_plural = f'WMS {_("Layers")}'

    raster_dataset = models.ForeignKey(
        RasterDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )
    vector_dataset = models.ForeignKey(
        VectorDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )
    custom_dataset = models.ForeignKey(
        CustomDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )

    @property
    def get_raster_dataset(self) -> RasterDataSet:
        return self.raster_dataset

    @property
    def get_vector_dataset(self) -> VectorDataSet:
        return self.vector_dataset

    @property
    def get_custom_dataset(self) -> CustomDataSet:
        return self.custom_dataset
