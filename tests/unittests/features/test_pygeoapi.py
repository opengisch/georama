from types import SimpleNamespace

import psycopg2
import pytest
from psycopg2.extensions import make_dsn, parse_dsn
from pygeoapi.provider import sql
from qgis_server_light.interface.exporter.extract import Crs, DataSource, PostgresSource

from georama.features.pygeoapi_providers.sql import GeoramaSqlProvider
from georama.features.views.pygeoapi import PygeoapiServer


class ConnectionInterceptedError(Exception):
    pass


def postgres_source(**kwargs) -> PostgresSource:
    return PostgresSource(
        key="id", table="my_table", schema="my_schema", geometry_column="geom", **kwargs
    )


def feature_layer(source: PostgresSource) -> SimpleNamespace:
    return SimpleNamespace(
        datasource=SimpleNamespace(
            source_to_qsl=DataSource(postgres=source),
            crs_to_qsl=Crs(
                auth_id="EPSG:2056", ogc_uri="http://www.opengis.net/def/crs/EPSG/0/2056"
            ),
            geometry_type_wkb="Point",
        )
    )


def create_provider_definition(source: PostgresSource) -> dict:
    return PygeoapiServer().create_postgres_provider(feature_layer(source), False, [])


@pytest.fixture
def captured_dsn(monkeypatch):
    """Replaces psycopg2.connect to capture the connection string libpq would receive,
    without connecting to any database.
    """
    captured = {}

    def fake_connect(dsn=None, **kwargs):
        captured.update(parse_dsn(make_dsn(dsn, **kwargs)))
        raise ConnectionInterceptedError()

    monkeypatch.setattr(psycopg2, "connect", fake_connect)
    sql.get_engine.cache_clear()
    yield captured
    sql.get_engine.cache_clear()


def connect(source: PostgresSource, captured_dsn: dict) -> dict:
    with pytest.raises(ConnectionInterceptedError):
        GeoramaSqlProvider(create_provider_definition(source))
    return captured_dsn


class TestCreatePostgresProviderConnection:
    """Checks the connection parameters libpq receives once the provider definition went
    through pygeoapi, SQLAlchemy and psycopg2.
    """

    def test_service_only_lets_libpq_resolve_everything(self, captured_dsn):
        dsn = connect(postgres_source(service="my_service"), captured_dsn)
        assert dsn["service"] == "my_service"
        for key in ("host", "port", "dbname", "user", "password", "sslmode"):
            assert key not in dsn

    def test_service_with_project_values_overrides_service(self, captured_dsn):
        dsn = connect(
            postgres_source(
                service="my_service",
                port=6543,
                username="other_user",
                sslmode=3,
                ssl_mode_text="require",
            ),
            captured_dsn,
        )
        assert dsn["service"] == "my_service"
        assert dsn["port"] == "6543"
        assert dsn["user"] == "other_user"
        assert dsn["sslmode"] == "require"
        assert "host" not in dsn
        assert "password" not in dsn

    def test_credentials_are_passed_to_libpq(self, captured_dsn):
        dsn = connect(
            postgres_source(
                host="db",
                port=5433,
                dbname="gis",
                username="user",
                password="secret",
                sslmode=0,
                ssl_mode_text="prefer",
            ),
            captured_dsn,
        )
        assert dsn["host"] == "db"
        assert dsn["port"] == "5433"
        assert dsn["dbname"] == "gis"
        assert dsn["user"] == "user"
        assert dsn["password"] == "secret"
        assert dsn["sslmode"] == "prefer"
        assert "service" not in dsn

    def test_credentials_without_port_use_default_port(self, captured_dsn):
        dsn = connect(postgres_source(host="db", dbname="gis", username="user"), captured_dsn)
        assert dsn["port"] == "5432"
