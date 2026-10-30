from crispy_bootstrap5.bootstrap5 import Switch
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import fields, forms
from django.urls import reverse
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from qgis_server_light.interface.exporter.extract import Algorithm, ProcessingParameterType

from georama.core.common.managers import OrganisationalManager
from georama.core.models.organisation import Organisation
from georama.processes.apps import central_app_label, qsl_available_processes
from georama.processes.interface.ogc_api.processes.part1.v_100.main import (
    JobControlOptions,
    Link,
    ProcessBase,
    TransmissionMode,
)
from georama.processes.managers.process import ProcessManager
from georama.processes.mappers.parameter_types import HtmlInputMapper, JsonSchemaMapper

User = get_user_model()


class Process(models.Model):
    ORGANISATION_FIELD_NAME = "organisation"

    PERMISSIONS = {
        "can_view": "execute_process",
    }

    ACTION_MAP = {
        "grant": (True, [PERMISSIONS["can_view"]], "grant access"),
        "revoke": (False, list(PERMISSIONS.values()), "revoke access"),
    }

    class Meta:
        verbose_name = f"{_('Process')}"
        verbose_name_plural = f"{_('Processes')}"
        permissions = [
            ("can_manage_object_permissions", "Can manage object permissions"),
            ("execute_process", "Can execute process"),
        ]

    objects = ProcessManager()

    id = models.CharField(primary_key=True)

    public = models.BooleanField(default=False)

    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="processes",
        help_text=_("Organisation this process belongs to."),
    )

    def __str__(self):
        return f"{self.title} ({self.id})"

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:process-detail", kwargs={"pk": self.pk})

    @property
    def qsl_algorithm(self) -> Algorithm:
        return qsl_available_processes.algorithm_by_id(self.id)

    @property
    def qsl_algorithm_params_jsonschema(self) -> list[tuple[ProcessingParameterType, dict]]:
        mapper = JsonSchemaMapper()
        parameter_and_schema = []
        for p in self.qsl_algorithm.parameters:
            parameter_and_schema.append(
                (
                    p,
                    mapper.map(p),
                )
            )
        return parameter_and_schema

    @property
    def qsl_algorithm_params_html_form(self) -> forms.Form:
        mapper = HtmlInputMapper()
        attrs = {}
        switch_fields = []
        for p in self.qsl_algorithm.parameters:
            field = mapper.map(p)
            attrs[p.name] = field
            if isinstance(field, fields.BooleanField):
                switch_fields.append(Switch(p.name))
        attrs["helper"] = FormHelper()
        attrs["helper"].layout = Layout(*tuple(switch_fields))

        form = type("DynamicParamsForm", (forms.Form,), attrs)
        return form

    @property
    def title(self):
        return self.qsl_algorithm.display_name

    @property
    def description(self) -> str:
        return self.qsl_algorithm.short_description

    @property
    def help(self) -> str:
        return self.qsl_algorithm.short_help_string

    @property
    def dataclass(self):
        return ProcessBase(
            id=self.id,
            description=self.qsl_algorithm.short_help_string,
            job_control_options=[JobControlOptions.SYNC],
            output_transmission=[TransmissionMode.VALUE],
            title=self.qsl_algorithm.display_name,
            version="1.0.0",
            links=[
                Link(
                    type="application/json",
                    rel="self",
                    href=reverse(
                        f"{central_app_label}:process-detail",
                        kwargs={"pk": self.pk},
                    ),
                    href_lang="en",
                    title=gettext("Process execution"),
                ),
                Link(
                    type="application/json",
                    rel="execution",
                    href=reverse(
                        f"{central_app_label}:process-execution",
                        kwargs={"pk": self.pk},
                    ),
                    href_lang="en",
                    title=gettext("Process execution"),
                ),
            ],
        )


class UserManager(UserObjectPermissionManager, OrganisationalManager): ...


class GroupManager(GroupObjectPermissionManager, OrganisationalManager): ...


class ProcessUserObjectPermission(UserObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__organisation"
    content_object = models.ForeignKey(
        Process, on_delete=models.CASCADE, related_name="user_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()


class ProcessGroupObjectPermission(GroupObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__organisation"
    content_object = models.ForeignKey(
        Process, on_delete=models.CASCADE, related_name="group_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = GroupManager()
