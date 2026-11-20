import base64
import hashlib
import uuid
from urllib.parse import urlencode

from django.conf import settings
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.common.managers import OrganisationalManager
from georama.integration.models import Project
from georama.maps.apps import central_app_label
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import Theme as GGTheme
from georama.webgis.managers.theme import ThemeManager
from georama.webgis.models.metadata import Metadata


class Theme(models.Model):
    ORGANISATION_FIELD_NAME = "project__organisation"

    PERMISSIONS = {
        "can_view": "view_published_theme",
        "can_create": "create_objects_theme_vector_layer",
        "can_update": "update_objects_theme_vector_layer",
        "can_delete": "delete_objects_theme_vector_layer",
    }

    ACTION_MAP = {
        "grant": (True, [PERMISSIONS["can_view"]], _("grant access")),
        "allow_create": (
            True,
            [PERMISSIONS["can_view"], PERMISSIONS["can_create"]],
            _("allow create"),
        ),
        "allow_update": (
            True,
            [PERMISSIONS["can_view"], PERMISSIONS["can_update"]],
            _("allow update"),
        ),
        "allow_delete": (
            True,
            [PERMISSIONS["can_view"], PERMISSIONS["can_delete"]],
            _("allow delete"),
        ),
        "prevent_create": (False, [PERMISSIONS["can_create"]], _("prevent create")),
        "prevent_update": (False, [PERMISSIONS["can_update"]], _("prevent update")),
        "prevent_delete": (False, [PERMISSIONS["can_delete"]], _("prevent delete")),
        "revoke": (False, list(PERMISSIONS.values()), _("revoke access")),
    }

    class Meta:
        ordering = ["ordering"]
        verbose_name = _("Theme")
        verbose_name_plural = _("Themes")
        permissions = [
            # permission which is used on the model
            ("manage_object_permissions", "Can manage object permissions"),
            # permission which is used for the object permission evaluation on the published themes
            ("view_published_theme", "Can view published theme"),
            ("create_objects_theme_vector_layer", "Can create items on theme vector layer"),
            ("delete_objects_theme_vector_layer", "Can delete items on theme vector layer"),
            ("update_objects_theme_vector_layer", "Can update items on theme vector layer"),
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(
        Project,
        related_name="themes",
        on_delete=models.CASCADE,
        verbose_name=_("project"),
    )
    metadata = models.ForeignKey(
        Metadata,
        related_name="themes",
        on_delete=models.CASCADE,
        verbose_name=_("metadata"),
    )
    public = models.BooleanField(default=False, verbose_name=_("public"))
    ordering = models.IntegerField(verbose_name=_("ordering"))
    preview = models.BinaryField(
        null=True,
        blank=True,
        help_text=_("Preview image of the theme."),
        verbose_name=_("preview"),
    )
    theme_json = models.JSONField(verbose_name=_("theme JSON"))
    background_layers = models.JSONField(blank=True, verbose_name=_("background layers"))
    ogc_servers = models.JSONField(blank=True, verbose_name=_("OGC servers"))

    objects = ThemeManager()

    @property
    def identifier(self):
        return str(self.id)

    @property
    def icon_default(self):
        return static("webgis/images/georama-logo-geogirafe.svg")

    @property
    def preview_image(self):
        if self.preview is not None:
            return f"data:image/png;base64,{base64.b64encode(self.preview).decode()}"
        return self.icon_default

    @property
    def icon_url(self) -> str:
        if self.preview is None:
            return self.icon_default
        url = reverse("webgis:theme-preview", kwargs={"pk": self.pk})
        # the content hash changes with every new preview, so browsers drop their cached copy
        return f"{url}?{urlencode({'v': hashlib.md5(self.preview).hexdigest()})}"

    def __str__(self):
        return self.metadata.title

    def as_dataclass(self) -> GGTheme:
        config = ParserConfig(fail_on_unknown_properties=False)
        return DictDecoder(config).decode(self.theme_json, GGTheme)

    def set_from_dataclass(self, theme: GGTheme):
        self.theme_json = DictEncoder().encode(theme)

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:theme-detail", kwargs={"pk": self.pk})

    @property
    def endpoint_url(self) -> str | None:
        if not self.theme_json:
            return None
        ggtheme = self.as_dataclass()
        params = {"themes": ggtheme.name}
        if ggtheme.zoom is not None:
            params["map_zoom"] = ggtheme.zoom
        if len(ggtheme.location) >= 2:
            params["map_x"], params["map_y"] = ggtheme.location[0], ggtheme.location[1]
        return f"{settings.WEBGISURL}?{urlencode(params)}"


class UserManager(UserObjectPermissionManager, OrganisationalManager): ...


class GroupManager(GroupObjectPermissionManager, OrganisationalManager): ...


class ThemeUserObjectPermission(UserObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__project__organisation"
    content_object = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name="user_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()


class ThemeGroupObjectPermission(GroupObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__project__organisation"
    content_object = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name="group_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = GroupManager()
