import pytest
from django.contrib.auth.models import User

import tests
from georama.data_integration.models import Project
from georama.data_integration.views import RegisterQgisProject
from tests.testing.helpers import TemporaryEnvVar, asset

ADMIN_USER = "admin"
ADMIN_PASS = "admin"
ADMIN_EMAIL = "admin@example.org"


@pytest.fixture(autouse=True)
def admin_user(db):
    admin = User.objects.create_superuser(ADMIN_USER, ADMIN_EMAIL, ADMIN_PASS)
    admin.save()
    yield admin
    admin.delete()


@pytest.fixture
def projects_dir():
    projects_dir = asset(tests, "resources/projects")
    with TemporaryEnvVar("GEORAMA_DATA_INTEGRATION_ROOT", projects_dir):
        yield


@pytest.fixture
def integrated_project(projects_dir):
    mandant_name = "TestMandant"
    project_name = "TestProject"

    view = RegisterQgisProject()
    qgis_project, project_config = view.load_project_config(
        mandant_name, project_name)
    view.integrate_project(qgis_project, project_config, mandant_name)
    project = Project.objects.get(hash=qgis_project.hash)
    return project