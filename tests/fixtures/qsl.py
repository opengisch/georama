"""QSL is mocked at its boundary: the redis queue."""

import pytest
from qgis_server_light.interface.common import Crs
from qgis_server_light.interface.dispatcher.common import Status
from qgis_server_light.interface.job.common.input import QslJobLayer
from qgis_server_light.interface.job.common.output import JobResult

from georama.maps.apps import qsl_redis_queue
from georama.maps.maps_config import Config


@pytest.fixture
def crs_factory():
    """Creates crs as QSL resolves them, `None` creates a crs without identifiers."""

    def create_crs(code: int | None, axis_inverted: bool = False) -> Crs:
        if code is None:
            return Crs()
        return Crs(
            auth_id=f"EPSG:{code}",
            postgis_srid=code,
            ogc_uri=f"http://www.opengis.net/def/crs/EPSG/0/{code}",
            ogc_urn=f"urn:ogc:def:crs:EPSG::{code}",
            axis_inverted=axis_inverted,
        )

    yield create_crs


@pytest.fixture(autouse=True)
def resolved_other_crs(crs_factory):
    """The other crs are resolved by QSL at runtime, which is not available in tests."""
    other_crs = [crs_factory(3857), crs_factory(4326, axis_inverted=True)]
    Config.resolved_other_crs.update({"maps": other_crs, "webgis": other_crs})
    yield Config.resolved_other_crs
    Config.resolved_other_crs.clear()


@pytest.fixture
def posted_jobs(monkeypatch):
    """Replaces the queue, the answer is set by the test via `posted_jobs.answer`."""

    class PostedJobs(list):
        answer: tuple[JobResult, str]

    jobs = PostedJobs()

    async def post(job_parameter, timeout):
        jobs.append(job_parameter)
        return jobs.answer

    monkeypatch.setattr(qsl_redis_queue, "post", post)
    yield jobs


@pytest.fixture
def render_job_result():
    """Answer of QSL for render jobs, see `posted_jobs`."""
    yield JobResult(id="job", data=b"png", content_type="image/png"), Status.SUCCESS.value


@pytest.fixture
def qsl_job_layer():
    yield QslJobLayer(
        id="layer", name="layer", source="{}", remote=True, folder_name="", driver="wms"
    )
