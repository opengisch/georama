from io import BytesIO

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from PIL import Image
from qgis_server_light.interface.job import JobResult

from georama.data_integration.models import Project
from georama.data_integration.views import RegisterQgisProject
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation

collect_ignore_glob = ["src/georama/maps/interfaces/*"]


@pytest.fixture
def admin_user_name():
    yield "admin"


@pytest.fixture
def admin_password():
    yield "admin"


@pytest.fixture
def admin_email():
    yield "admin@example.org"


@pytest.fixture()
def admin_user(db, admin_user_name, admin_password, admin_email):
    admin = User.objects.create_superuser(admin_user_name, admin_email, admin_password)
    admin.save()
    yield admin
    admin.delete()


@pytest.fixture()
def example_users():
    call_command("loaddata", "tests/resources/users.json")


@pytest.fixture
def projects_dir(settings):
    settings.DATA_INTEGRATION_ROOT = "./tests/resources/projects"
    yield


@pytest.fixture
def integrated_project(projects_dir):
    mandant_name = "TestMandant"
    project_name = "TestProject"

    view = RegisterQgisProject()
    qgis_project, project_config = view.load_project_config(mandant_name, project_name)
    view.integrate_project(qgis_project, project_config, mandant_name)
    project = Project.objects.get(hash=qgis_project.hash)
    return project


@pytest.fixture
def empty_png_bytes_job_result() -> JobResult:
    """

    Args:
        width: in pixels
        height: in pixels

    Returns:
        The image buffer
    """
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    buf = BytesIO()
    img.save(buf, format="PNG")

    return JobResult(
        data=buf.getvalue(),
        content_type="image/png",
    )


@pytest.fixture
def wfs_op() -> WfsOperation:
    return WfsOperation(
        appname="maps",
        url="http://localhost:4242/maps?",
        user=None,
        model=PublishedAsWms,
    )
