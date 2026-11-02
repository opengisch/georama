"""Published layers of the global organisation, with the users permitted on them."""

import pytest
from guardian.shortcuts import assign_perm

from georama.features.factories import FeatureLayerFactory
from georama.features.factories import MetadataFactory as FeatureLayerMetadataFactory
from georama.features.models import FeatureLayer
from georama.integration.models import Project, Vector
from georama.maps.factories import MetadataFactory as MapsWmsLayerMetadataFactory
from georama.maps.factories import WmsLayerFactory
from georama.maps.models import WmsLayer
from georama.webgis.factories import MetadataFactory as WebGisMetadataFactory
from georama.webgis.factories import ThemeFactory
from georama.webgis.factories import WmsLayerFactory as WebGisWmsLayerFactory
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import MetaData
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import Theme as GGTheme
from georama.webgis.models import Theme
from georama.webgis.models import WmsLayer as WebGisWmsLayer


def visibility(public: bool) -> str:
    return "Public" if public else "NonPublic"


def scope(project: Project) -> str:
    """The organisation of `project`, as named in the titles."""
    return project.organisation.name if project.organisation else "Global"


def create_wms_layer(vector: Vector, public: bool, queryable: bool) -> WmsLayer:
    return WmsLayerFactory.create(
        public=public,
        queryable=queryable,
        datasource=vector,
        metadata=MapsWmsLayerMetadataFactory.create(
            title=f"{scope(vector.project)} {visibility(public)} "
            f"{'Queryable' if queryable else 'NonQueryable'}"
        ),
    )


def create_theme(project: Project, public: bool) -> Theme:
    return ThemeFactory.create(
        project=project,
        public=public,
        metadata=WebGisMetadataFactory.create(title=f"{scope(project)} {visibility(public)} Theme"),
    )


def with_geogirafe_json(theme: Theme) -> Theme:
    """Gives `theme` the minimal GeoGirafe JSON: `geogirafe` leaves out the themes without."""
    theme.set_from_dataclass(
        GGTheme(
            id=theme.identifier,
            name=theme.metadata.title,
            icon=theme.icon_default,
            metadata=MetaData(),
        )
    )
    theme.save()
    return theme


def create_webgis_wms_layer(vector: Vector, theme: Theme) -> WebGisWmsLayer:
    return WebGisWmsLayerFactory.create(
        queryable=True,
        datasource=vector,
        metadata=WebGisMetadataFactory.create(
            title=f"{scope(theme.project)} {visibility(theme.public)} Theme Layer"
        ),
        theme=theme,
    )


def create_feature_layer(vector: Vector, public: bool) -> FeatureLayer:
    return FeatureLayerFactory.create(
        public=public,
        datasource=vector,
        metadata=FeatureLayerMetadataFactory.create(
            title=f"{scope(vector.project)} {visibility(public)}"
        ),
    )


@pytest.fixture
def global_wms_layer_public_queryable(global_vector):
    return create_wms_layer(global_vector, public=True, queryable=True)


@pytest.fixture
def global_wms_layer_public_non_queryable(global_vector):
    return create_wms_layer(global_vector, public=True, queryable=False)


@pytest.fixture
def global_wms_layer_non_public_queryable(global_vector):
    return create_wms_layer(global_vector, public=False, queryable=True)


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
    return create_theme(project_global_organisation, public=True)


@pytest.fixture
def global_webgis_theme_non_public(project_global_organisation):
    return create_theme(project_global_organisation, public=False)


@pytest.fixture
def global_webgis_wms_layer_public_theme(global_vector, global_webgis_theme_public):
    return create_webgis_wms_layer(global_vector, global_webgis_theme_public)


@pytest.fixture
def global_webgis_wms_layer_non_public_theme(global_vector, global_webgis_theme_non_public):
    return create_webgis_wms_layer(global_vector, global_webgis_theme_non_public)


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
    return create_feature_layer(global_postgis_vector, public=True)


@pytest.fixture
def global_feature_layer_nonpublic(global_postgis_vector):
    return create_feature_layer(global_postgis_vector, public=False)


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
