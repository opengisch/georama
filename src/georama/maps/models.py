from typing import List

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

from georama.core.entities.models import PermissionInterface, PublishedAs
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet


class PublishedAsWms(PublishedAs):

    published_as_type = "wms"
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
    extent_buffer = models.FloatField(default=0.0, null=False)

    @property
    def bound_dataset(self) -> VectorDataSet | RasterDataSet | CustomDataSet:
        if isinstance(self.raster_dataset, RasterDataSet):
            return self.raster_dataset
        elif isinstance(self.vector_dataset, VectorDataSet):
            return self.vector_dataset
        elif isinstance(self.custom_dataset, CustomDataSet):
            return self.custom_dataset
        else:
            raise NotImplementedError(
                "linked dataset has to be RasterDataSet|VectorDataSet|CustomDataSet!"
            )

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
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
        content_type = ContentType.objects.get_for_model(PublishedAsWms)
        for permission in self.permissions:
            if Permission.objects.filter(codename=permission.codename).count() == 0:
                Permission(
                    codename=permission.codename,
                    name=f"{permission.readable_name} ({dataset.project.mandant.name}.{dataset.project.name}.{self.identifier})",
                    content_type=content_type,
                ).save()

    def delete(self, using=None, keep_parents=False):
        Permission.objects.filter(codename__in=self.permission_codenames).delete()
        super().delete(
            using=using,
            keep_parents=keep_parents,
        )
