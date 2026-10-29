import pytest
from asgiref.sync import async_to_sync
from httpx import RequestError
from qgis_server_light.interface.common import BBox, Crs
from qgis_server_light.interface.dispatcher.common import Status
from qgis_server_light.interface.job.common.output import JobResult
from qgis_server_light.interface.job.crs.input import QslJobParameterCrs
from qgis_server_light.interface.job.crs.output import CrsCollection
from qgis_server_light.interface.job.render.input import QslJobParameterRender
from xsdata.formats.dataclass.serializers import DictEncoder, JsonSerializer

from georama.integration.models import Vector
from georama.maps.adapter import qsl
from georama.maps.exception.job import JobExecutionError
from georama.maps.maps_config import Config
from georama.maps.models import WmsLayer


def crs_job_result(crs: list, status: str = Status.SUCCESS.value) -> tuple[JobResult, str]:
    data = JsonSerializer().render(CrsCollection(crs=crs)).encode()
    return JobResult(id="job", data=data, content_type="application/json"), status


@pytest.fixture
def wms_layer(qsl_job_layer, monkeypatch):
    crs = Crs(auth_id="EPSG:4326", axis_inverted=True)
    wms_layer = WmsLayer(
        datasource=Vector(crs=DictEncoder().encode(crs)), extent="5.9,45.8,10.5,47.8"
    )
    # the job layer needs the project of the datasource from the DB
    monkeypatch.setattr(wms_layer, "to_qsl_job_layer", lambda: qsl_job_layer)
    yield wms_layer


@pytest.fixture
def bbox():
    yield BBox.from_string("2457000,1075000,2862000,1296000")


class TestRenderImage:
    def test_rendered_through_qsl(
        self, posted_jobs, render_job_result, qsl_job_layer, wms_layer, bbox
    ):
        posted_jobs.answer = render_job_result

        image = async_to_sync(qsl.render_image)(wms_layer, bbox, "EPSG:2056", 220, 120)

        assert image == b"png"
        assert posted_jobs == [
            QslJobParameterRender(
                layers=[qsl_job_layer],
                bbox=bbox,
                crs="EPSG:2056",
                width=220,
                height=120,
                dpi=72,
            )
        ]

    @pytest.mark.parametrize(
        "render_job_result",
        [(JobResult(id="job", data="error", content_type="text/plain"), Status.FAILURE.value)],
    )
    def test_failure(self, posted_jobs, render_job_result, wms_layer, bbox):
        posted_jobs.answer = render_job_result

        with pytest.raises(RequestError):
            async_to_sync(qsl.render_image)(wms_layer, bbox, "EPSG:2056", 220, 120)


class TestGeneratePreviewImage:
    def test_layer_extent_in_axis_order(self, posted_jobs, render_job_result, wms_layer):
        posted_jobs.answer = render_job_result

        assert async_to_sync(qsl.generate_preview_image)(wms_layer) == b"png"
        [job] = posted_jobs
        assert job.bbox.to_2d_list() == [45.8, 5.9, 47.8, 10.5]
        assert job.crs == "EPSG:4326"
        assert (job.width, job.height) == wms_layer.preview_dimensions


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
