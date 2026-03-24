import logging

from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.job.common.input import OgcFilter110
from qgis_server_light.interface.job.render.input import QslJobParameterRender

from georama.data_integration.models import VectorDataSet
from georama.maps.interfaces.georama.requests import GetMapRequestParams
from georama.maps.services.wms_1_3_0 import WmsOperation


class WmsGetMap(WmsOperation):
    default_style_name = "default"

    def __init__(self, appname: str, url: str, user, model):
        super().__init__(appname, url, user, model)

    def prepare_job_content(
        self, service_params: GetMapRequestParams
    ) -> QslJobParameterRender | str:
        # we pass the requested layers to filter DB objects
        # (this includes permission checks and fails for
        # all request when only one layer is not permitted!)
        accessible_published_as = self.obtain_accessible_layers(service_params.layer_list)

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
        styles = service_params.style_list
        filters = service_params.filter_list
        for index, published_as in enumerate(accessible_published_as):
            requested_style_name = styles[index]
            dataset = published_as.bound_dataset
            if requested_style_name == self.default_style_name:
                qsl_job_layer = dataset.to_qsl_job_layer()
            else:
                try:
                    qsl_job_layer = dataset.to_qsl_job_layer(requested_style_name)
                except LookupError:
                    raise ValueError(  # noqa: B904
                        f"Requested style {requested_style_name} is not"
                        f"defined for layer {dataset.name}"
                    )

            logging.debug(f"Set style for layer to: {qsl_job_layer.style.name}")
            if isinstance(dataset, VectorDataSet) and filters:
                # since we will use this in the on a plain
                # list of layers, the largest extent buffer
                # should be applied
                qsl_job_layer.filter = OgcFilter110(definition=filters[index])
            job.layers.append(qsl_job_layer)
        logging.debug(f"Job prepared successfully: {job}")
        return job
