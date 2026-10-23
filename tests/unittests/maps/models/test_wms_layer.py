import pytest
from qgis_server_light.interface.common import BBox
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.integration.models import Vector
from georama.maps.models import WmsLayer


@pytest.fixture
def wms_layer_factory(crs_factory):
    def create_wms_layer(code: int, axis_inverted: bool, extent: str) -> WmsLayer:
        datasource = Vector(
            crs=DictEncoder().encode(crs_factory(code, axis_inverted=axis_inverted)),
            bbox="2480000.0,1070000.0,0.0,2840000.0,1300000.0,0.0",
            bbox_wgs84="5.9,45.8,0.0,10.5,47.8,0.0",
        )
        return WmsLayer(datasource=datasource, extent=extent)

    yield create_wms_layer


class TestWmsLayerExtentInAxisOrder:
    def test_east_north_crs(self, wms_layer_factory):
        wms_layer = wms_layer_factory(2056, False, "2480000,1070000,2840000,1300000")
        assert wms_layer.extent_in_axis_order.to_2d_list() == [2480000, 1070000, 2840000, 1300000]

    def test_inverted_axis_crs(self, wms_layer_factory):
        wms_layer = wms_layer_factory(4326, True, "5.9,45.8,10.5,47.8")
        assert wms_layer.extent_in_axis_order.to_2d_list() == [45.8, 5.9, 47.8, 10.5]


class TestWmsLayerHasDatasourceExtent:
    def test_datasource_extent(self, wms_layer_factory):
        wms_layer = wms_layer_factory(2056, False, "2480000,1070000,2840000,1300000")
        assert wms_layer.has_datasource_extent(wms_layer.datasource) is True

    def test_custom_extent(self, wms_layer_factory):
        wms_layer = wms_layer_factory(2056, False, "2500000,1100000,2700000,1200000")
        assert wms_layer.has_datasource_extent(wms_layer.datasource) is False

    def test_datasource_extent_wgs84_is_taken(self, wms_layer_factory):
        wms_layer = wms_layer_factory(2056, False, "2480000,1070000,2840000,1300000")
        wms_layer._prepare_save()
        assert BBox.from_string(wms_layer.extent_wgs84).to_2d_list() == [5.9, 45.8, 10.5, 47.8]
