import uuid

from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase

from georama.features.managers.feature_layer import FeatureLayerManager
from georama.integration.models.datasource import Vector


class FeatureLayer(models.Model):
    class Meta:
        verbose_name = _("feature layer")
        verbose_name_plural = _("feature layers")

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the feature layer.")
    )
    datasource = models.ForeignKey(
        Vector,
        related_name="feature_layers",
        related_query_name="feature_layer",
        on_delete=models.CASCADE,
        help_text=_("Datasource the feature layer points to."),
    )

    objects = FeatureLayerManager()

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self._state.adding:
                from georama.features.models.field import Field

                super().save(*args, **kwargs)
                Field.objects.bulk_create(
                    Field(
                        feature_layer=self,
                        datasource_field=datasource_field,
                        name=datasource_field.name,
                    )
                    for datasource_field in self.datasource.fields.all()
                )
            else:
                super().save(*args, **kwargs)


class FeatureLayerUserObjectPermission(UserObjectPermissionBase):
    content_object = models.ForeignKey(
        FeatureLayer, on_delete=models.CASCADE, related_name="user_object_permissions"
    )


class FeatureLayerGroupObjectPermission(GroupObjectPermissionBase):
    content_object = models.ForeignKey(
        FeatureLayer, on_delete=models.CASCADE, related_name="group_object_permissions"
    )
