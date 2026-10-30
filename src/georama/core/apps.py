from django.utils.translation import gettext_lazy as _

from georama.core.common.apps import GeoramaAbstractConfig


class CoreConfig(GeoramaAbstractConfig):
    label = "core"
    verbose_name = "Core"
    name = "georama.core"
    description = _("The master app.")

    def ready(self):
        # We don't want to register a menu for Core on the Page
        pass
