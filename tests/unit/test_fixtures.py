"""Guards the shared fixtures: a broken fixture makes every test built on it meaningless."""

from pathlib import Path

import pytest
from django.conf import settings
from django.db import connection

from tests.fixtures.gis import GIS_SCHEMA


@pytest.mark.django_db
def test_postgis_data_is_in_the_test_database(db_connection, global_postgis_vector):
    with connection.cursor() as cur:
        cur.execute("SELECT current_database()")
        django_database = cur.fetchone()[0]
    assert db_connection.execute("SELECT current_database()").fetchone()[0] == django_database
    assert global_postgis_vector.source["postgres"]["dbname"] == django_database


@pytest.mark.django_db
def test_global_vector_matches_its_table(db_connection, global_postgis_vector):
    postgres = global_postgis_vector.source["postgres"]
    columns = [
        row[0]
        for row in db_connection.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_schema = %s AND table_name = %s ORDER BY ordinal_position",
            (GIS_SCHEMA, postgres["table"]),
        )
    ]
    fields = {field.name for field in global_postgis_vector.fields.all()}
    assert columns[:2] == ["id", postgres["geometry_column"]]
    assert set(columns[2:]) == fields
    count = db_connection.execute(f"SELECT count(*) FROM {GIS_SCHEMA}.{postgres['table']}")
    assert count.fetchone()[0] == 10


@pytest.mark.django_db
def test_global_vector_is_the_same_in_every_run(global_vector):
    assert global_vector.name == "cities"
    assert global_vector.source["postgres"]["geometry_column"] == "geom"
    assert {field.name for field in global_vector.fields.all()} == {
        "name",
        "visited",
        "distance",
        "video",
    }


def test_data_integration_root_is_temporary(tmp_path):
    root = Path(settings.DATA_INTEGRATION_ROOT)
    assert root.is_relative_to(tmp_path)
    assert (root / settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER).is_dir()


@pytest.mark.django_db
def test_organisation_folder_is_created_in_the_temporary_root(tmp_path, organisation):
    assert (Path(settings.DATA_INTEGRATION_ROOT) / organisation.domain).is_dir()


@pytest.mark.django_db
def test_testmandant_layers_share_the_project(
    testmandant_folder, testmandant_wms_layer, testmandant_feature_layer
):
    vector = testmandant_wms_layer.datasource
    assert testmandant_feature_layer.datasource.pk == vector.pk
    project_file = testmandant_folder.parent / vector.project.path
    assert project_file.is_file()
    assert (project_file.parent / vector.source["ogr"]["path"]).is_file()
