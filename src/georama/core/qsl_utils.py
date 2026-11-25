"""Utilities for QSL (QGIS Server Light) operations."""

import logging

from httpx import RequestError
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.dispatcher.common import Status
from qgis_server_light.interface.job.common.input import QslJobLayer
from qgis_server_light.interface.job.render.input import QslJobParameterRender

from georama.maps.apps import qsl_redis_queue
from georama.maps.maps_config import Config


async def render_image(
    qsl_layers: list[QslJobLayer],
    bbox: BBox,
    crs: str,
    width: int,
    height: int,
) -> bytes | None:
    """Renders a png through QSL.

    Args:
        qsl_layers: The QSL job layers to render.
        bbox: The extent to render, in the axis order of `crs`.
        crs: The auth id of the crs to render in, e.g. `EPSG:2056`.
        width: The width of the image in pixel.
        height: The height of the image in pixel.

    Returns:
        The png or `None` if the job could not be created.

    Raises:
        RequestError: In case QSL did not render the image successfully.
    """
    # this way we always set a style, or it will fail if list has no styles
    # we could make that configurable in admin gui easily
    get_map_job = QslJobParameterRender(
        bbox=bbox,
        crs=crs,
        width=width,
        height=height,
        dpi=72,
        format="image/png",
        layers=qsl_layers,
    )
    try:
        result_tuple = await qsl_redis_queue.post(get_map_job, Config().job_timeout)
        result, status = result_tuple
        if status == Status.SUCCESS.value:
            return result.data
        else:
            logging.error(
                f"Preview image generation through QSL was not successful. "
                f"Status: {status} Result: {result}"
            )
            raise RequestError(
                f"The request to QSL returned non successful. Status: {status}, "
                f"Reason: {result.data}"
            )
    except ValueError as e:
        logging.exception(f"Error while generating preview image: {e}")
    except PermissionError as e:
        logging.exception(f"Permission error while generating preview image: {e}")
    return None
