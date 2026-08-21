import logging

from qgis_server_light.interface.job.legend.input import QslJobParameterLegend

from georama.maps.interfaces.georama.requests import GetLegendGraphicRequestParams
from georama.maps.services.wms_1_3_0 import WmsOperation


class WmsGetLegendGraphic(WmsOperation):
    default_style_name = "default"

    def __init__(self, appname: str, url: str, user, model):
        super().__init__(appname, url, user, model)

    def prepare_job_content(
        self, service_params: GetLegendGraphicRequestParams
    ) -> QslJobParameterLegend:
        accessible_published_as = self.obtain_accessible_layers(service_params.layer_list)

        if service_params.DPI:
            dpi = service_params.DPI
        elif service_params.FORMAT_OPTIONS and ":" in service_params.FORMAT_OPTIONS:
            dpi = int(service_params.FORMAT_OPTIONS.split(":")[-1])
        else:
            dpi = None

        job = QslJobParameterLegend(
            layers=[],
            width=service_params.WIDTH,
            height=service_params.HEIGHT,
            dpi=dpi,
            format=service_params.FORMAT,
            layer_title=service_params.LAYERTITLE,
            scale=service_params.SCALE,
        )

        for published_as, requested_style_name in zip(
            accessible_published_as,
            service_params.style_list,
            strict=True,
        ):
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
            job.layers.append(qsl_job_layer)

        logging.debug(f"Legend job prepared successfully: {job}")
        return job
