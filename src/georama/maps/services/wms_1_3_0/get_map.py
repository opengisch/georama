import logging

from qgis_server_light.interface.job import QslGetMapJob, WmsGetMapParams
from qgis_server_light.interface.qgis import Custom, Raster, Vector

from georama.maps.services.wms_1_3_0 import WmsOperation


class WmsGetMap(WmsOperation):
    default_style_name = "default"

    def __init__(self, appname: str, url: str, user):
        super().__init__(appname, url, user)

    def prepare_job_content(self, service_params: WmsGetMapParams) -> QslGetMapJob | str:
        if not service_params.styles:
            logging.debug(
                "No styles were passed to the request, so we apply the default styles to all layers"
            )
            styles = [self.default_style_name] * len(service_params.layers)
        else:
            logging.debug("There were styles in the request. Processing them further...")
            styles = service_params.styles
            if len(styles) != len(service_params.layers):
                logging.debug(
                    "Layer and Style in query param are of different length. We stop here."
                )
                raise ValueError(
                    "Each passed layer needs a corresponding style (comma separated lists need to be of same length)."
                )
        for index, style in enumerate(styles.copy()):
            if style == "":
                styles[index] = self.default_style_name
        # finally we set the styles to the parameter to pass them to QSL
        service_params.STYLES = ",".join(styles)
        # we pass the requested layers to filter DB objects
        accessible_published_as = self.obtain_accessible_layers(service_params.layers)

        job = QslGetMapJob(
            # we set the extent buffer to zero, this is used to control rendering issues like
            # https://github.com/qgis/QGIS/issues/30251
            extent_buffer=0.0,
            service_params=service_params,
            raster_layers=[],
            vector_layers=[],
            custom_layers=[],
        )
        for index, published_as in enumerate(accessible_published_as):
            dataset = published_as.bound_dataset
            qsl_instance = dataset.to_qsl
            if isinstance(qsl_instance, Raster):
                job.raster_layers.append(qsl_instance)
            elif isinstance(qsl_instance, Vector):
                # since we will use this in the on a plain list of layers, the largest extent buffer
                # should be applied
                if published_as.extent_buffer > job.extent_buffer:
                    job.extent_buffer = published_as.extent_buffer
                job.vector_layers.append(qsl_instance)
            elif isinstance(qsl_instance, Custom):
                job.custom_layers.append(qsl_instance)
            else:
                logging.error(f"Found a QSL instance which is not expected! {qsl_instance}")
        return job
