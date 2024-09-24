from typing import List
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


from georama.core.entities.models import PublishedAs, PublishedAsRoleNameSystem, PermissionInterface
from georama.qmeleon.models import VectorDataSet

COLUMN_TYPE_VALUES = {
    "numeric": "Numerical Type",
    "string": "Alphanumerical Type",
    "boolean": "Boolean Type",
    "date": "Date Type",
    "datetime": "Datetime Type"
}


class PublishedAsVectorFeature(PublishedAs):

    published_as_type = 'feature'
    column_permission = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @property
    def permissions(self) -> List[PermissionInterface]:
        if self.public:
            return []
        else:
            role_names = (
                    self.read_permissions +
                    self.create_permissions +
                    self.update_permissions +
                    self.delete_permissions
            )
            if not self.column_permission:
                return role_names
            else:
                for column in self.columns.all():
                    role_names = role_names + column.permissions
                return role_names


class Column(PublishedAsRoleNameSystem):
    published_as_type = 'feature_column'
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
        on_delete=models.CASCADE
    )


class ColumnWfs(Column):
    published_definition = models.ForeignKey(
        PublishedAsWfs,
        related_name="columns",
        related_query_name="column",
        on_delete=models.CASCADE
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
        on_delete=models.CASCADE
    )

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.name is None and isinstance(self.dataset, VectorDataSet):
            # TODO: maybe we want this to be configurable?
            self.name = f'{self.dataset.project.mandant.name}.{self.dataset.project.name}.{self.dataset.name}'
        if self.title is None and isinstance(self.dataset, VectorDataSet):
            self.title = self.dataset.title
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
        for field in self.dataset.fields.all():
            if ColumnOgcApiFeatures.objects.filter(name=field.name, published_definition=self).count() == 0:
                ColumnOgcApiFeatures(
                    published_definition=self,
                    name=field.name,
                    title=field.name.title(),
                    public=True
                ).save()
        content_type = ContentType.objects.get_for_model(PublishedAsOgcApiFeatures)
        for permission in self.permissions:
            if Permission.objects.filter(codename=permission.codename).count() == 0:
                Permission(
                    codename=permission.codename,
                    name=f'{permission.readable_name} ({self.dataset.project.mandant.name}.{self.dataset.project.name})',
                    content_type=content_type
                ).save()

    def delete(self, using=None, keep_parents=False):
        Permission.objects.filter(codename__in=self.permission_codenames).delete()
        super().delete(
            using=using,
            keep_parents=keep_parents,
        )


class ColumnOgcApiFeatures(Column):
    published_definition = models.ForeignKey(
        PublishedAsOgcApiFeatures,
        related_name="columns",
        related_query_name="column",
        on_delete=models.CASCADE
    )
