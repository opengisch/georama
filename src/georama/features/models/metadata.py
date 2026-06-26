from django.utils.translation import gettext_lazy as _

from georama.core.common.models import BaseMetadata


class Metadata(BaseMetadata):
    class Meta:
        verbose_name = _("metadata")
        verbose_name_plural = _("metadata")
