from io import BytesIO
from unittest.mock import Mock

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from PIL import Image
from qgis_server_light.interface.job import JobResult
from qgis_server_light.interface.qgis import Crs
from xsdata.models.enums import FormType
from xsdata.models.xsd import (
    ComplexContent,
    ComplexType,
    Element,
    Extension,
    Import,
    Schema,
    Sequence,
)

from georama.data_integration.models import Project, VectorDataSet
from georama.data_integration.views import RegisterQgisProject
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation
from georama.maps.services.wfs_2_0_0.describe_feature_type import WfsDescribeFeatureType
from georama.maps.services.wfs_2_0_0.get_capabilities import WfsGetCapabilities
from georama.maps.services.wfs_2_0_0.get_metadata import WfsGetMetadata

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


@pytest.fixture
def wfs_desc_ft() -> WfsDescribeFeatureType:
    return WfsDescribeFeatureType(
        appname="maps",
        url="http://localhost:4242/maps?",
        user=None,
        model=PublishedAsWms,
    )


@pytest.fixture
def wfs_get_cap() -> WfsGetCapabilities:
    return WfsGetCapabilities(
        appname="maps",
        url="http://localhost:4242/maps?",
        user=None,
        model=PublishedAsWms,
    )


@pytest.fixture
def wfs_get_metadata() -> WfsGetMetadata:
    return WfsGetMetadata(
        appname="maps",
        url="http://localhost:4242/maps?",
        user=None,
        model=PublishedAsWms,
    )


@pytest.fixture
def described_feature_type() -> Schema:
    return Schema(
        imports=[
            Import(
                schema_location="http://schemas.opengis.net/gml/3.2.1/gml.xsd",
                namespace="http://www.opengis.net/gml/3.2",
            )
        ],
        target_namespace="https://www.opengis.ch/georama",
        element_form_default=FormType.QUALIFIED,
        version="0.1",
        elements=[
            Element(
                name="mylayer",
                type="georama:mylayerType",
                substitution_group="gml:AbstractFeature",
            )
        ],
        complex_types=[
            ComplexType(
                name="mylayerType",
                complex_content=ComplexContent(
                    extension=Extension(
                        base="gml:AbstractFeatureType",
                        sequence=Sequence(
                            elements=[
                                Element(
                                    name="geometry",
                                    type="gml:GeometryPropertyType",
                                    min_occurs=0,
                                    max_occurs=1,
                                ),
                                Element(
                                    name="required_long",
                                    type="long",
                                    min_occurs=1,
                                    max_occurs=1,
                                    nillable=False,
                                ),
                                Element(
                                    name="optional_string",
                                    type="string",
                                    min_occurs=0,
                                    max_occurs=1,
                                    nillable=True,
                                ),
                            ]
                        ),
                    )
                ),
            )
        ],
    )


@pytest.fixture
def mock_dataset() -> tuple[Mock, str]:
    extent = ",".join(
        [
            "6.2305498123169",
            "46.0072288513184",
            "10.2997055053711",
            "47.7490196228027",
        ]
    )

    dataset = Mock(
        spec=VectorDataSet,
        crs_to_qsl=Crs(
            auth_id="EPSG:4326",
            postgis_srid=4326,
            ogc_uri="http://www.opengis.net/def/crs/EPSG/0/4326",
            ogc_urn="urn:ogc:def:crs:EPSG::4326",
        ),
        bbox_wgs84=extent,
    )
    return dataset, extent


@pytest.fixture
def mock_layer(mock_dataset) -> Mock:
    layer_name = "TestPointLayer_1234_5678"
    dataset, extent = mock_dataset

    layer = Mock(
        spec=PublishedAsWms,
        title="TestPointLayer",
        bound_dataset=dataset,
        description="This is a test layer.",
        extent=extent,
    )
    layer.configure_mock(**{"name": layer_name})
    return layer
