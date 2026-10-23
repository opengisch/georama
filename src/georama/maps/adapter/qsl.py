import logging
from pathlib import Path

import httpx
from asgiref.sync import sync_to_async
from django.conf import settings
from httpx import RequestError
from httpx._models import Response as HttpxResponse
from qgis_server_light.interface.common import BBox, Crs
from qgis_server_light.interface.dispatcher.common import Status
from qgis_server_light.interface.exporter.api import ExportParameters
from qgis_server_light.interface.job.crs.input import QslJobParameterCrs
from qgis_server_light.interface.job.crs.output import CrsCollection
from qgis_server_light.interface.job.render.input import QslJobParameterRender
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.maps.apps import qsl_redis_queue
from georama.maps.exception.job import JobExecutionError
from georama.maps.maps_config import Config
from georama.maps.models import WmsLayer


async def call_qsl_exporter(path: Path) -> HttpxResponse:
    url = settings.QSL_EXPORTER_URL
    async with httpx.AsyncClient() as client:
        logging.debug(f"Sending export request to {url}")
        r = await client.post(
            url,
            json=JsonSerializer().render(
                ExportParameters(
                    str(path),
                    output_format="json",
                )
            ),
            headers={"Content-Type": "application/json"},
            timeout=None,
        )
        return r


async def generate_preview_image(wms_layer: WmsLayer) -> bytes | None:
    # We have to call the following @properties a bit awkward because
    # they contain sync django orm actions
    datasource = await sync_to_async(lambda: wms_layer.get_datasource)()
    qsl_job_layer = await sync_to_async(wms_layer.to_qsl_job_layer)()
    # this way we always set a style, or it will fail if list has no styles
    # we could make that configurable in admin gui easily
    get_map_job = QslJobParameterRender(
        bbox=BBox.from_string(wms_layer.extent),
        crs=datasource.crs_to_qsl.auth_id,
        width=wms_layer.preview_dimensions[0],
        height=wms_layer.preview_dimensions[1],
        dpi=72,
        format="image/png",
        layers=[qsl_job_layer],
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
            raise RequestError(f"The request to QSL returned non successful. Status: {status}")
    except ValueError as e:
        logging.exception(f"Error while generating preview image: {e}")
    except PermissionError as e:
        logging.exception(f"Permission error while generating preview image: {e}")
    return None


async def resolve_other_crs(appname: str) -> list[Crs]:
    """
    Resolves the crs configured for the OGC services of an app through QSL, so georama
    gets the full crs information (identifiers, axis order) without own crs knowledge.
    The result is cached per process in `Config.resolved_other_crs`.

    Args:
        appname: The simple name of the app, e.g. `maps` or `webgis`.

    Returns:
        The resolved crs without duplicates, in the configured order.

    Raises:
        JobExecutionError: In case QSL could not resolve the configured crs.
    """
    config = Config()
    if appname in config.resolved_other_crs:
        return config.resolved_other_crs[appname]
    identifiers = config.other_crs_identifiers(appname)
    other_crs = []
    if identifiers:
        result, status = await qsl_redis_queue.post(
            QslJobParameterCrs(identifiers=identifiers), config.job_timeout
        )
        if status != Status.SUCCESS.value:
            raise JobExecutionError(
                f"Resolving the configured crs {identifiers} of the app {appname} failed",
                job_id=result.id,
            )
        for crs in JsonParser().from_bytes(result.data, CrsCollection).crs:
            if crs not in other_crs:
                other_crs.append(crs)
    config.resolved_other_crs[appname] = other_crs
    return other_crs
