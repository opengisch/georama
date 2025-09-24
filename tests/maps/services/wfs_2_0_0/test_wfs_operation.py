from unittest.mock import Mock

import pytest
from lxml import etree
from lxml.etree import QName

from georama.data_integration.models import VectorDataSet
from georama.maps.interfaces.ogc.wfs_2_0_0 import ExceptionReport


class TestWfsOperation:
    def assert_exception_text(self, exc, message):
        root = etree.fromstring(str(exc).encode("utf-8"))
        nsmap = {"": "http://www.opengis.net/ows/1.1"}
        txt = root.findall(".//ExceptionText", namespaces=nsmap)[-1].text
        assert txt == message

    def test_create_exception(self, wfs_op):
        exc = wfs_op.create_exception("test message")

        assert isinstance(exc, ExceptionReport)
        assert exc.version == "2.0.0"
        assert len(exc.exception) == 2

        exc1 = exc.exception[0]
        assert exc1.exception_code == "OperationParsingFailed"
        assert exc1.exception_text == ["It was not possible to process the request"]
        assert exc1.locator == "GetFeature"

        exc2 = exc.exception[1]
        assert exc2.exception_code == "InvalidParameterValue"
        assert exc2.exception_text == ["test message"]

    def test_render_exception(self, wfs_op):
        rendered = wfs_op.render_exception("test message")
        root = etree.fromstring(rendered.encode("utf-8"))

        NS_OWS = "http://www.opengis.net/ows/1.1"
        NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
        XSD_OWS = "http://schemas.opengis.net/ows/1.1.0/owsAll.xsd"

        nsmap = {
            None: NS_OWS,
            "xsi": NS_XSI,
        }
        assert root.nsmap == nsmap

        assert QName(root).localname == "ExceptionReport"
        assert root.attrib["version"] == "2.0.0"

        schema_loc = root.xpath("./@xsi:schemaLocation", namespaces={"xsi": NS_XSI})[0]
        assert sorted(schema_loc.split()) == [XSD_OWS, NS_OWS]

        exceptions = root.findall("Exception", namespaces=nsmap)
        assert len(exceptions) == 2

        exc1 = exceptions[0]
        assert exc1.attrib["exceptionCode"] == "OperationParsingFailed"
        assert exc1.attrib["locator"] == "GetFeature"
        exc1_texts = exc1.findall("ExceptionText", namespaces=nsmap)
        assert len(exc1_texts) == 1
        assert exc1_texts[0].text == "It was not possible to process the request"

        exc2 = exceptions[1]
        assert exc2.attrib["exceptionCode"] == "InvalidParameterValue"
        exc2_texts = exc2.findall("ExceptionText", namespaces=nsmap)
        assert len(exc2_texts) == 1
        assert exc2_texts[0].text == "test message"

    def test_sanitized_typenames_unprefixed_names(self, wfs_op):
        assert wfs_op.sanitized_typenames(["layer_1234"]) == ["layer_1234"]

    def test_sanitized_typenames_own_namespace(self, wfs_op):
        assert wfs_op.sanitized_typenames(["georama:layer_1234"]) == ["layer_1234"]

    def test_sanitized_typenames_foreign_namespace(self, wfs_op):
        with pytest.raises(AttributeError) as excinfo:
            wfs_op.sanitized_typenames(["foreign-namespace:layer_1234"])

        msg = (
            "Unknown feature type "
            "(wrong namespace? this server offers namespace 'georama'): "
            "wrongTypeName(s) => foreign-namespace:layer_1234"
        )
        self.assert_exception_text(excinfo.value, msg)

    def test_sanitized_typenames_invalid_format(self, wfs_op):
        with pytest.raises(AttributeError) as excinfo:
            wfs_op.sanitized_typenames(["foo:bar:layer_1234"])

        msg = (
            "Unknown feature type "
            "(wrong namespace? this server offers namespace 'georama'): "
            "wrongTypeName(s) => typename has unexpected format "
            "(expected '<namespace>:<name>') got foo:bar:layer_1234"
        )
        self.assert_exception_text(excinfo.value, msg)

    def test_obtain_accessible_layers(self, wfs_op, caplog):
        # No read permission
        layer_no_read = Mock(
            has_read_permission=Mock(return_value=False),
            queryable=True,
        )
        # Read permission but not queryable
        layer_not_queryable = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=False,
        )
        # Read permission, queryable, but not a VectorDataSet
        layer_read_query_but_no_vec = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=True,
        )
        # Accessible vector layer
        layer_vector = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=True,
            vector_dataset=Mock(spec=VectorDataSet),
        )

        wfs_op.model = Mock()
        wfs_op.model.objects.all.return_value = [
            layer_no_read,
            layer_not_queryable,
            layer_read_query_but_no_vec,
            layer_vector,
        ]

        layers = wfs_op.obtain_accessible_layers()
        assert layers == [layer_vector]

        assert [r.msg for r in caplog.records] == [
            "linked dataset has to be VectorDataSet for WFS 2.0.0, all others are ignored!",
        ]
