import logging

from qgis_server_light.interface.job.input import QslJobParameterMap

from georama.maps.interfaces.georama.requests import QslGetMapRequest
from georama.maps.services.wms_1_3_0 import WmsOperation


class WmsGetMap(WmsOperation):
    default_style_name = "default"

    def __init__(self, appname: str, url: str, user, model):
        super().__init__(appname, url, user, model)

    def prepare_job_content(
        self, service_params: QslGetMapRequest
    ) -> QslJobParameterMap | str:
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

        job = QslJobParameterMap(
            # we set the extent buffer to zero, this is used to
            # control rendering issues like
            # https://github.com/qgis/QGIS/issues/30251
            extent_buffer=0.0,
            bbox=service_params.BBOX,
            crs=service_params.CRS,
            width=str(service_params.WIDTH),
            height=str(service_params.HEIGHT),
            dpi=int(dpi),
            format=service_params.FORMAT,
            layers=[],
        )
        styles = service_params.style_list
        filters = service_params.filter_list
        for index, published_as in enumerate(accessible_published_as):
            requested_style_name = styles[index]
            dataset = published_as.bound_dataset
            qsl_instance = dataset.to_qsl
            qsl_instance.style_name = requested_style_name
            matched_style = qsl_instance.get_style_by_name(qsl_instance.style_name)
            if matched_style is None:
                if requested_style_name == "default":
                    logging.debug(
                        f"Requested style name for layer '{qsl_instance.name}'"
                        f"was {qsl_instance.style_name} "
                        f"but this is not in the available styles,"
                        f"we choose the first available style "
                        f"instead which is '{qsl_instance.styles[0].name}'"
                    )
                    qsl_instance.style_name = qsl_instance.styles[0].name
                else:
                    raise ValueError(
                        f"Requested style {requested_style_name} is not"
                        f"defined for layer {qsl_instance.name}"
                    )

            logging.debug(f"Set style for layer to: {qsl_instance.style_name}")
            if isinstance(qsl_instance, Raster):
                job.raster_layers.append(qsl_instance)
            elif isinstance(qsl_instance, Vector):
                # since we will use this in the on a plain
                # list of layers, the largest extent buffer
                # should be applied
                if published_as.extent_buffer > job.extent_buffer:
                    job.extent_buffer = published_as.extent_buffer
                if filters:
                    qsl_instance.filter = OgcFilter110(definition=filters[index])
                job.vector_layers.append(qsl_instance)
            elif isinstance(qsl_instance, Custom):
                job.custom_layers.append(qsl_instance)
            else:
                logging.error(f"Found a QSL instance which is not expected! {qsl_instance}")
        logging.debug(f"Job prepared successfully: {job}")
        return job
