import os

import pytest
from django.contrib.auth.models import User

from georama.data_integration.models import Project
from georama.data_integration.views import RegisterQgisProject

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


@pytest.fixture(autouse=True)
def admin_user(db, admin_user_name, admin_password, admin_email):
    admin = User.objects.create_superuser(admin_user_name, admin_email, admin_password)
    admin.save()
    yield admin
    admin.delete()


@pytest.fixture
def projects_dir():
    os.environ["GEORAMA_DATA_INTEGRATION_ROOT"] = "./tests/resources/projects"
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
