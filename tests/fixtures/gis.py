"""PostGIS data, created in the test database of pytest-django."""

from importlib import import_module
from typing import NamedTuple

import psycopg
import pytest
from django.db import connection
from faker import Faker
from faker.utils.loading import find_available_providers

from georama.core.common.faker.gis import Dataset
from georama.core.models.organisation import Organisation
from georama.integration.builders import create_dataset_table, create_vector_from_dataset
from georama.integration.factories import ProjectFactory
from georama.integration.models import Project, Vector
from tests.fixtures import reseed

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
    reseed()
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


class Gis(NamedTuple):
    """The dataset with its table, and what creates the Vectors reading it."""

    dataset: Dataset
    db_settings: dict
    faker: Faker

    def create_vector(self, project: Project) -> Vector:
        return create_vector(project, self.dataset, self.db_settings, self.faker)

    def first_feature_id(self, vector: Vector) -> str:
        """The id of a feature of the table of `vector`."""
        table = vector.source["postgres"]["table"]
        with psycopg.connect(**self.db_settings) as conn:
            return str(conn.execute(f"SELECT id FROM {GIS_SCHEMA}.{table} LIMIT 1").fetchone()[0])


@pytest.fixture(scope="session")
def gis(gis_dataset, gis_db_settings, gis_faker) -> Gis:
    return Gis(gis_dataset, gis_db_settings, gis_faker)


def create_project(organisation: Organisation | None = None) -> Project:
    """A project of `organisation`, None for the global one."""
    path = f"{organisation.domain}/Project.qgz" if organisation else "Global/GlobalProject.qgz"
    return ProjectFactory.create(organisation=organisation, path=path)


def create_vector(
    project: Project, dataset: Dataset, gis_db_settings: dict, gis_faker: Faker
) -> Vector:
    """The Vector of `dataset` in `project`, its table is created by `gis_dataset`."""
    return create_vector_from_dataset(
        dataset,
        GIS_SCHEMA,
        gis_db_settings,
        gis_faker.bounds(),
        gis_faker.bounds_wgs84(),
        project=project,
    )


@pytest.fixture
def global_vector(project_global_organisation, gis_db_settings, gis_dataset_definition, gis_faker):
    """A Vector of the global organisation whose table is not guaranteed to exist: enough for
    everything built from the models (Capabilities, DescribeFeatureType, permissions, QSL jobs).
    """
    return create_vector(
        project_global_organisation, gis_dataset_definition, gis_db_settings, gis_faker
    )


@pytest.fixture
def global_postgis_vector(gis_dataset, global_vector):
    """The global Vector backed by its table, for what reads the data (OGC API Features)."""
    return global_vector
