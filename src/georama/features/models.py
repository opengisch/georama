from typing import List

from django.contrib.auth.models import User
from django.db import models

from georama.core.entities.models import (
    PermissionInterface,
    PublishedAs,
    PublishedAsRoleNameSystem,
    delete_publishedas_db_permissions,
    save_publishedas_db_permissions
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

    def get_columns(self) -> List["Column"]:
        raise NotImplementedError

    @property
    def columns_permissions(self) -> List[PermissionInterface]:
        """Returns all the possible permissions for columns of this VectorFeature
        
        Doesn't check if column permissions are enabled on this VectorFeature publication"""
        return [p for col in self.get_columns() for p in col.permissions]

    @property
    def all_permissions(self) -> List[PermissionInterface]:
        permissions = self.permissions
        if self.column_permission:
            permissions = permissions + self.columns_permissions
        return permissions

    def has_general_permission(self, user: User, app_name: str) -> bool:
        """include columns permissions in this check"""
        if self.public:
            return True
        permissions = self.permission_codenames if not self.column_permission else [p.codename for p in self.all_permissions]
        return self._has_grained_permission(user, permissions, app_name)


class Column(PublishedAsRoleNameSystem):
    published_as_type = "feature_column"
    title = models.CharField(max_length=1000)

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        models.signals.pre_delete.connect(delete_publishedas_db_permissions, sender=cls)

    @property
    def create_permissions(self) -> List[PermissionInterface]:
        """delete permission not relevant for specific property: create/delete property happens at the layer level"""
        return []

    @property
    def delete_permissions(self) -> List[PermissionInterface]:
        """delete permission not relevant for specific property: create/delete property happens at the layer level"""
        return []

    def get_published_definition(self) -> PublishedAsVectorFeature:
        raise NotImplementedError

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = f"{self.get_published_definition().name}.{self.title}"
        super().save(*args, **kwargs)
        save_publishedas_db_permissions(self)

    @property
    def readable_identifier(self) -> str:
        """Using the publicatoin identifier at the end to make column visibly linked to their publication"""
        return f"{self.get_published_definition().readable_identifier}.{self.name}"

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

    def get_columns(self) -> List["ColumnWfs"]:
        return self.columns.all()


class ColumnWfs(Column):
    published_definition = models.ForeignKey(
        PublishedAsWfs,
        related_name="columns",
        related_query_name="column",
        on_delete=models.CASCADE,
    )

    def get_published_definition(self) -> PublishedAsWfs:
        return self.published_definition


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
        return f"{dataset.project.mandant.name}.{dataset.project.name}.{dataset.name}.{self.identifier}"

    def get_columns(self) -> List["ColumnOgcApiFeatures"]:
        return self.columns.all()

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
                not ColumnOgcApiFeatures.objects.filter(
                    name=field.name, published_definition=self
                ).exists()
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

    def get_published_definition(self) -> PublishedAsOgcApiFeatures:
        return self.published_definition


