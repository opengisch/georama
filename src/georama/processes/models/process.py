import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.forms import forms
from django.urls import reverse
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from qgis_server_light.interface.job.process.description import (
    ProcessDescription,
    ProcessDescriptions,
)

from georama.core.common.managers import OrganisationalManager
from georama.core.models.organisation import Organisation
from georama.processes.apps import central_app_label
from georama.processes.interface.ogc_api.processes.part1.v_100.main import (
    JobControlOptions,
    Link,
    ProcessBase,
    ProcessDetail,
    TransmissionMode,
)
from georama.processes.managers.process import ProcessManager
from georama.processes.mappers.input_descriptions import (
    HtmlInputMapper,
    HtmlOutputFormatMapper,
)

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
            ("manage_object_permissions", "Can manage object permissions"),
            ("execute_process", "Can execute process"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["algorithm_id", "organisation"],
                nulls_distinct=False,
                name="unique_process_algorithm_per_organisation",
            ),
        ]

    objects = ProcessManager()

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the process.")
    )

    algorithm_id = models.CharField(
        help_text=_("Identifier of the QGIS processing algorithm this process publishes."),
    )

    public = models.BooleanField(default=False)

    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="processes",
        help_text=_("Organisation this process belongs to."),
    )

    process_description: ProcessDescription | None = None

    def __str__(self):
        return f"{self.title} ({self.algorithm_id})"

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:process-detail", kwargs={"pk": self.pk})

    def describe(self, process_descriptions: ProcessDescriptions):
        try:
            self.process_description = process_descriptions.process_by_id(self.algorithm_id)
        except LookupError:
            self.process_description = None

    @property
    def served(self) -> bool:
        return self.process_description is not None

    @property
    def inputs_html_form(self) -> type[forms.Form]:
        return HtmlInputMapper().form_class(self.process_description.inputs)

    @property
    def outputs_html_form(self) -> type[forms.Form]:
        return HtmlOutputFormatMapper().form_class(self.process_description.outputs)

    @property
    def title(self) -> str:
        if self.process_description is None:
            return self.algorithm_id
        return self.process_description.title

    @property
    def description(self) -> str | None:
        if self.process_description is None:
            return None
        return self.process_description.description

    @property
    def dataclass(self):
        return ProcessBase(
            id=self.algorithm_id,
            description=self.description,
            job_control_options=[JobControlOptions.SYNC, JobControlOptions.ASYNC],
            output_transmission=[TransmissionMode.VALUE],
            title=self.title,
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

    @property
    def detail_dataclass(self) -> ProcessDetail:
        return ProcessDetail(
            **vars(self.dataclass),
            inputs=self.process_description.inputs,
            outputs=self.process_description.outputs,
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
