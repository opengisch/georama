import json
from http import HTTPStatus
from types import SimpleNamespace

import psycopg2
import pytest
from django.test import RequestFactory
from psycopg2.extensions import make_dsn, parse_dsn
from pygeoapi import l10n
from pygeoapi.provider import sql
from qgis_server_light.interface.exporter.extract import (
    Crs,
    DataSource,
    EditorWidget,
    PostgresSource,
    Range,
    Relation,
    RelationFieldPair,
    RelationReference,
    ValueMap,
    ValueMapEntry,
)
from qgis_server_light.interface.exporter.extract import Field as QslField

from georama.features.pygeoapi_providers.sql import GeoramaSqlProvider
from georama.features.references import ReferenceResolver, ReferenceTarget
from georama.features.views.pygeoapi import (
    DatasetFieldConstraints,
    PygeoapiServer,
    _NoCache,
)
from georama.integration.models import VectorField


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
            is_spatial=True,
            qgis_layer_id="my_layer_1a2b",
            # a project without export, so it has no relations
            project=SimpleNamespace(config={}),
        )
    )


def create_provider_definition(source: PostgresSource) -> dict:
    server = PygeoapiServer()
    # the connection does not depend on references, there are no layers to look them up
    server.get_reference_targets = lambda project: {}
    return server.create_postgres_provider(feature_layer(source), False, [])


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


class TestL10nConfigCache:
    """Checks that pygeoapi's per locale config cache never hands out a config which was
    translated for another request.
    """

    @pytest.mark.parametrize(
        "cache, config_of_user_a, config_of_user_b, locale, expected_resources",
        [
            (
                {},
                {"resources": {"layer_of_user_a": {"title": {"en": "Layer A"}}}},
                {"resources": {"layer_of_user_b": {"title": {"en": "Layer B"}}}},
                "en",
                ["layer_of_user_a"],
            ),
            (
                _NoCache(),
                {"resources": {"layer_of_user_a": {"title": {"en": "Layer A"}}}},
                {"resources": {"layer_of_user_b": {"title": {"en": "Layer B"}}}},
                "en",
                ["layer_of_user_b"],
            ),
        ],
    )
    def test_second_request_gets_own_config(
        self, monkeypatch, cache, config_of_user_a, config_of_user_b, locale, expected_resources
    ):
        monkeypatch.setattr(l10n, "_cfg_cache", cache)
        l10n.translate_struct(config_of_user_a, l10n.str2locale(locale), True)
        translated = l10n.translate_struct(config_of_user_b, l10n.str2locale(locale), True)
        assert list(translated["resources"]) == expected_resources

    def test_module_patch_is_applied(self):
        assert isinstance(l10n._cfg_cache, _NoCache)


class TestDatasetFieldConstraintsValueLists:
    """The QGIS widgets which define value lists or domains become JSON schema keywords of
    the field, so clients like GeoGirafe can offer them in their forms.
    """

    @pytest.mark.parametrize(
        "value_map,type_oapif,expected",
        [
            # keys and descriptions differ, only `oneOf` carries the descriptions
            (
                ValueMap(
                    entries=[
                        ValueMapEntry(key="F", description="Forest"),
                        ValueMapEntry(key="M", description="Meadow"),
                    ]
                ),
                "string",
                {"oneOf": [{"const": "F", "title": "Forest"}, {"const": "M", "title": "Meadow"}]},
            ),
            # keys equal to their descriptions are offered as plain `enum` as well
            (
                ValueMap(
                    entries=[
                        ValueMapEntry(key="Forest", description="Forest"),
                        ValueMapEntry(key="Meadow", description="Meadow"),
                    ]
                ),
                "string",
                {
                    "oneOf": [
                        {"const": "Forest", "title": "Forest"},
                        {"const": "Meadow", "title": "Meadow"},
                    ],
                    "enum": ["Forest", "Meadow"],
                },
            ),
            # keys are cast to the type of the field
            (
                ValueMap(
                    entries=[
                        ValueMapEntry(key="1", description="one"),
                        ValueMapEntry(key="2", description="two"),
                    ]
                ),
                "integer",
                {"oneOf": [{"const": 1, "title": "one"}, {"const": 2, "title": "two"}]},
            ),
            # a key which does not fit the type of the field is left out
            (
                ValueMap(
                    entries=[
                        ValueMapEntry(key="1.5", description="one and a half"),
                        ValueMapEntry(key="many", description="many"),
                    ]
                ),
                "number",
                {"oneOf": [{"const": 1.5, "title": "one and a half"}]},
            ),
            # an empty value map offers nothing
            (ValueMap(entries=[]), "string", {"oneOf": []}),
        ],
    )
    def test_value_map_constraints(self, value_map, type_oapif, expected):
        assert DatasetFieldConstraints.value_map_constraints(value_map, type_oapif) == expected

    @pytest.mark.parametrize(
        "widget_range,expected",
        [
            (Range(minimum=0.0, maximum=100.0, step=0.5), {"minimum": 0.0, "maximum": 100.0}),
            (Range(minimum=0.0), {"minimum": 0.0}),
            (Range(maximum=100.0), {"maximum": 100.0}),
            (Range(), {}),
        ],
    )
    def test_range_constraints(self, widget_range, expected):
        assert DatasetFieldConstraints.range_constraints(widget_range) == expected


class TestDatasetFieldConstraintsSchema:
    """The schema of a single field, built from the field as it was exported by QSL. The
    layer is `parcels_1a2b`, the owners layer `owners_3c4d` is published on the mount.
    """

    @pytest.fixture
    def reference_resolver(self):
        yield ReferenceResolver(
            layer_id="parcels_1a2b",
            relations=[
                Relation(
                    id="parcels_owners_rel",
                    name="Parcel owner",
                    referencing_layer_id="parcels_1a2b",
                    referenced_layer_id="owners_3c4d",
                    field_pairs=[
                        RelationFieldPair(referencing_field="owner_id", referenced_field="id")
                    ],
                )
            ],
            targets={"owners_3c4d": ReferenceTarget(collection_id="owners", key_field="id")},
        )

    @pytest.mark.parametrize(
        "is_generated,expected",
        [
            # the source assigns the identifier on insert, the client must not send it
            (True, {"title": "fid", "type": "integer", "readOnly": True}),
            # the client has to send the identifier itself
            (False, {"title": "fid", "type": "integer", "required": True}),
        ],
    )
    def test_primary_key(self, reference_resolver, is_generated, expected):
        vector_field = VectorField(name="fid", type_oapif="integer", nullable=False)
        vector_field.set_definition_from_qsl(
            QslField(name="fid", type="integer", is_primary_key=True, is_generated=is_generated)
        )
        properties = SimpleNamespace(name="fid", datasource_field=vector_field)
        assert DatasetFieldConstraints.create_schema(properties, reference_resolver) == expected

    def test_value_map_field(self, reference_resolver):
        vector_field = VectorField(name="land_use", type_oapif="string", nullable=True)
        vector_field.set_definition_from_qsl(
            QslField(
                name="land_use",
                type="text",
                editor_widget=EditorWidget(
                    value_map=ValueMap(entries=[ValueMapEntry(key="F", description="Forest")])
                ),
            )
        )
        properties = SimpleNamespace(name="land_use", datasource_field=vector_field)
        assert DatasetFieldConstraints.create_schema(properties, reference_resolver) == {
            "title": "land_use",
            "type": "string",
            "oneOf": [{"const": "F", "title": "Forest"}],
        }

    def test_range_field(self, reference_resolver):
        vector_field = VectorField(name="height", type_oapif="number", nullable=True)
        vector_field.set_definition_from_qsl(
            QslField(
                name="height",
                type="float8",
                editor_widget=EditorWidget(range=Range(minimum=0.0, maximum=50.0)),
            )
        )
        properties = SimpleNamespace(name="height", datasource_field=vector_field)
        assert DatasetFieldConstraints.create_schema(properties, reference_resolver) == {
            "title": "height",
            "type": "number",
            "minimum": 0.0,
            "maximum": 50.0,
        }

    def test_reference_field(self, reference_resolver):
        vector_field = VectorField(name="owner_id", type_oapif="integer", nullable=True)
        vector_field.set_definition_from_qsl(
            QslField(
                name="owner_id",
                type="int4",
                editor_widget=EditorWidget(
                    relation_reference=RelationReference(relation_id="parcels_owners_rel")
                ),
            )
        )
        properties = SimpleNamespace(name="owner_id", datasource_field=vector_field)
        assert DatasetFieldConstraints.create_schema(properties, reference_resolver) == {
            "title": "owner_id",
            "type": "integer",
            "x-ogc-role": "reference",
            "x-ogc-collectionId": "owners",
        }

    def test_field_of_an_export_without_definition(self, reference_resolver):
        # fields of exports before the definition existed keep their plain schema
        vector_field = VectorField(name="owner_id", type_oapif="integer", nullable=True)
        properties = SimpleNamespace(name="owner_id", datasource_field=vector_field)
        assert DatasetFieldConstraints.create_schema(properties, reference_resolver) == {
            "title": "owner_id",
            "type": "integer",
        }


class TestFieldRepresentations:
    """ValueMap fields are delivered with the description instead of the stored value, as
    QGIS Server does. A setting switches that off.
    """

    @pytest.fixture
    def features_properties(self):
        land_use = VectorField(name="land_use", type_oapif="string", nullable=True)
        land_use.set_definition_from_qsl(
            QslField(
                name="land_use",
                type="text",
                editor_widget=EditorWidget(
                    value_map=ValueMap(
                        entries=[
                            ValueMapEntry(key="F", description="Forest"),
                            ValueMapEntry(key="M", description="Meadow"),
                        ]
                    )
                ),
            )
        )
        # no value map, no representation
        name = VectorField(name="name", type_oapif="string", nullable=True)
        name.set_definition_from_qsl(QslField(name="name", type="text"))
        # exported before the definition existed
        area = VectorField(name="area", type_oapif="number", nullable=True)
        yield [
            SimpleNamespace(name="land_use", datasource_field=land_use),
            SimpleNamespace(name="name", datasource_field=name),
            SimpleNamespace(name="area", datasource_field=area),
        ]

    def test_value_map_fields_are_represented(self, settings, features_properties):
        settings.FEATURES_REPRESENT_VALUES = True
        assert PygeoapiServer.get_field_representations(features_properties) == {
            "land_use": {"F": "Forest", "M": "Meadow"}
        }

    def test_switched_off_by_setting(self, settings, features_properties):
        settings.FEATURES_REPRESENT_VALUES = False
        assert PygeoapiServer.get_field_representations(features_properties) == {}


class TestGeoramaSqlProviderRepresent:
    """The provider replaces the stored values of the items it delivers by their labels.
    The provider itself is not instantiated, that would connect to the database, the
    labels are all `represent` needs.
    """

    @pytest.mark.parametrize(
        "properties,expected",
        [
            # the stored value gets its label
            ({"land_use": "F", "class": 1}, {"land_use": "Forest", "class": "first class"}),
            # a value without label is delivered as it is
            ({"land_use": "X", "class": 3}, {"land_use": "X", "class": 3}),
            # NULL stays NULL
            ({"land_use": None, "class": None}, {"land_use": None, "class": None}),
            # properties which are not part of the item are not added
            ({"name": "Parcel 1"}, {"name": "Parcel 1"}),
        ],
    )
    def test_represent(self, properties, expected):
        provider = SimpleNamespace(
            _representations={
                "land_use": {"F": "Forest", "M": "Meadow"},
                # labels are keyed by the stored value as string
                "class": {"1": "first class", "2": "second class"},
            }
        )
        feature = {"type": "Feature", "properties": properties}
        GeoramaSqlProvider.represent(provider, feature)
        assert feature["properties"] == expected


class TestValueViolation:
    """The database does not check value lists, so items written over OGC API Features are
    checked against the `oneOf` / `enum` lists of their fields before pygeoapi gets them.
    The layer lookup is replaced, only the constraints of the fields matter here.
    """

    @pytest.fixture
    def server(self, monkeypatch):
        server = PygeoapiServer()
        monkeypatch.setattr(server, "accessible_feature_layers", lambda request, cid: ["parcels"])
        monkeypatch.setattr(server, "get_visible_fields", lambda feature_layer: [])
        monkeypatch.setattr(
            server,
            "get_field_constraints",
            lambda feature_layer, fields: {
                "land_use": {
                    "type": "string",
                    "oneOf": [
                        {"const": "F", "title": "Forest"},
                        {"const": "M", "title": "Meadow"},
                    ],
                },
                "class": {"type": "integer", "enum": [1, 2]},
                "name": {"type": "string"},
            },
        )
        yield server

    @pytest.mark.parametrize(
        "properties",
        [
            {"land_use": "F", "class": 1, "name": "Parcel 1"},
            # NULL and missing values are not part of the value list check
            {"land_use": None},
            {},
            # fields without value list take anything
            {"name": "anything"},
        ],
    )
    def test_allowed_values_pass(self, server, properties):
        request = RequestFactory().post(
            "/features/collections/parcels/items",
            data=json.dumps({"type": "Feature", "properties": properties}),
            content_type="application/geo+json",
        )
        assert server.get_value_violation(request, "parcels") is None

    @pytest.mark.parametrize(
        "properties,expected_description",
        [
            ({"land_use": "X"}, "Value 'X' is not allowed for land_use"),
            ({"class": 3}, "Value 3 is not allowed for class"),
        ],
    )
    def test_values_out_of_the_list_are_rejected(self, server, properties, expected_description):
        request = RequestFactory().post(
            "/features/collections/parcels/items",
            data=json.dumps({"type": "Feature", "properties": properties}),
            content_type="application/geo+json",
        )
        response = server.get_value_violation(request, "parcels")
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert json.loads(response.content) == {
            "code": "InvalidParameterValue",
            "description": expected_description,
        }

    def test_malformed_body_is_left_to_pygeoapi(self, server):
        request = RequestFactory().post(
            "/features/collections/parcels/items",
            data="{not json",
            content_type="application/geo+json",
        )
        assert server.get_value_violation(request, "parcels") is None
