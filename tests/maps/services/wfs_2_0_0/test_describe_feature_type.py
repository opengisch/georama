import json
from unittest.mock import Mock

from lxml import etree
from lxml.etree import QName
from xsdata.models.enums import FormType
from xsdata.models.xsd import (
    ComplexContent,
    ComplexType,
    Element,
    Extension,
    Import,
    Schema,
    Sequence,
)

from georama.data_integration.models import VectorDataSet
from georama.maps.models import PublishedAsWms


class TestWfsDescribeFeatureType:
    def test_allowed_formats(self, wfs_desc_ft):
        expected = [
            "APPLICATION/GML+XML; VERSION=3.2",
            "GML3" "TEXT/XML",
            "APPLICATION/JSON",
            "TEXT/JSON",
        ]
        assert wfs_desc_ft.allowed_formats == expected

    def test_obtain_accessible_layers(self, wfs_desc_ft):
        # No read permission
        layer_vector_no_read = Mock(
            has_read_permission=Mock(return_value=False),
            queryable=True,
            vector_dataset=Mock(spec=VectorDataSet),
        )
        # Read permission but not queryable
        layer_vector_not_queryable = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=False,
            vector_dataset=Mock(spec=VectorDataSet),
        )
        # Accessible vector layer
        layer_vector_foo = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=True,
            vector_dataset=Mock(spec=VectorDataSet),
        )
        # Second accessible vector layer
        layer_vector_bar = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=True,
            vector_dataset=Mock(spec=VectorDataSet),
        )

        wfs_desc_ft.model = Mock()
        wfs_desc_ft.model.objects.exclude.return_value = [
            layer_vector_no_read,
            layer_vector_not_queryable,
            layer_vector_foo,
            layer_vector_bar,
        ]

        # Unfiltered
        layers = wfs_desc_ft.obtain_accessible_layers()
        assert layers == [layer_vector_foo, layer_vector_bar]

        # Filtered
        wfs_desc_ft.model.objects.exclude.return_value = Mock(
            filter=Mock(return_value=[layer_vector_foo])
        )
        layers = wfs_desc_ft.obtain_accessible_layers(layer_names=["foo"])
        assert layers == [layer_vector_foo]

    def test_prepare_geometry_column(self, wfs_desc_ft, caplog):
        geom_types = {
            "Point": "gml:PointPropertyType",
            "Point25D": "gml:PointPropertyType",
            "LineString": "gml:LineStringPropertyType",
            "LineString25D": "gml:LineStringPropertyType",
            "Polygon": "gml:PolygonPropertyType",
            "Polygon25D": "gml:PolygonPropertyType",
            "MultiPoint": "gml:MultiPointPropertyType",
            "MultiPoint25D": "gml:MultiPointPropertyType",
            "MultiCurve": "gml:MultiCurvePropertyType",
            "MultiLineString": "gml:MultiCurvePropertyType",
            "MultiLineString25D": "gml:MultiCurvePropertyType",
            "MultiSurface": "gml:MultiSurfacePropertyType",
            "MultiPolygon": "gml:MultiSurfacePropertyType",
            "MultiPolygon25D": "gml:MultiSurfacePropertyType",
        }

        for geom_type, expected in geom_types.items():
            dataset = VectorDataSet(geometry_type_wkb=geom_type)
            assert wfs_desc_ft.prepare_geometry_column(dataset) == Element(
                name="geometry",
                type=expected,
                min_occurs=0,
                max_occurs=1,
            )

        # Unknown geometry type
        dataset = VectorDataSet(geometry_type_wkb="Unknown")
        assert wfs_desc_ft.prepare_geometry_column(dataset) == Element(
            name="geometry",
            type="gml:GeometryPropertyType",
            min_occurs=0,
            max_occurs=1,
        )

        assert [r.msg for r in caplog.records] == [
            "We casted to generic type since no match was available for type: 'Unknown'",
        ]

    def test_describe_feature_type(self, wfs_desc_ft):
        field_required_long = Mock(type_wfs="long", nullable=False)
        field_required_long.configure_mock(**{"name": "required_long"})

        field_optional_string = Mock(type_wfs="string", nullable=True)
        field_optional_string.configure_mock(**{"name": "optional_string"})

        layer_vector = Mock(
            spec=PublishedAsWms,
            has_read_permission=Mock(return_value=True),
            queryable=True,
            vector_dataset=Mock(
                spec=VectorDataSet,
                fields=Mock(
                    all=Mock(
                        return_value=[
                            field_required_long,
                            field_optional_string,
                        ]
                    )
                ),
            ),
        )
        layer_vector.configure_mock(**{"name": "mylayer"})
        wfs_desc_ft.obtain_accessible_layers = Mock(return_value=[layer_vector])

        expected = Schema(
            imports=[
                Import(
                    schema_location="http://schemas.opengis.net/gml/3.2.1/gml.xsd",
                    namespace="http://www.opengis.net/gml/3.2",
                )
            ],
            target_namespace="https://www.opengis.ch/georama",
            element_form_default=FormType.QUALIFIED,
            version="0.1",
            elements=[
                Element(
                    name="mylayer",
                    type="georama:mylayerType",
                    substitution_group="gml:AbstractFeature",
                )
            ],
            complex_types=[
                ComplexType(
                    name="mylayerType",
                    complex_content=ComplexContent(
                        extension=Extension(
                            base="gml:AbstractFeatureType",
                            sequence=Sequence(
                                elements=[
                                    Element(
                                        name="geometry",
                                        type="gml:GeometryPropertyType",
                                        min_occurs=0,
                                        max_occurs=1,
                                    ),
                                    Element(
                                        name="required_long",
                                        type="long",
                                        min_occurs=1,
                                        max_occurs=1,
                                        nillable=False,
                                    ),
                                    Element(
                                        name="optional_string",
                                        type="string",
                                        min_occurs=0,
                                        max_occurs=1,
                                        nillable=True,
                                    ),
                                ]
                            ),
                        )
                    ),
                )
            ],
        )
        assert wfs_desc_ft.describe_feature_type(None) == expected

    def test_describe_feature_type_respects_layer_names(self, wfs_desc_ft):
        obtain_accessible_layers = Mock(return_value=[])
        wfs_desc_ft.obtain_accessible_layers = obtain_accessible_layers

        # Should call obtain_accessible_layers() without args
        wfs_desc_ft.describe_feature_type(None)
        obtain_accessible_layers.assert_called_with()

        # Should call obtain_accessible_layers() with given layer list
        obtain_accessible_layers.reset_mock()
        wfs_desc_ft.describe_feature_type(["mylayer"])
        obtain_accessible_layers.assert_called_with(["mylayer"])

    def test_render_xml(self, wfs_desc_ft, described_feature_type):
        rendered = wfs_desc_ft.render_xml(described_feature_type)
        root = etree.fromstring(rendered.encode("utf-8"))

        assert root.tag == "{http://www.w3.org/2001/XMLSchema}schema"
        assert [QName(c).localname for c in root.getchildren()] == [
            "import",
            "complexType",
            "element",
        ]

    def test_render_json(self, wfs_desc_ft, described_feature_type):
        rendered = wfs_desc_ft.render_json(described_feature_type)
        described_feature = json.loads(rendered)

        assert sorted(described_feature.keys()) == [
            "annotation",
            "anyAttribute",
            "attribute",
            "attributeGroup",
            "complexType",
            "defaultOpenContent",
            "element",
            "elementFormDefault",
            "group",
            "import",
            "include",
            "notation",
            "override",
            "redefine",
            "simpleType",
            "targetNamespace",
            "version",
        ]

    def test_render(self, wfs_desc_ft):
        render_xml = Mock(return_value=("content"))
        render_json = Mock(return_value=("content"))

        wfs_desc_ft.render_xml = render_xml
        wfs_desc_ft.render_json = render_json

        expectations = [
            (
                "TEXT/XML",
                "text/xml",
                render_xml,
            ),
            (
                "APPLICATION/GML+XML; VERSION=3.2",
                "application/gml+xml; version=3.2",
                render_xml,
            ),
            (
                "GML3",
                "application/gml+xml; version=3.2",
                render_xml,
            ),
            (
                "APPLICATION/JSON",
                "application/json",
                render_json,
            ),
            (
                "TEXT/JSON",
                "text/json",
                render_json,
            ),
        ]

        dft = Mock()
        for format, content_type, render_method in expectations:
            render_xml.reset_mock()
            render_json.reset_mock()
            result = wfs_desc_ft.render(format, dft)
            render_method.assert_called_with(dft)
            assert result[1:] == (content_type, True)

        failure_response = wfs_desc_ft.render("UNKNOWN", dft)
        assert "Format UNKNOWN is not allowed" in failure_response[0]
        assert failure_response[1] == "text/xml"
        assert failure_response[2] is False
