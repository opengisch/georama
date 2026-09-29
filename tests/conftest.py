from importlib import import_module

import psycopg
import pytest
from django.conf import settings
from faker import Faker
from faker.utils.loading import find_available_providers
from guardian.shortcuts import assign_perm

from georama.core.common.faker.gis import Dataset
from georama.core.factories import (
    AdminUserFactory,
    MembershipFactory,
    OrganisationFactory,
    UserFactory,
)
from georama.features.factories import FeatureLayerFactory
from georama.features.factories import MetadataFactory as FeatureLayerMetadataFactory
from georama.features.models.feature_layer import FeatureLayerUserObjectPermission
from georama.integration.factories import FieldFactory, ProjectFactory, VectorFactory
from georama.maps.factories import MetadataFactory as MapsWmsLayerMetadataFactory
from georama.maps.factories import WmsLayerFactory
from georama.maps.models.wms_layer import WmsLayerUserObjectPermission


@pytest.fixture
def admin_user_name():
    yield "admin"


@pytest.fixture
def admin_password():
    yield "admin"


@pytest.fixture
def admin_email():
    yield "admin@example.org"


@pytest.fixture
def admin_user(admin_user_name, admin_password, admin_email):
    admin = AdminUserFactory.create(
        username=admin_user_name,
        email=admin_email,
        is_staff=True,
        is_superuser=True,
        password=admin_password,
    )
    yield admin
    admin.delete()


@pytest.fixture
def organisation():
    organisation = OrganisationFactory.create()
    yield organisation
    organisation.delete()


@pytest.fixture
def organisation_public_access():
    organisation = OrganisationFactory.create(public_access=True)
    yield organisation
    organisation.delete()


@pytest.fixture
def organisation_non_public_access():
    organisation = OrganisationFactory.create(public_access=False)
    yield organisation
    organisation.delete()


@pytest.fixture
def membership(organisation):
    membership = MembershipFactory.create(organisation=organisation)
    yield membership
    membership.delete()


@pytest.fixture
def membership_public_organisation(organisation_public_access):
    membership = MembershipFactory.create(organisation=organisation_public_access)
    yield membership
    membership.delete()


@pytest.fixture
def membership_global():
    membership = MembershipFactory.create(organisation=None)
    yield membership
    membership.delete()


@pytest.fixture
def membership_non_public_organisation(organisation_non_public_access):
    membership = MembershipFactory.create(organisation=organisation_non_public_access)
    yield membership
    membership.delete()


@pytest.fixture
def user_user_name():
    yield "limu"


@pytest.fixture
def user_first_name():
    yield "Lieschen"


@pytest.fixture
def user_last_name():
    yield "Müller"


@pytest.fixture
def user_password():
    yield "oh-my-secret"


@pytest.fixture
def user_email(user_user_name):
    yield f"{user_user_name}@example.org"


@pytest.fixture
def user(user_user_name, user_first_name, user_last_name, user_email, user_password):
    user = UserFactory.create(
        username=user_user_name,
        password=user_password,
        first_name=user_first_name,
        last_name=user_last_name,
        email=user_email,
        is_staff=False,
        is_superuser=False,
    )
    yield user
    user.delete()


@pytest.fixture
def user_with_membership_global(user, membership_global):
    user.memberships.add(membership_global)
    user.save()
    yield user


@pytest.fixture
def user_with_dedicated_membership_non_public(user, membership_non_public_organisation):
    user.memberships.add(membership_non_public_organisation)
    user.save()
    yield user


@pytest.fixture
def project_global_organisation():
    project = ProjectFactory.create(organisation=None)
    yield project
    project.delete()


@pytest.fixture
def schema_name():
    return "test_data"


@pytest.fixture
def db_connection():
    conn = psycopg.connect(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PW,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )
    try:
        yield conn
    finally:
        conn.close()


@pytest.fixture
def db_schema(schema_name, db_connection):
    with db_connection.cursor() as cur:
        cur.execute(f"CREATE SCHEMA {schema_name};")
    db_connection.commit()
    yield
    with db_connection.cursor() as cur:
        cur.execute(f"DROP SCHEMA IF EXISTS {schema_name} CASCADE;")
    db_connection.commit()


@pytest.fixture
def global_vector_dataset(project_global_organisation, db_schema, schema_name, db_connection):
    META_PROVIDERS_MODULES = [
        "georama.core.common.faker",
    ]
    PROVIDERS = find_available_providers([import_module(path) for path in META_PROVIDERS_MODULES])
    fake = Faker(locale="de_CH", providers=PROVIDERS)
    dataset: Dataset = fake.vector_datasets(schema_name, amount=1)[0]
    with db_connection.cursor() as cur:
        cur.execute(dataset.create_table_sql)
        cur.execute(dataset.insert_values_sql)
    db_connection.commit()
    vector = VectorFactory.create(
        project=project_global_organisation,
        name=dataset.name,
        geometry_type_wkb=dataset.geometry_type_wkb,
        geometry_type_simple=dataset.geometry_type_simple,
        crs={
            "auth_id": f"EPSG:{dataset.epsg_id}",
            "ogc_uri": f"http://www.opengis.net/def/crs/EPSG/0/{dataset.epsg_id}",
            "ogc_urn": f"urn:ogc:def:crs:EPSG::{dataset.epsg_id}",
            "postgis_srid": dataset.epsg_id,
        },
        driver="postgres",
        source={
            "ogr": None,
            "wfs": None,
            "wms": None,
            "xyz": None,
            "gdal": None,
            "wmts": None,
            "postgres": {
                "key": "id",
                "sql": None,
                "host": settings.DB_HOST,
                "port": settings.DB_PORT,
                "srid": f"{dataset.epsg_id}",
                "type": None,
                "table": dataset.table_name.lower(),
                "dbname": settings.DB_NAME,
                "schema": schema_name,
                "service": None,
                "sslmode": 0,
                "password": settings.DB_PW,
                "username": settings.DB_USER,
                "ssl_mode_text": "prefer",
                "geometry_column": dataset.geometry_field_name,
                "check_primary_key_unicity": None,
            },
            "vector_tile": None,
        },
        bbox="{},{},{},{}".format(*fake.bounds()),
        bbox_wgs84="{},{},{},{}".format(*fake.bounds_wgs84()),
    )
    for field in dataset.selected_fields:
        FieldFactory.create(
            datasource=vector,
            name=field.name,
            type=field.type,
            alias=field.alias,
            nullable=field.nullable,
            type_oapif=field.type_oapif,
            is_primary_key=field.is_primary_key,
            length=field.length,
            precision=field.precision,
            type_oapif_format=field.type_oapif_format,
            type_wfs=field.type_wfs,
            comment=field.comment,
        )
    yield vector
    vector.delete()


@pytest.fixture
def global_wms_layer_public_queryable(global_vector_dataset):
    layer = WmsLayerFactory.create(
        public=True,
        queryable=True,
        datasource=global_vector_dataset,
        metadata=MapsWmsLayerMetadataFactory.create(title="Global Public Queryable"),
    )
    yield layer
    layer.delete()


@pytest.fixture
def global_wms_layer_public_non_queryable(global_vector_dataset):
    layer = WmsLayerFactory.create(
        public=True,
        queryable=False,
        datasource=global_vector_dataset,
        metadata=MapsWmsLayerMetadataFactory.create(title="Global Public NonQueryable"),
    )
    yield layer
    layer.delete()


@pytest.fixture
def global_wms_layer_non_public_queryable(global_vector_dataset):
    layer = WmsLayerFactory.create(
        public=False,
        queryable=True,
        datasource=global_vector_dataset,
        metadata=MapsWmsLayerMetadataFactory.create(title="Global NonPublic Queryable"),
    )
    yield layer
    layer.delete()


@pytest.fixture
def user_with_membership_global_wms_layer_permission(
    user_with_membership_global, global_wms_layer_non_public_queryable
):
    assign_perm(
        "view_published_wms_layer",
        user_with_membership_global,
        global_wms_layer_non_public_queryable,
    )
    yield user_with_membership_global
    WmsLayerUserObjectPermission.objects.all().delete()


@pytest.fixture
def global_feature_layer_public(global_vector_dataset):
    layer = FeatureLayerFactory.create(
        public=True,
        datasource=global_vector_dataset,
        metadata=FeatureLayerMetadataFactory.create(title="Global Public"),
    )
    yield layer
    layer.delete()


@pytest.fixture
def global_feature_layer_nonpublic(global_vector_dataset):
    layer = FeatureLayerFactory.create(
        public=False,
        datasource=global_vector_dataset,
        metadata=FeatureLayerMetadataFactory.create(title="Global NonPublic"),
    )
    yield layer
    layer.delete()


@pytest.fixture
def user_with_membership_global_feature_layer_view_permission(
    user_with_membership_global, global_feature_layer_nonpublic
):
    assign_perm(
        "view_objects_on_published_layer",
        user_with_membership_global,
        global_feature_layer_nonpublic,
    )
    yield user_with_membership_global
    FeatureLayerUserObjectPermission.objects.all().delete()


@pytest.fixture
def user_with_membership_global_feature_layer_create_permission(
    user_with_membership_global,
    global_feature_layer_nonpublic,
    user_with_membership_global_feature_layer_view_permission,
):
    assign_perm(
        "create_objects_on_published_layer",
        user_with_membership_global,
        global_feature_layer_nonpublic,
    )
    yield user_with_membership_global
    FeatureLayerUserObjectPermission.objects.all().delete()


@pytest.fixture
def user_with_membership_global_feature_layer_delete_permission(
    user_with_membership_global,
    global_feature_layer_nonpublic,
    user_with_membership_global_feature_layer_view_permission,
):
    assign_perm(
        "delete_objects_on_published_layer",
        user_with_membership_global,
        global_feature_layer_nonpublic,
    )
    yield user_with_membership_global
    FeatureLayerUserObjectPermission.objects.all().delete()


@pytest.fixture
def user_with_membership_global_feature_layer_update_permission(
    user_with_membership_global,
    global_feature_layer_nonpublic,
    user_with_membership_global_feature_layer_view_permission,
):
    assign_perm(
        "update_objects_on_published_layer",
        user_with_membership_global,
        global_feature_layer_nonpublic,
    )
    yield user_with_membership_global
    FeatureLayerUserObjectPermission.objects.all().delete()
