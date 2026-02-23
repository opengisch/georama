from georama.core.entities.models import PublishedAs
from georama.core.models.mixins import GeoramaPermissionMixin


class TypingHelperClass(GeoramaPermissionMixin, PublishedAs):
    pass
