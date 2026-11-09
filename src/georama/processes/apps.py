from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from qgis_server_light.dispatcher.redis_asio import RedisStateQueue

from georama.core.apps import GeoramaAbstractConfig
from georama.maps.maps_config import Config

central_app_label = "processes"

qsl_redis_state_queue = RedisStateQueue.create(Config().redis_url)


class ProcessConfig(GeoramaAbstractConfig):
    label = "processes"
    name = "georama.processes"
    menu_order: int = 10
    description = _("OGC API Processes.")
    app_index_page = "processes:api-landing"

    def ready(self):
        from georama.core.common.remote_actions import RemoteAction, register_remote_action
        from georama.integration.models.datasource import Datasource

        super().ready()
        rma = RemoteAction(
            target=reverse("processes:process-input-manager-publish-from-datasource"),
            name=_("ProcessInput"),
            icon_classes="fa fa-circle-plus",
            help_text=_("Publishes this Datasource as a new process input in the Processes app."),
            origin=self.name,
            permissions=["processes.add_processinput"],
            count_relation="process_inputs",
        )
        register_remote_action(Datasource, rma)
