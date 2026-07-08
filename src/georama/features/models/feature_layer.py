import uuid

from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase

from georama.core.common.managers import OrganisationalManager
from georama.features.managers.feature_layer import FeatureLayerManager
from georama.features.models.field import Field
from georama.features.models.metadata import Metadata
from georama.integration.models.datasource import Vector


class FeatureLayer(models.Model):
    ORGANISATION_FIELD_NAME = "datasource__project__organisation"

    ON_EXCEED_CHOICES = (
        ("ERROR", "error"),
        ("THROTTLE", "throttle"),
    )

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
    default_items = models.IntegerField(
        default=10,
        null=True,
        help_text=_("The default number of features that should be returned for the layer."),
    )
    max_items = models.IntegerField(
        default=500,
        null=True,
        help_text=_("The maximum number of features that may be returned for the layer."),
    )
    on_exceed = models.CharField(
        default="ERROR",
        choices=ON_EXCEED_CHOICES,
        max_length=10,
        null=True,
        help_text=_(
            "Whether the server should return an error or cap the value when more than"
            "max_items are requested"
        ),
    )
    metadata = models.OneToOneField(
        Metadata,
        related_name="feature_layer",
        on_delete=models.CASCADE,
        help_text=_("Metadata of the feature layer."),
    )
    objects = FeatureLayerManager()

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self._state.adding:
                super().save(*args, **kwargs)
                Field.objects.bulk_create(self.datasource_related_fields())
            else:
                super().save(*args, **kwargs)

    def datasource_related_fields(self):
        for datasource_field in self.datasource.fields.all():
            yield Field(
                feature_layer=self,
                datasource_field=datasource_field,
                name=datasource_field.name,
            )

    @property
    def title(self):
        return self.metadata.title


class UserManager(UserObjectPermissionManager, OrganisationalManager): ...


class GroupManager(GroupObjectPermissionManager, OrganisationalManager): ...


class FeatureLayerUserObjectPermission(UserObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__datasource__project__organisation"
    content_object = models.ForeignKey(
        FeatureLayer, on_delete=models.CASCADE, related_name="user_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()


class FeatureLayerGroupObjectPermission(GroupObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__datasource__project__organisation"
    content_object = models.ForeignKey(
        FeatureLayer, on_delete=models.CASCADE, related_name="group_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = GroupManager()
