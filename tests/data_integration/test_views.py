from datetime import datetime

import pytest
from qgis_server_light.interface.qgis import Crs, DataSource, OgrSource

from georama.data_integration.models import Project

pytestmark = pytest.mark.django_db


class TestDataIntegrationViews:
    def test_register_qgis_project_view(
        self, client, projects_dir, admin_user_name, admin_password
    ):
        client.login(username=admin_user_name, password=admin_password)

        project_path = "TestMandant/TestProject"
        response = client.get(
            f"/data_integrationregister_qgis_project/{project_path}",
            follow=True,
        )
        assert response.status_code == 200
        assert response.redirect_chain == [
            ("/admin/data_integration/project/", 302),
        ]

        assert b"TestProject" in response.content
        assert Project.objects.filter(name="TestProject").exists()

        project = Project.objects.get(name="TestProject")
        assert isinstance(project.id, int)
        assert project.name == "TestProject"
        assert project.mandant.name == "TestMandant"
        assert project.title == ""
        assert project.version == ""

        # TODO: Should use a static UUID generator for this
        assert isinstance(project.hash, str)

        # TODO: Should use time freezing lib like freezegun for this
        assert isinstance(project.integration_date, datetime)

        vector_datasets = project.vector_datasets.all()
        assert len(vector_datasets) == 1

        point_layer = vector_datasets[0]

        assert isinstance(point_layer.id, int)
        assert point_layer.title == "TestPointLayer"
        assert point_layer.name.startswith("TestPointLayer_")
        assert point_layer.qgis_layer_id.startswith("TestPointLayer_")

        datasource, path = point_layer.source_to_qsl
        assert path == "TestMandant/data/TestPointLayer.gpkg|layername=TestPointLayer"
        assert datasource == DataSource(
            ogr=OgrSource(
                path="data/TestPointLayer.gpkg",
                layer_name="TestPointLayer",
            ),
        )

        assert point_layer.crs_to_qsl == Crs(
            auth_id="EPSG:4326",
            postgis_srid=4326,
            ogc_uri="http://www.opengis.net/def/crs/EPSG/0/4326",
            ogc_urn="urn:ogc:def:crs:EPSG::4326",
        )

        # TODO: We might want to also compare point_layer.to_qsl to a Vector()
        # dataclass instance here. But because it contains so much highly
        # variable data, we first need a helper function to compare only a
        # *subset* of a dataclass instance to another, so that we can write
        # decent assertions that aren"t brittle.
