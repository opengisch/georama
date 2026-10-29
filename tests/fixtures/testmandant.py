"""The TestMandant project: a real QGIS project with its data, versioned in `tests/resources`."""

import shutil
from pathlib import Path

import pytest
from django.conf import settings

from georama.features.builders import create_test_feature_layer
from georama.integration.builders import create_test_point_vector, create_test_project
from georama.maps.builders import create_test_wms_layer

TEST_MANDANT_SOURCE = (
    Path(__file__).parents[1] / "resources" / "projects" / "global" / "TestMandant"
)


@pytest.fixture
def testmandant_folder() -> Path:
    """Copies TestMandant into the temporary integration root of the test."""
    target = (
        Path(settings.DATA_INTEGRATION_ROOT)
        / settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER
        / TEST_MANDANT_SOURCE.name
    )
    shutil.copytree(TEST_MANDANT_SOURCE, target)
    return target


@pytest.fixture
def testmandant_project(db):
    return create_test_project()


@pytest.fixture
def testmandant_point_vector(testmandant_project):
    return create_test_point_vector(testmandant_project)


@pytest.fixture
def testmandant_wms_layer(testmandant_point_vector):
    return create_test_wms_layer(testmandant_point_vector)


@pytest.fixture
def testmandant_feature_layer(testmandant_point_vector):
    return create_test_feature_layer(testmandant_point_vector)
