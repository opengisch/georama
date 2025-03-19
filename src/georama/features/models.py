from typing import List

from django.db import models

from georama.core.entities.models import (
    PermissionInterface,
    PublishedAs,
    PublishedAsRoleNameSystem,
)
from georama.data_integration.models import VectorDataSet

COLUMN_TYPE_VALUES = {
    "numeric": "Numerical Type",
    "string": "Alphanumerical Type",
    "boolean": "Boolean Type",
    "date": "Date Type",
    "datetime": "Datetime Type",
}


class PublishedAsVectorFeature(PublishedAs):

    published_as_type = "feature"
    column_permission = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @property
    def permissions(self) -> List[PermissionInterface]:
        layer_permissions = super().permissions
        if self.column_permission:
            # NOTE: self.columns not defined and guaranteed to exist as this is an abstract class.
            # possible to define abstract django property/DB field?
            layer_permissions = layer_permissions + [col.permissions for col in self.columns.all()]
        return layer_permissions


class Column(PublishedAsRoleNameSystem):
    published_as_type = "feature_column"
    title = models.CharField(max_length=1000)

    class Meta:
        abstract = True


class PublishedAsWfs(PublishedAsVectorFeature):
    dataset = models.ForeignKey(
        VectorDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wfs",
        related_query_name="published_ogc_wfs",
        on_delete=models.CASCADE,
    )


class ColumnWfs(Column):
    published_definition = models.ForeignKey(
        PublishedAsWfs,
        related_name="columns",
        related_query_name="column",
        on_delete=models.CASCADE,
    )


class PublishedAsOgcApiFeatures(PublishedAsVectorFeature):
    dataset = models.ForeignKey(
        VectorDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_api_features",
        related_query_name="published_ogc_api_feature",
        on_delete=models.CASCADE,
    )

    @property
    def readable_identifier(self) -> str:
        dataset = self.dataset
        return f"{dataset.project.mandant.name}.{dataset.project.name}.{self.identifier}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name is None and isinstance(self.dataset, VectorDataSet):
            # TODO: maybe we want this to be configurable?
            self.name = f"{self.dataset.project.mandant.name}.{self.dataset.project.name}.{self.dataset.name}"
        if self.title is None and isinstance(self.dataset, VectorDataSet):
            self.title = self.dataset.title
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
        for field in self.dataset.fields.all():
            if (
                ColumnOgcApiFeatures.objects.filter(
                    name=field.name, published_definition=self
                ).count()
                == 0
            ):
                ColumnOgcApiFeatures(
                    published_definition=self,
                    name=field.name,
                    title=field.name.title(),
                    public=True,
                ).save()


class ColumnOgcApiFeatures(Column):
    published_definition = models.ForeignKey(
        PublishedAsOgcApiFeatures,
        related_name="columns",
        related_query_name="column",
        on_delete=models.CASCADE,
    )
