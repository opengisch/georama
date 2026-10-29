"""PostGIS data, created in the test database of pytest-django."""

import random
from importlib import import_module

import psycopg
import pytest
from django.db import connection
from faker import Faker
from faker.utils.loading import find_available_providers

from georama.core.common.faker.gis import Dataset
from georama.integration.builders import create_dataset_table, create_vector_from_dataset
from tests.fixtures import SEED

GIS_SCHEMA = "test_data"


@pytest.fixture(scope="session")
def gis_db_settings(django_db_setup) -> dict:
    """Connection settings of the test database (one per xdist worker), as passed to
    `psycopg.connect`. `django_db_setup` has renamed the database at this point.
    """
    settings_dict = connection.settings_dict
    return {
        "host": settings_dict["HOST"],
        "port": settings_dict["PORT"],
        "dbname": settings_dict["NAME"],
        "user": settings_dict["USER"],
        "password": settings_dict["PASSWORD"],
    }


@pytest.fixture
def db_connection(gis_db_settings):
    with psycopg.connect(**gis_db_settings) as conn:
        yield conn


@pytest.fixture(scope="session")
def gis_faker() -> Faker:
    providers = find_available_providers([import_module("georama.core.common.faker")])
    return Faker(locale="de_CH", providers=providers)


@pytest.fixture(scope="session")
def gis_dataset_definition(gis_faker) -> Dataset:
    """The dataset of the global vector, identical in every run.

    It seeds on its own: session fixtures run before the autouse seeding fixture.
    """
    random.seed(SEED)
    Faker.seed(SEED)
    return gis_faker.vector_dataset(
        GIS_SCHEMA,
        min_records=10,
        max_records=10,
        schema_name="cities",
        field_names=["name", "visited", "distance", "video"],
        geometry_field_name="geom",
    )


@pytest.fixture(scope="session")
def gis_dataset(gis_db_settings, gis_dataset_definition) -> Dataset:
    """The dataset with its table, shared by all tests: they must only read it."""
    with psycopg.connect(**gis_db_settings) as conn, conn.cursor() as cur:
        # a crashed run may have left the schema behind with --reuse-db
        cur.execute(f"DROP SCHEMA IF EXISTS {GIS_SCHEMA} CASCADE;")
        cur.execute(f"CREATE SCHEMA {GIS_SCHEMA};")
        create_dataset_table(cur, gis_dataset_definition)
    yield gis_dataset_definition
    with psycopg.connect(**gis_db_settings) as conn:
        conn.execute(f"DROP SCHEMA IF EXISTS {GIS_SCHEMA} CASCADE;")


@pytest.fixture
def global_vector(project_global_organisation, gis_db_settings, gis_dataset_definition, gis_faker):
    """A Vector of the global organisation whose table is not guaranteed to exist: enough for
    everything built from the models (Capabilities, DescribeFeatureType, permissions, QSL jobs).
    """
    return create_vector_from_dataset(
        gis_dataset_definition,
        GIS_SCHEMA,
        gis_db_settings,
        gis_faker.bounds(),
        gis_faker.bounds_wgs84(),
        project=project_global_organisation,
    )


@pytest.fixture
def global_postgis_vector(gis_dataset, global_vector):
    """The global Vector backed by its table, for what reads the data (OGC API Features)."""
    return global_vector
