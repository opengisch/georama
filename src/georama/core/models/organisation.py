import logging
import uuid
from pathlib import Path

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

SUBDOMAIN_REGEX = r"^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?(\.[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?)?$"


def validate_domain_name_not_global(value: str) -> None:
    global_folder = settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER
    if value == global_folder:
        raise ValidationError(
            _("Domain name must be different from the global one: ") + global_folder
        )


class Organisation(models.Model):
    class Meta:
        verbose_name = _("organisation")
        verbose_name_plural = _("organisations")

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the organisation.")
    )
    name = models.CharField(help_text=_("Name of the organisation."))
    domain = models.CharField(
        unique=True,
        help_text=_("Domain used to identify the organisation."),
        validators=[
            RegexValidator(SUBDOMAIN_REGEX),
            validate_domain_name_not_global,
        ],
    )
    public_access = models.BooleanField(
        default=False, help_text=_("Whether anonymous users can access this organisation.")
    )

    def __str__(self):
        return f"{self.name} (domain: {self.domain})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        organisation_folder: Path = settings.DATA_INTEGRATION_ROOT / self.domain
        if not organisation_folder.exists():
            logging.info(f"Organisation folder {self.domain} created")
            organisation_folder.mkdir()
        elif not organisation_folder.is_dir():
            raise Exception(f"A file already exists at {self.domain}")
        else:
            logging.debug(f"Organisation folder {self.domain} already created")
