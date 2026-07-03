from pathlib import Path
from uuid import uuid4

import pytest
from django.conf import settings


@pytest.fixture
def organisation_a_folder():
    orga_path = Path(settings.DATA_INTEGRATION_ROOT) / str(uuid4())
    orga_path.mkdir()
    yield orga_path
    orga_path.rmdir()


@pytest.fixture
def organisation_b_folder():
    orga_path = Path(settings.DATA_INTEGRATION_ROOT) / str(uuid4())
    orga_path.mkdir()
    yield orga_path
    orga_path.rmdir()


@pytest.fixture
def orga_a_project_file(organisation_a_folder):
    project_path = organisation_a_folder / "test.qgs"
    project_path.touch()
    yield project_path
    project_path.unlink()


@pytest.fixture
def orga_a_project_random_file(orga_b_project_file):
    random_path = Path(f"{orga_b_project_file}.bak")
    random_path.touch()
    yield random_path
    random_path.unlink()


@pytest.fixture
def orga_b_project_file(organisation_b_folder):
    project_path = organisation_b_folder / "test.qgz"
    project_path.touch()
    yield project_path
    project_path.unlink()


@pytest.fixture
def orga_b_project_config_file(orga_b_project_file):
    config_path = Path(f"{orga_b_project_file}.json")
    config_path.touch()
    yield config_path
    config_path.unlink()
