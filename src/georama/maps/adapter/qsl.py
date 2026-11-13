import logging
from pathlib import Path

import httpx
from asgiref.sync import sync_to_async
from django.conf import settings
from httpx._models import Response as HttpxResponse
from qgis_server_light.interface.common import Crs
from qgis_server_light.interface.dispatcher.common import Status
from qgis_server_light.interface.exporter.api import ExportParameters
from qgis_server_light.interface.job.crs.input import QslJobParameterCrs
from qgis_server_light.interface.job.crs.output import CrsCollection
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.core.qsl_utils import render_image
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
    # QSL expects the bbox in the axis order of the crs like WMS 1.3.0
    bbox = await sync_to_async(lambda: wms_layer.extent_in_axis_order)()
    qsl_layer = await sync_to_async(lambda: wms_layer.to_qsl_job_layer())()
    return await render_image(
        [qsl_layer],
        bbox,
        datasource.crs_to_qsl.auth_id,
        *wms_layer.preview_dimensions,
    )


async def resolve_other_crs(appname: str) -> list[Crs]:
    """Resolves the crs configured for the OGC services of an app through QSL, so georama
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
