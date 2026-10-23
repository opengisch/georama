import pytest
from asgiref.sync import async_to_sync
from qgis_server_light.interface.dispatcher.common import Status
from qgis_server_light.interface.job.common.output import JobResult
from qgis_server_light.interface.job.crs.input import QslJobParameterCrs
from qgis_server_light.interface.job.crs.output import CrsCollection
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.maps.adapter import qsl
from georama.maps.exception.job import JobExecutionError
from georama.maps.maps_config import Config


@pytest.fixture
def posted_jobs(monkeypatch):
    """Replaces the queue, the answer is set by the test via `posted_jobs.answer`."""

    class PostedJobs(list):
        answer: tuple[JobResult, str]

    jobs = PostedJobs()

    async def post(job_parameter, timeout):
        jobs.append(job_parameter)
        return jobs.answer

    monkeypatch.setattr(qsl.qsl_redis_queue, "post", post)
    yield jobs


def crs_job_result(crs: list, status: str = Status.SUCCESS.value) -> tuple[JobResult, str]:
    data = JsonSerializer().render(CrsCollection(crs=crs)).encode()
    return JobResult(id="job", data=data, content_type="application/json"), status


class TestResolveOtherCrs:
    def test_resolved_through_qsl_and_cached(self, settings, posted_jobs, crs_factory):
        del Config.resolved_other_crs["maps"]
        settings.MAPS_OGC_OTHER_CRS = ["EPSG:4326", "urn:ogc:def:crs:EPSG::4326", "EPSG:3857"]
        crs_4326 = crs_factory(4326, axis_inverted=True)
        posted_jobs.answer = crs_job_result([crs_4326, crs_4326, crs_factory(3857)])

        other_crs = async_to_sync(qsl.resolve_other_crs)("maps")
        async_to_sync(qsl.resolve_other_crs)("maps")

        assert [crs.auth_id for crs in other_crs] == ["EPSG:4326", "EPSG:3857"]
        assert other_crs[0].axis_inverted is True
        assert Config().other_crs("maps") == other_crs
        assert posted_jobs == [QslJobParameterCrs(identifiers=settings.MAPS_OGC_OTHER_CRS)]

    def test_failure(self, settings, posted_jobs):
        del Config.resolved_other_crs["maps"]
        settings.MAPS_OGC_OTHER_CRS = ["EPSG:999999"]
        posted_jobs.answer = crs_job_result([], Status.FAILURE.value)

        with pytest.raises(JobExecutionError, match="EPSG:999999"):
            async_to_sync(qsl.resolve_other_crs)("maps")
        assert "maps" not in Config.resolved_other_crs

    def test_nothing_configured(self, settings, posted_jobs):
        del Config.resolved_other_crs["webgis"]
        settings.WEBGIS_OGC_OTHER_CRS = []

        assert async_to_sync(qsl.resolve_other_crs)("webgis") == []
        assert posted_jobs == []
