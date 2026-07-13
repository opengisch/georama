from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.dispatcher.redis_asio import RedisQueue

from georama.core.common.apps import GeoramaAbstractConfig
from georama.maps.maps_config import Config

central_app_label = "maps"

qsl_redis_queue = RedisQueue.create(Config().redis_url)


class MapsConfig(GeoramaAbstractConfig):
    label = "maps"
    name = "georama.maps"
    menu_order: int = 10
    description = _("Share map layers.")
    app_index_page = "maps:maplayer-list"

    def ready(self):
        from georama.core.common.remote_actions import RemoteAction, register_remote_action
        from georama.integration.models.datasource import Datasource

        super().ready()
        rma = RemoteAction(
            target=reverse("maps:maplayer-manager-publish-from-datasource"),
            name=_("WmsLayer"),
            icon_classes="fa fa-circle-plus",
            help_text=_("Publishes this Datasource as a new WmsLayer in the Maps app."),
            origin=self.name,
            permissions=["maps.add_wmslayer"],
        )
        register_remote_action(Datasource, rma)
