import json
from unittest.mock import Mock, patch
from xml.etree.ElementTree import QName

from lxml import etree
from qgis_server_light.interface.qgis import BBox

from georama.data_integration.models import VectorDataSet
from georama.maps.interfaces.ogc import wfs_2_0_0


class TestWfsGetCapabilities:
    def test_allowed_formats(self, wfs_get_cap):
        expected = ["TEXT/XML", "APPLICATION/JSON"]
        assert wfs_get_cap.allowed_formats == expected

    def test_get_capabilities_body(self, wfs_get_cap):
        body = wfs_get_cap.get_capabilities_body()
        assert isinstance(body, wfs_2_0_0.WfsCapabilities)

        # Test that service URL is used as expected.
        # Rest of config is tested in test_maps_config.TestMapsConfig
        expected_url = wfs_get_cap.url

        operations = body.operations_metadata.operation
        for op in operations:
            for dcp in op.dcp:
                for http_method in dcp.http.get_or_post:
                    assert http_method.href == expected_url

    def test_create_feature_type(self, wfs_get_cap):
        crs = ("http://www.opengis.net/def/crs/EPSG/0/4326",)
        bbox = BBox(
            x_min=6.2305498123169,
            x_max=10.2997055053711,
            y_min=46.0072288513184,
            y_max=47.7490196228027,
            z_min=0.0,
            z_max=0.0,
        )
        result = wfs_get_cap.create_feature_type(
            name="georama:TestPointLayer_1234_5678",
            title="TestPointLayer",
            crs=crs,
            bbox=bbox,
            url="http://localhost:4242/maps?",
        )

        assert isinstance(result, wfs_2_0_0.FeatureTypeType)
        assert result.name == QName("georama:TestPointLayer_1234_5678")
        assert result.title == [wfs_2_0_0.Title2(value="TestPointLayer")]
        assert result.default_crs_or_other_crs_or_no_crs == [wfs_2_0_0.DefaultCrs(value=crs)]
        assert result.output_formats == wfs_2_0_0.OutputFormatListType(
            format=[
                "application/gml+xml; version=3.2",
                "text/xml; subtype=gml/3.2.1",
            ]
        )

        assert result.wgs84_bounding_box == [
            wfs_2_0_0.Wgs84BoundingBox(
                lower_corner=[bbox.x_min, bbox.y_min],
                upper_corner=[bbox.x_max, bbox.y_max],
            )
        ]

        assert result.metadata_url == [
            wfs_2_0_0.MetadataUrltype(
                href=(
                    "http://localhost:4242/maps?"
                    "request=GetMetadata&"
                    "layer=TestPointLayer_1234_5678"
                ),
            )
        ]

    @patch(
        "georama.maps.services.wfs_2_0_0.get_capabilities.WfsGetCapabilities.obtain_accessible_layers"
    )
    def test_get_capabilities(self, patched_obtain_layers, wfs_get_cap):
        dataset = Mock(
            spec=VectorDataSet,
            geometry_type_wkb="Point",
            crs={
                "AuthId": "EPSG:4326",
                "OgcUri": "http://www.opengis.net/def/crs/EPSG/0/4326",
                "OgcUrn": "urn:ogc:def:crs:EPSG::4326",
                "PostgisSrid": 4326,
            },
        )
        layer = Mock(
            title="Cities",
            vector_dataset=dataset,
            extent_wgs84=",".join(
                [
                    "6.2305498123169",
                    "46.0072288513184",
                    "10.2997055053711",
                    "47.7490196228027",
                ]
            ),
        )
        layer.configure_mock(**{"name": "TestPointLayer_1234_5678"})
        patched_obtain_layers.return_value = [layer]

        capabilities = wfs_get_cap.get_capabilities()
        assert isinstance(capabilities, wfs_2_0_0.WfsCapabilities)

        expected_feature_type_list = wfs_2_0_0.FeatureTypeList(
            feature_type=[
                wfs_2_0_0.FeatureTypeType(
                    name=QName("georama:TestPointLayer_1234_5678"),
                    title=[wfs_2_0_0.Title2(value="Cities", lang="en")],
                    default_crs_or_other_crs_or_no_crs=[
                        wfs_2_0_0.DefaultCrs(
                            value="http://www.opengis.net/def/crs/EPSG/0/4326"
                        )
                    ],
                    output_formats=wfs_2_0_0.OutputFormatListType(
                        format=[
                            "application/gml+xml; " "version=3.2",
                            "text/xml; " "subtype=gml/3.2.1",
                        ]
                    ),
                    wgs84_bounding_box=[
                        wfs_2_0_0.Wgs84BoundingBox(
                            lower_corner=[6.2305498123169, 46.0072288513184],
                            upper_corner=[10.2997055053711, 47.7490196228027],
                        )
                    ],
                    metadata_url=[
                        wfs_2_0_0.MetadataUrltype(
                            href=(
                                "http://localhost:4242/maps?"
                                "request=GetMetadata&"
                                "layer=TestPointLayer_1234_5678"
                            ),
                        )
                    ],
                    extended_description=None,
                )
            ]
        )

        expected_capabilities = wfs_get_cap.get_capabilities_body()
        expected_capabilities.feature_type_list = expected_feature_type_list
        assert capabilities == expected_capabilities

    def test_render_xml(self, wfs_get_cap):
        rendered = wfs_get_cap.render_xml(wfs_get_cap.get_capabilities_body())

        root = etree.fromstring(rendered.encode("utf-8"))
        assert root.tag == "{http://www.opengis.net/wfs/2.0}WFS_Capabilities"

    def test_render_json(self, wfs_get_cap):
        rendered = wfs_get_cap.render_json(wfs_get_cap.get_capabilities_body())
        capabilities = json.loads(rendered)

        assert capabilities["version"] == "2.0.0"
        assert sorted(capabilities.keys()) == [
            "FeatureTypeList",
            "Filter_Capabilities",
            "OperationsMetadata",
            "ServiceIdentification",
            "ServiceProvider",
            "WSDL",
            "updateSequence",
            "version",
        ]

    def test_render(self, wfs_get_cap):
        render_xml = Mock(return_value=("content"))
        render_json = Mock(return_value=("content"))

        wfs_get_cap.render_xml = render_xml
        wfs_get_cap.render_json = render_json

        expectations = [
            (
                "TEXT/XML",
                render_xml,
            ),
            (
                "APPLICATION/JSON",
                render_json,
            ),
        ]

        capabilities = Mock()
        for format, render_method in expectations:
            render_xml.reset_mock()
            render_json.reset_mock()

            result = wfs_get_cap.render(format, capabilities)
            render_method.assert_called_with(capabilities)
            assert result == "content"

        failure_response = wfs_get_cap.render("UNKNOWN", capabilities)
        assert failure_response is None
