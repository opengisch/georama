import pytest
from asgiref.sync import async_to_sync
from django.contrib import messages
from django.contrib.messages.storage.cookie import CookieStorage
from qgis_server_light.interface.common import BBox

from georama.core.common.api import GeoramaPreviewMixin
from georama.core.qsl_utils import render_image
from georama.integration.models import Project


@pytest.fixture
def request_with_messages(rf):
    request = rf.post("/")
    request._messages = CookieStorage(request)
    yield request


@pytest.fixture
def bbox():
    yield BBox.from_string("2457000,1075000,2862000,1296000")


class TestPreviewOrWarning:
    def test_preview_is_passed_through(
        self, posted_jobs, render_job_result, qsl_job_layer, request_with_messages, bbox
    ):
        posted_jobs.answer = render_job_result

        preview = async_to_sync(GeoramaPreviewMixin.preview_or_warning)(
            request_with_messages,
            Project(name="Bern"),
            render_image([qsl_job_layer], bbox, "EPSG:2056", 250, 250),
        )

        # QSL rendered fine, so there is the png and nothing to tell the user
        assert preview == b"png"
        assert list(messages.get_messages(request_with_messages)) == []

    def test_failed_rendering_becomes_a_warning(
        self, posted_jobs, failed_render_job_result, qsl_job_layer, request_with_messages, bbox
    ):
        posted_jobs.answer = failed_render_job_result

        preview = async_to_sync(GeoramaPreviewMixin.preview_or_warning)(
            request_with_messages,
            Project(name="Bern"),
            render_image([qsl_job_layer], bbox, "EPSG:2056", 250, 250),
        )

        # QSL failed, there is no preview but the error must not leave the mixin, the
        # user gets a warning naming the entity instead
        assert preview is None
        [warning] = messages.get_messages(request_with_messages)
        assert warning.level == messages.WARNING
        assert str(warning) == "The preview of 'Bern' could not be generated."
