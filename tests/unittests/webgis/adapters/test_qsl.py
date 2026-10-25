from types import SimpleNamespace

import pytest
from asgiref.sync import async_to_sync
from qgis_server_light.interface.exporter.extract import (
    Config,
    Datasets,
    Group,
    MetaData,
    Project,
    Raster,
    Service,
    Tree,
    TreeGroup,
    Vector,
)

from georama.webgis.adapters.qsl import WmsLayerIndex, theme_json_from_project_config
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup,
    WmsLayer,
    XyzLayer,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    MetaData as GGMetaData,
)

ROOT = ""


@pytest.fixture
def tree_group_factory():

    def create_tree_group(name: str, children: list[str]) -> TreeGroup:
        return TreeGroup(
            id=f"{name}_id", name=name, is_checked=True, children=children, is_expanded=True
        )

    yield create_tree_group


@pytest.fixture
def project_config_factory():

    def create_project_config(
        tree_groups: list[TreeGroup], datasets: list[Vector | Raster]
    ) -> Config:
        return Config(
            project=Project(version="3.44", name="project"),
            meta_data=MetaData(service=Service(contact_organization=None, contact_mail=None)),
            tree=Tree(members=tree_groups),
            datasets=Datasets(
                vector=[ds for ds in datasets if isinstance(ds, Vector)],
                raster=[ds for ds in datasets if isinstance(ds, Raster)],
                group=[
                    Group(
                        id=tg.id,
                        name=tg.name,
                        is_checked=True,
                        title=tg.name,
                        is_expanded=True,
                    )
                    for tg in tree_groups
                    if tg.name != ROOT
                ],
            ),
        )

    yield create_project_config


@pytest.fixture
def wms_layer_index_factory():
    """Stands in for `georama.webgis.models.WmsLayer`, which needs a datasource in the DB."""

    def create_wms_layer(identifier: str) -> SimpleNamespace:
        return SimpleNamespace(
            identifier=identifier,
            extent=None,
            metadata=SimpleNamespace(title=identifier),
            as_gg_wms_layer=WmsLayer(
                id=identifier,
                name=identifier,
                metadata=GGMetaData(),
                type="WMS",
                layers=identifier,
                imageType="image/png",
                minResolutionHint=0.0,
                maxResolutionHint=999999999.0,
                childLayers=[],
            ),
        )

    def create_wms_layer_index(datasets: list[Vector | Raster]) -> WmsLayerIndex:
        return {ds.id: create_wms_layer(ds.id) for ds in datasets}

    yield create_wms_layer_index


@pytest.fixture
def themes_json(project_config_factory, wms_layer_index_factory):
    """Runs the adapter for the given tree and datasets."""

    def create_themes_json(tree_groups: list[TreeGroup], datasets: list[Vector | Raster]):
        return async_to_sync(theme_json_from_project_config)(
            "theme",
            "icon",
            project_config_factory(tree_groups, datasets),
            wms_layer_index_factory(datasets),
        )

    yield create_themes_json


def names(children: list[LayerGroup | WmsLayer]) -> list[str]:
    return [child.name for child in children]


class TestEmptyGroups:
    def test_group_with_background_layers_only_is_dropped(
        self, themes_json, tree_group_factory, qsl_vector_factory, qsl_background_factory
    ):
        theme, background_layers, _ = themes_json(
            [
                tree_group_factory(ROOT, ["rivers", "Backgrounds"]),
                tree_group_factory("Backgrounds", ["ortho", "map"]),
            ],
            [
                qsl_vector_factory("rivers"),
                qsl_background_factory("ortho"),
                qsl_background_factory("map"),
            ],
        )

        assert names(theme.children) == ["rivers"]
        assert [type(layer) for layer in background_layers] == [XyzLayer, XyzLayer]
        assert names(background_layers) == ["ortho", "map"]

    def test_group_with_non_spatial_layers_only_is_dropped(
        self, themes_json, tree_group_factory, qsl_vector_factory
    ):
        theme, _, _ = themes_json(
            [
                tree_group_factory(ROOT, ["rivers", "Tables"]),
                tree_group_factory("Tables", ["owners"]),
            ],
            [qsl_vector_factory("rivers"), qsl_vector_factory("owners", is_spatial=False)],
        )

        assert names(theme.children) == ["rivers"]

    def test_group_without_children_is_dropped(
        self, themes_json, tree_group_factory, qsl_vector_factory
    ):
        theme, _, _ = themes_json(
            [tree_group_factory(ROOT, ["rivers", "Empty"]), tree_group_factory("Empty", [])],
            [qsl_vector_factory("rivers")],
        )

        assert names(theme.children) == ["rivers"]

    def test_group_with_empty_groups_only_is_dropped(
        self, themes_json, tree_group_factory, qsl_vector_factory, qsl_background_factory
    ):
        theme, background_layers, _ = themes_json(
            [
                tree_group_factory(ROOT, ["rivers", "Outer"]),
                tree_group_factory("Outer", ["Backgrounds"]),
                tree_group_factory("Backgrounds", ["ortho"]),
            ],
            [qsl_vector_factory("rivers"), qsl_background_factory("ortho")],
        )

        assert names(theme.children) == ["rivers"]
        assert names(background_layers) == ["ortho"]

    def test_mixed_group_keeps_its_position_and_non_background_layers(
        self, themes_json, tree_group_factory, qsl_vector_factory, qsl_background_factory
    ):
        theme, background_layers, _ = themes_json(
            [
                tree_group_factory(ROOT, ["Water", "roads"]),
                tree_group_factory("Water", ["Backgrounds", "rivers", "ortho"]),
                tree_group_factory("Backgrounds", ["map"]),
            ],
            [
                qsl_vector_factory("rivers"),
                qsl_vector_factory("roads"),
                qsl_background_factory("ortho"),
                qsl_background_factory("map"),
            ],
        )

        assert names(theme.children) == ["Water", "roads"]
        assert names(theme.children[0].children) == ["rivers"]
        assert names(background_layers) == ["map", "ortho"]
