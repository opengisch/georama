from types import SimpleNamespace

import pytest
from asgiref.sync import async_to_sync
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.dispatcher.common import Status
from qgis_server_light.interface.exporter.extract import (
    Config,
    Datasets,
    DataSource,
    Group,
    MetaData,
    Project,
    Raster,
    Service,
    Tree,
    TreeGroup,
    Vector,
    XYZSource,
)
from qgis_server_light.interface.job.common.output import JobResult
from qgis_server_light.interface.job.render.input import QslJobParameterRender

from georama.webgis.adapters.qsl import theme_json_from_project_config
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup,
    WmsLayer,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    MetaData as GGMetaData,
)

ROOT = ""

# fixtures cant be used in test parametrization, so we instanciate some test objects
RIVERS = Vector(
    id="rivers", name="rivers", is_checked=True, title="rivers", source=DataSource(), driver="ogr"
)
ROADS = Vector(
    id="roads", name="roads", is_checked=True, title="roads", source=DataSource(), driver="ogr"
)
OWNERS = Vector(
    id="owners",
    name="owners",
    is_checked=True,
    title="owners",
    source=DataSource(),
    driver="ogr",
    is_spatial=False,
)
ORTHO = Raster(
    id="ortho",
    name="ortho",
    is_checked=False,
    title="ortho",
    source=DataSource(xyz=XYZSource(url="https://ortho.example.com/{z}/{x}/{y}.png")),
    driver="wms",
    is_background=True,
)
MAP = Raster(
    id="map",
    name="map",
    is_checked=False,
    title="map",
    source=DataSource(xyz=XYZSource(url="https://map.example.com/{z}/{x}/{y}.png")),
    driver="wms",
    is_background=True,
)

BACKGROUNDS = Group(
    id="backgrounds", name="Backgrounds", is_checked=True, title="Backgrounds", is_expanded=True
)
TABLES = Group(id="tables", name="Tables", is_checked=True, title="Tables", is_expanded=True)
EMPTY = Group(id="empty", name="Empty", is_checked=True, title="Empty", is_expanded=True)
OUTER = Group(id="outer", name="Outer", is_checked=True, title="Outer", is_expanded=True)
WATER = Group(id="water", name="Water", is_checked=True, title="Water", is_expanded=True)

FAILED_RENDER_JOB_RESULT = (
    JobResult(id="job", data="error", content_type="text/plain"),
    Status.FAILURE.value,
)


@pytest.fixture
def project_config(tree, datasets):
    yield Config(
        project=Project(version="3.44", name="project"),
        meta_data=MetaData(service=Service(contact_organization=None, contact_mail=None)),
        tree=tree,
        datasets=datasets,
    )


@pytest.fixture
def wms_layer_index(datasets, qsl_job_layer):
    """Stands in for `georama.webgis.models.WmsLayer`, which needs a datasource in the DB."""
    yield {
        ds.id: SimpleNamespace(
            identifier=ds.id,
            extent=None,
            metadata=SimpleNamespace(title=ds.id),
            as_gg_wms_layer=WmsLayer(
                id=ds.id,
                name=ds.id,
                metadata=GGMetaData(),
                type="WMS",
                layers=ds.id,
                imageType="image/png",
                minResolutionHint=0.0,
                maxResolutionHint=999999999.0,
                childLayers=[],
            ),
            to_qsl_job_layer=lambda: qsl_job_layer,
        )
        for ds in [*datasets.vector, *datasets.raster]
    }


@pytest.fixture
def themes_json(project_config, wms_layer_index, posted_jobs, render_job_result):
    """Runs the adapter, background thumbnails are answered with `render_job_result`."""
    posted_jobs.answer = render_job_result
    yield async_to_sync(theme_json_from_project_config)(
        "theme", "icon", project_config, wms_layer_index
    )


def names(children: list[LayerGroup | WmsLayer]) -> list[str]:
    return [child.name for child in children]


class TestEmptyGroups:
    @pytest.mark.parametrize(
        "tree, datasets, background_layer_names",
        [
            pytest.param(
                Tree(
                    members=[
                        TreeGroup(
                            id="root",
                            name=ROOT,
                            is_checked=True,
                            children=["rivers", "Backgrounds"],
                            is_expanded=True,
                        ),
                        TreeGroup(
                            id="backgrounds",
                            name="Backgrounds",
                            is_checked=True,
                            children=["ortho", "map"],
                            is_expanded=True,
                        ),
                    ]
                ),
                Datasets(vector=[RIVERS], raster=[ORTHO, MAP], group=[BACKGROUNDS]),
                ["ortho", "map"],
                id="background_layers_only",
            ),
            pytest.param(
                Tree(
                    members=[
                        TreeGroup(
                            id="root",
                            name=ROOT,
                            is_checked=True,
                            children=["rivers", "Tables"],
                            is_expanded=True,
                        ),
                        TreeGroup(
                            id="tables",
                            name="Tables",
                            is_checked=True,
                            children=["owners"],
                            is_expanded=True,
                        ),
                    ]
                ),
                Datasets(vector=[RIVERS, OWNERS], group=[TABLES]),
                [],
                id="non_spatial_layers_only",
            ),
            pytest.param(
                Tree(
                    members=[
                        TreeGroup(
                            id="root",
                            name=ROOT,
                            is_checked=True,
                            children=["rivers", "Empty"],
                            is_expanded=True,
                        ),
                        TreeGroup(
                            id="empty", name="Empty", is_checked=True, children=[], is_expanded=True
                        ),
                    ]
                ),
                Datasets(vector=[RIVERS], group=[EMPTY]),
                [],
                id="without_children",
            ),
            pytest.param(
                Tree(
                    members=[
                        TreeGroup(
                            id="root",
                            name=ROOT,
                            is_checked=True,
                            children=["rivers", "Outer"],
                            is_expanded=True,
                        ),
                        TreeGroup(
                            id="outer",
                            name="Outer",
                            is_checked=True,
                            children=["Backgrounds"],
                            is_expanded=True,
                        ),
                        TreeGroup(
                            id="backgrounds",
                            name="Backgrounds",
                            is_checked=True,
                            children=["ortho"],
                            is_expanded=True,
                        ),
                    ]
                ),
                Datasets(vector=[RIVERS], raster=[ORTHO], group=[OUTER, BACKGROUNDS]),
                ["ortho"],
                id="empty_groups_only",
            ),
        ],
    )
    def test_group_is_dropped(self, themes_json, background_layer_names):
        theme, background_layers, _ = themes_json

        assert names(theme.children) == ["rivers"]
        assert names(background_layers) == background_layer_names

    @pytest.mark.parametrize(
        "tree, datasets",
        [
            (
                Tree(
                    members=[
                        TreeGroup(
                            id="root",
                            name=ROOT,
                            is_checked=True,
                            children=["Water", "roads"],
                            is_expanded=True,
                        ),
                        TreeGroup(
                            id="water",
                            name="Water",
                            is_checked=True,
                            children=["Backgrounds", "rivers", "ortho"],
                            is_expanded=True,
                        ),
                        TreeGroup(
                            id="backgrounds",
                            name="Backgrounds",
                            is_checked=True,
                            children=["map"],
                            is_expanded=True,
                        ),
                    ]
                ),
                Datasets(vector=[RIVERS, ROADS], raster=[ORTHO, MAP], group=[WATER, BACKGROUNDS]),
            )
        ],
    )
    def test_mixed_group_keeps_its_position_and_non_background_layers(self, themes_json):
        theme, background_layers, _ = themes_json

        assert names(theme.children) == ["Water", "roads"]
        assert names(theme.children[0].children) == ["rivers"]
        assert names(background_layers) == ["map", "ortho"]


BACKGROUND_ONLY_TREE = Tree(
    members=[TreeGroup(id="root", name=ROOT, is_checked=True, children=["ortho"], is_expanded=True)]
)
NO_BACKGROUND_TREE = Tree(
    members=[
        TreeGroup(id="root", name=ROOT, is_checked=True, children=["rivers"], is_expanded=True)
    ]
)


class TestBackgroundThumbnail:
    @pytest.mark.parametrize("tree, datasets", [(BACKGROUND_ONLY_TREE, Datasets(raster=[ORTHO]))])
    def test_rendered_over_configured_extent(
        self, settings, themes_json, posted_jobs, qsl_job_layer
    ):
        _, background_layers, _ = themes_json

        assert posted_jobs == [
            QslJobParameterRender(
                layers=[qsl_job_layer],
                bbox=BBox.from_string(settings.WEBGIS_BACKGROUND_THUMBNAIL_EXTENT),
                crs=settings.WEBGIS_BACKGROUND_THUMBNAIL_CRS,
                width=220,
                height=120,
                dpi=72,
            )
        ]
        assert background_layers[0].metadata.thumbnail == "data:image/png;base64,cG5n"

    @pytest.mark.parametrize(
        "tree, datasets, render_job_result",
        [(BACKGROUND_ONLY_TREE, Datasets(raster=[ORTHO]), FAILED_RENDER_JOB_RESULT)],
    )
    def test_failed_rendering(self, themes_json):
        _, background_layers, _ = themes_json

        assert names(background_layers) == ["ortho"]
        assert background_layers[0].metadata.thumbnail is None

    @pytest.mark.parametrize("tree, datasets", [(NO_BACKGROUND_TREE, Datasets(vector=[RIVERS]))])
    def test_not_rendered_for_other_layers(self, themes_json, posted_jobs):
        theme, _, _ = themes_json

        assert posted_jobs == []
        assert theme.children[0].metadata.thumbnail is None
