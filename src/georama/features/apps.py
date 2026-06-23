from django.utils.translation import gettext_lazy as _

from georama.core.common.apps import GeoramaAbstractConfig


class FeaturesConfig(GeoramaAbstractConfig):
    label = "features"
    name = "georama.features"
    menu_order: int = 10
    description = _("Share feature layers.")
