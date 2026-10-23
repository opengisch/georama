import struct

import numpy as np
import pytest
from django.core.exceptions import ImproperlyConfigured
from qgis_server_light.interface.common import Crs

from georama.maps.maps_config import Config
from georama.maps.services.wfs_2_0_0.get_feature import WfsGetFeature


@pytest.fixture
def wfs_get_feature():
    return WfsGetFeature("maps", "http://localhost/", None, None, None, [])


@pytest.fixture
def layer_crs():
    return Config.crs_from_epsg_auth_id("EPSG:2056")


class TestWfsGetFeatureResolveSrsName:
    @pytest.mark.parametrize(
        "srs_name",
        [
            "EPSG:2056",
            "epsg:2056",
            "http://www.opengis.net/def/crs/EPSG/0/2056",
            "urn:ogc:def:crs:EPSG::2056",
        ],
    )
    def test_matching_srs_name_returns_layer_crs(self, wfs_get_feature, layer_crs, srs_name):
        assert wfs_get_feature.resolve_srs_name(srs_name, [layer_crs]) is layer_crs

    def test_matching_srs_name_returns_other_crs(self, wfs_get_feature, layer_crs):
        other_crs = Config.crs_from_epsg_auth_id("EPSG:4326")
        resolved_crs = wfs_get_feature.resolve_srs_name(
            "urn:ogc:def:crs:EPSG::4326", [layer_crs, other_crs]
        )
        assert resolved_crs is other_crs

    def test_rejection_with_crs_without_identifiers(self, wfs_get_feature, layer_crs):
        with pytest.raises(AttributeError) as error:
            wfs_get_feature.resolve_srs_name("EPSG:4326", [layer_crs, Crs()])
        assert "InvalidParameterValue" in str(error.value)

    def test_other_srs_name_is_rejected(self, wfs_get_feature, layer_crs):
        with pytest.raises(AttributeError) as error:
            wfs_get_feature.resolve_srs_name("EPSG:4326", [layer_crs])
        assert "InvalidParameterValue" in str(error.value)
        assert "EPSG:4326" in str(error.value)


class TestWfsOperationSupportedCrs:
    def test_layer_crs_first_then_configured(self, settings, wfs_get_feature, layer_crs):
        settings.MAPS_OGC_OTHER_CRS = ["EPSG:3857", "EPSG:4326"]
        supported_crs = wfs_get_feature.supported_crs(layer_crs)
        assert [crs.auth_id for crs in supported_crs] == ["EPSG:2056", "EPSG:3857", "EPSG:4326"]

    def test_layer_crs_is_not_duplicated(self, settings, wfs_get_feature):
        settings.MAPS_OGC_OTHER_CRS = ["EPSG:3857", "EPSG:4326"]
        layer_crs = Config.crs_from_epsg_auth_id("EPSG:4326")
        supported_crs = wfs_get_feature.supported_crs(layer_crs)
        assert [crs.auth_id for crs in supported_crs] == ["EPSG:4326", "EPSG:3857"]

    def test_configured_duplicates_are_removed(self, settings, wfs_get_feature, layer_crs):
        settings.MAPS_OGC_OTHER_CRS = ["EPSG:4326", "epsg:4326", "EPSG:3857", "EPSG:4326"]
        supported_crs = wfs_get_feature.supported_crs(layer_crs)
        assert [crs.auth_id for crs in supported_crs] == ["EPSG:2056", "EPSG:4326", "EPSG:3857"]

    def test_configured_per_app(self, settings, layer_crs):
        settings.WEBGIS_OGC_OTHER_CRS = ["EPSG:21781"]
        wfs_get_feature = WfsGetFeature("webgis", "http://localhost/", None, None, None, [])
        supported_crs = wfs_get_feature.supported_crs(layer_crs)
        assert [crs.auth_id for crs in supported_crs] == ["EPSG:2056", "EPSG:21781"]


class TestConfigCrsFromEpsgAuthId:
    def test_all_identifiers(self):
        assert Config.crs_from_epsg_auth_id("EPSG:3857") == Crs(
            auth_id="EPSG:3857",
            postgis_srid=3857,
            ogc_uri="http://www.opengis.net/def/crs/EPSG/0/3857",
            ogc_urn="urn:ogc:def:crs:EPSG::3857",
        )

    @pytest.mark.parametrize("auth_id", ["CRS:84", "EPSG:abc", "3857"])
    def test_no_epsg_code_is_rejected(self, auth_id):
        with pytest.raises(ImproperlyConfigured):
            Config.crs_from_epsg_auth_id(auth_id)


class TestWfsGetFeatureSwapAxis:
    @pytest.mark.parametrize(
        "srs_name, auth_id, expected",
        [
            ("EPSG:4326", "EPSG:4326", False),
            ("epsg:4326", "EPSG:4326", False),
            ("urn:ogc:def:crs:EPSG::4326", "EPSG:4326", True),
            ("http://www.opengis.net/def/crs/EPSG/0/4326", "EPSG:4326", True),
            ("urn:ogc:def:crs:EPSG::2056", "EPSG:2056", False),
            ("http://www.opengis.net/def/crs/EPSG/0/3857", "EPSG:3857", False),
        ],
    )
    def test_decision(self, srs_name, auth_id, expected):
        crs = Config.crs_from_epsg_auth_id(auth_id)
        crs.axis_inverted = auth_id == "EPSG:4326"
        assert WfsGetFeature.swap_axis(srs_name, crs) is expected

    def test_swap_keeps_further_ordinates(self):
        coordinates = np.frombuffer(struct.pack("<6d", 8.5, 47.4, 500, 9, 46, 600), dtype="<f8")
        swapped = WfsGetFeature.swap_axis_of_coordinates(coordinates, 3)
        assert swapped.tolist() == [47.4, 8.5, 500, 46, 9, 600]
        assert coordinates.tolist() == [8.5, 47.4, 500, 9, 46, 600]

    @pytest.mark.parametrize("swap_axis, expected", [(False, [8.5, 47.4]), (True, [47.4, 8.5])])
    def test_point(self, wfs_get_feature, swap_axis, expected):
        wkb = struct.pack("<BI2d", 1, 1, 8.5, 47.4)
        geometry = wfs_get_feature.parse_wkb_to_gml3(wkb, "urn:ogc:def:crs:EPSG::4326", swap_axis)
        assert geometry.point.pos.value.tolist() == expected

    def test_polygon(self, wfs_get_feature):
        ring = [(8, 47), (9, 47), (9, 48), (8, 47)]
        wkb = struct.pack("<BIII", 1, 3, 1, len(ring)) + b"".join(
            struct.pack("<2d", *point) for point in ring
        )
        geometry = wfs_get_feature.parse_wkb_to_gml3(wkb, "urn:ogc:def:crs:EPSG::4326", True)
        assert geometry.polygon.exterior.linear_ring.pos_list.value.tolist() == [
            47,
            8,
            47,
            9,
            48,
            9,
            47,
            8,
        ]
