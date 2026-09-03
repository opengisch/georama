import logging

from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.job.common.input import OgcFilter110
from qgis_server_light.interface.job.render.input import QslJobParameterRender

from georama.core.models import Organisation
from georama.maps.interfaces.georama.requests import GetMapRequestParams
from georama.maps.services.wms_1_3_0 import WmsOperation


class WmsGetMap(WmsOperation):
    default_style_name = "default"

    def __init__(self, appname: str, url: str, user, model, organisation: Organisation):
        super().__init__(appname, url, user, model, organisation)

    def prepare_job_content(
        self, service_params: GetMapRequestParams
    ) -> QslJobParameterRender:
        # we pass the requested layers to filter DB objects
        # (this includes permission checks and fails for
        # all request when only one layer is not permitted!)
        accessible_wms_layers = self.obtain_accessible_layers(service_params.layer_list)

        if service_params.DPI:
            dpi = service_params.DPI
        elif service_params.FORMAT_OPTIONS:
            dpi = service_params.FORMAT_OPTIONS.split(":")[-1]
        else:
            dpi = None

        job = QslJobParameterRender(
            # we set the extent buffer to zero, this is used to
            # control rendering issues like
            # https://github.com/qgis/QGIS/issues/30251
            bbox=BBox.from_string(service_params.BBOX),
            crs=service_params.CRS,
            width=service_params.WIDTH,
            height=service_params.HEIGHT,
            dpi=int(dpi),
            format=service_params.FORMAT,
            layers=[],
        )
        for wms_layer, requested_style_name, filter_definition in zip(
            accessible_wms_layers,
            service_params.style_list,
            service_params.filter_list or [None] * len(accessible_wms_layers),
            strict=True,
        ):
            if requested_style_name == self.default_style_name:
                qsl_job_layer = wms_layer.datasource.to_qsl_job_layer()
            else:
                try:
                    qsl_job_layer = wms_layer.datasource.to_qsl_job_layer(
                        requested_style_name
                    )
                except LookupError:
                    raise ValueError(
                        f"Requested style {requested_style_name} is not"
                        f"defined for layer {wms_layer.datasource.name}"
                    )

            logging.debug(f"Set style for layer to: {qsl_job_layer.style.name}")
            # TODO@maps: implement check for vector
            if wms_layer.datasource.type == "vector" and filter_definition:
                # since we will use this in the on a plain
                # list of layers, the largest extent buffer
                # should be applied
                qsl_job_layer.filter = OgcFilter110(definition=filter_definition)
            job.layers.append(qsl_job_layer)
        # WMS layers order are given in the order they should be drawn, but the QSL
        # uses QgsMapSettings in which the drawing order is reversed
        job.layers.reverse()
        logging.debug(f"Job prepared successfully: {job}")
        return job
