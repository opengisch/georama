"""Published layers of the global organisation, with the users permitted on them."""

import pytest
from guardian.shortcuts import assign_perm

from georama.features.factories import FeatureLayerFactory
from georama.features.factories import MetadataFactory as FeatureLayerMetadataFactory
from georama.maps.factories import MetadataFactory as MapsWmsLayerMetadataFactory
from georama.maps.factories import WmsLayerFactory
from georama.webgis.factories import MetadataFactory as WebGisMetadataFactory
from georama.webgis.factories import ThemeFactory
from georama.webgis.factories import WmsLayerFactory as WebGisWmsLayerFactory


@pytest.fixture
def global_wms_layer_public_queryable(global_vector):
    return WmsLayerFactory.create(
        public=True,
        queryable=True,
        datasource=global_vector,
        metadata=MapsWmsLayerMetadataFactory.create(title="Global Public Queryable"),
    )


@pytest.fixture
def global_wms_layer_public_non_queryable(global_vector):
    return WmsLayerFactory.create(
        public=True,
        queryable=False,
        datasource=global_vector,
        metadata=MapsWmsLayerMetadataFactory.create(title="Global Public NonQueryable"),
    )


@pytest.fixture
def global_wms_layer_non_public_queryable(global_vector):
    return WmsLayerFactory.create(
        public=False,
        queryable=True,
        datasource=global_vector,
        metadata=MapsWmsLayerMetadataFactory.create(title="Global NonPublic Queryable"),
    )


@pytest.fixture
def user_with_membership_global_wms_layer_permission(
    user_with_membership_global, global_wms_layer_non_public_queryable
):
    assign_perm(
        "view_published_wms_layer",
        user_with_membership_global,
        global_wms_layer_non_public_queryable,
    )
    return user_with_membership_global


@pytest.fixture
def global_webgis_theme_public(project_global_organisation):
    return ThemeFactory.create(
        project=project_global_organisation,
        public=True,
        metadata=WebGisMetadataFactory.create(title="Global Public Theme"),
    )


@pytest.fixture
def global_webgis_theme_non_public(project_global_organisation):
    return ThemeFactory.create(
        project=project_global_organisation,
        public=False,
        metadata=WebGisMetadataFactory.create(title="Global NonPublic Theme"),
    )


@pytest.fixture
def global_webgis_wms_layer_public_theme(global_vector, global_webgis_theme_public):
    return WebGisWmsLayerFactory.create(
        queryable=True,
        datasource=global_vector,
        metadata=WebGisMetadataFactory.create(title="Global Public Theme Layer"),
        theme=global_webgis_theme_public,
    )


@pytest.fixture
def global_webgis_wms_layer_non_public_theme(global_vector, global_webgis_theme_non_public):
    return WebGisWmsLayerFactory.create(
        queryable=True,
        datasource=global_vector,
        metadata=WebGisMetadataFactory.create(title="Global NonPublic Theme Layer"),
        theme=global_webgis_theme_non_public,
    )


@pytest.fixture
def user_with_membership_global_webgis_theme_permission(
    user_with_membership_global, global_webgis_wms_layer_non_public_theme
):
    assign_perm(
        "view_published_theme",
        user_with_membership_global,
        global_webgis_wms_layer_non_public_theme.theme,
    )
    return user_with_membership_global


@pytest.fixture
def global_feature_layer_public(global_postgis_vector):
    return FeatureLayerFactory.create(
        public=True,
        datasource=global_postgis_vector,
        metadata=FeatureLayerMetadataFactory.create(title="Global Public"),
    )


@pytest.fixture
def global_feature_layer_nonpublic(global_postgis_vector):
    return FeatureLayerFactory.create(
        public=False,
        datasource=global_postgis_vector,
        metadata=FeatureLayerMetadataFactory.create(title="Global NonPublic"),
    )


@pytest.fixture
def user_with_membership_global_feature_layer_view_permission(
    user_with_membership_global, global_feature_layer_nonpublic
):
    assign_perm(
        "view_objects_on_published_layer",
        user_with_membership_global,
        global_feature_layer_nonpublic,
    )
    return user_with_membership_global


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
    return user_with_membership_global


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
    return user_with_membership_global


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
    return user_with_membership_global
