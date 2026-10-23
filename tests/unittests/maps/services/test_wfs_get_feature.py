import struct

import numpy as np
import pytest
from qgis_server_light.interface.common import Crs
from qgis_server_light.interface.job.common.output import JobResult
from qgis_server_light.interface.job.feature.output import (
    Feature,
    FeatureCollection,
    Geometry,
    QueryCollection,
)
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.maps.maps_config import Config
from georama.maps.services.wfs_2_0_0.get_feature import WfsGetFeature


@pytest.fixture
def wfs_get_feature():
    return WfsGetFeature("maps", "http://localhost/", None, None, None, [])


@pytest.fixture
def layer_crs(crs_factory):
    return crs_factory(2056)


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

    def test_matching_srs_name_returns_other_crs(self, wfs_get_feature, layer_crs, crs_factory):
        other_crs = crs_factory(4326, axis_inverted=True)
        resolved_crs = wfs_get_feature.resolve_srs_name(
            "urn:ogc:def:crs:EPSG::4326", [layer_crs, other_crs]
        )
        assert resolved_crs is other_crs

    def test_rejection_with_crs_without_identifiers(self, wfs_get_feature, layer_crs, crs_factory):
        with pytest.raises(AttributeError) as error:
            wfs_get_feature.resolve_srs_name("EPSG:4326", [layer_crs, crs_factory(None)])
        assert "InvalidParameterValue" in str(error.value)

    def test_other_srs_name_is_rejected(self, wfs_get_feature, layer_crs):
        with pytest.raises(AttributeError) as error:
            wfs_get_feature.resolve_srs_name("EPSG:4326", [layer_crs])
        assert "InvalidParameterValue" in str(error.value)
        assert "EPSG:4326" in str(error.value)


class TestWfsOperationSupportedCrs:
    def test_layer_crs_first_then_configured(self, wfs_get_feature, layer_crs, crs_factory):
        Config.resolved_other_crs["maps"] = [crs_factory(3857), crs_factory(4326)]
        supported_crs = wfs_get_feature.supported_crs(layer_crs)
        assert [crs.auth_id for crs in supported_crs] == ["EPSG:2056", "EPSG:3857", "EPSG:4326"]

    def test_layer_crs_is_not_duplicated(self, wfs_get_feature, crs_factory):
        Config.resolved_other_crs["maps"] = [crs_factory(3857), crs_factory(4326)]
        supported_crs = wfs_get_feature.supported_crs(crs_factory(4326))
        assert [crs.auth_id for crs in supported_crs] == ["EPSG:4326", "EPSG:3857"]

    def test_configured_per_app(self, layer_crs, crs_factory):
        Config.resolved_other_crs["webgis"] = [crs_factory(21781)]
        wfs_get_feature = WfsGetFeature("webgis", "http://localhost/", None, None, None, [])
        supported_crs = wfs_get_feature.supported_crs(layer_crs)
        assert [crs.auth_id for crs in supported_crs] == ["EPSG:2056", "EPSG:21781"]

    def test_not_resolved(self, wfs_get_feature, layer_crs):
        del Config.resolved_other_crs["maps"]
        with pytest.raises(RuntimeError):
            wfs_get_feature.supported_crs(layer_crs)


class TestWfsGetFeatureSwapAxis:
    @pytest.mark.parametrize(
        "code, axis_inverted, expected_srs_name, expected_swap",
        [
            (4326, True, "http://www.opengis.net/def/crs/EPSG/0/4326", True),
            (2056, False, "http://www.opengis.net/def/crs/EPSG/0/2056", False),
            (3857, False, "http://www.opengis.net/def/crs/EPSG/0/3857", False),
        ],
    )
    def test_decision(self, crs_factory, code, axis_inverted, expected_srs_name, expected_swap):
        crs = crs_factory(code, axis_inverted=axis_inverted)
        assert WfsGetFeature.srs_name_of(crs) == expected_srs_name
        assert WfsGetFeature.swap_axis(crs) is expected_swap

    def test_crs_without_uri(self):
        crs = Crs(auth_id="IGNF:LAMB93", ogc_uri="", axis_inverted=True)
        assert WfsGetFeature.srs_name_of(crs) == "IGNF:LAMB93"
        assert WfsGetFeature.swap_axis(crs) is False

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


class TestWfsGetFeatureRendering:
    def test_inverted_axis_crs_labeled_with_uri_in_authority_order(
        self, wfs_get_feature, crs_factory
    ):
        output_crs = crs_factory(4326, axis_inverted=True)
        wfs_get_feature.feature_collection_srs = [wfs_get_feature.srs_name_of(output_crs)]
        wfs_get_feature.feature_collection_swap_axis = [wfs_get_feature.swap_axis(output_crs)]
        query_collection = QueryCollection(
            feature_collections=[
                FeatureCollection(
                    name="1ddbab8a-ce60-4907-bf13-4f12e573b14d",
                    features=[
                        Feature(geometry=Geometry(value=struct.pack("<BI2d", 1, 1, 7.12, 47.05)))
                    ],
                )
            ]
        )
        result = JobResult(
            id="job",
            data=JsonSerializer().render(query_collection).encode(),
            content_type="application/json",
        )

        xml = wfs_get_feature.render_xml(wfs_get_feature.get_feature(result), [])

        assert 'srsName="http://www.opengis.net/def/crs/EPSG/0/4326"' in xml
        assert "<gml:pos>47.05 7.12</gml:pos>" in xml
