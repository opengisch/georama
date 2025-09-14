import json
from datetime import datetime
from io import BytesIO
from unittest.mock import Mock, patch

import numpy as np
import pytest
from qgis_server_light.interface.job import QslGetFeatureJob
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from georama.data_integration.models import VectorDataSet
from georama.maps.interfaces.ogc import wfs_2_0_0
from georama.maps.interfaces.ogc.wfs_2_0_0.match_action_type import MatchActionType
from georama.maps.interfaces.ogc.wfs_2_0_0.query import Query
from georama.maps.interfaces.opengis.gml_3_2_1.direct_position_type import (
    DirectPositionType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.envelope import Envelope
from georama.maps.interfaces.opengis.gml_3_2_1.pos import Pos
from georama.maps.services.wfs_2_0_0.get_feature import NumpyArrayConverter


def get_lcs(obj):
    return obj.localised_character_string.value


class TestWfsGetFeature:
    def test_allowed_formats(self, wfs_get_feature):
        expected = [
            "APPLICATION/GML+XML; VERSION=3.2",
            "GML3",
            "TEXT/XML",
            "APPLICATION/JSON",
            "TEXT/JSON",
        ]
        assert wfs_get_feature.allowed_formats == expected

    def test_obtain_accessible_layers(self, wfs_get_feature):
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
        layer_vector_one = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=True,
            vector_dataset=Mock(spec=VectorDataSet),
        )
        # Second accessible vector layer
        layer_vector_two = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=True,
            vector_dataset=Mock(spec=VectorDataSet),
        )

        layer_vector_one.configure_mock(**{"name": "one"})
        layer_vector_two.configure_mock(**{"name": "two"})
        layer_vector_no_read.configure_mock(**{"name": "no_read"})

        all_vectors = [
            layer_vector_no_read,
            layer_vector_not_queryable,
            layer_vector_one,
            layer_vector_two,
        ]

        wfs_get_feature.model = Mock()

        # No filtering
        wfs_get_feature.model.objects.exclude.return_value = Mock(
            all=Mock(
                return_value=all_vectors,
            )
        )
        layers = wfs_get_feature.obtain_accessible_layers([])
        assert layers == [layer_vector_one, layer_vector_two]

        # Filtering - successful
        wfs_get_feature.model.objects.exclude.return_value = Mock(
            filter=Mock(
                return_value=Mock(
                    all=Mock(return_value=[layer_vector_one]),
                ),
            )
        )
        layers = wfs_get_feature.obtain_accessible_layers(["one"])
        assert layers == [layer_vector_one]

        # Filtering - layer not found
        wfs_get_feature.model.objects.exclude.return_value = Mock(
            filter=Mock(
                return_value=Mock(
                    all=Mock(return_value=[]),
                ),
            )
        )
        with pytest.raises(AttributeError) as excinfo:
            wfs_get_feature.obtain_accessible_layers(["doesnt-exist"])

        assert "Layer(s) not found: ['doesnt-exist']" in str(excinfo.value)

        # Filtering - layer not found
        wfs_get_feature.model.objects.exclude.return_value = Mock(
            filter=Mock(
                return_value=Mock(
                    all=Mock(return_value=[layer_vector_one, layer_vector_no_read])
                ),
            )
        )
        with pytest.raises(PermissionError) as excinfo:
            wfs_get_feature.obtain_accessible_layers(["one", "no_read"])

        assert "Layer(s) not permitted: ['no_read']" in str(excinfo.value)

    def test_prepare_filter_element(self, wfs_get_feature, simple_filter):
        fes_filter = wfs_get_feature.prepare_filter_element(simple_filter)

        expected = wfs_2_0_0.Filter(
            choice=[
                wfs_2_0_0.PropertyIsGreaterThan(
                    literal_or_function_or_value_reference=[
                        wfs_2_0_0.ValueReference(value="fid"),
                        wfs_2_0_0.Literal(type_value=None, content=["1"]),
                    ],
                    match_case=True,
                    match_action=MatchActionType.ANY,
                ),
            ]
        )
        assert fes_filter == expected

    def test_check_filter_empty(self, wfs_get_feature):
        empty_filter = wfs_2_0_0.Filter()
        assert wfs_get_feature.check_filter_empty(empty_filter) is True

        non_empty_filter = wfs_2_0_0.Filter(
            choice=[
                wfs_2_0_0.PropertyIsGreaterThan(
                    literal_or_function_or_value_reference=[
                        wfs_2_0_0.ValueReference(value="fid"),
                        wfs_2_0_0.Literal(type_value=None, content=["1"]),
                    ],
                ),
            ]
        )
        assert wfs_get_feature.check_filter_empty(non_empty_filter) is False

    def test_prepare_queries_type_names(self, wfs_get_feature):
        # Type names are required
        with pytest.raises(AttributeError) as excinfo:
            wfs_get_feature.prepare_queries({})
        assert "TypeNames is a mandatory parameter!" in str(excinfo.value)

        # Valid type names
        query_params = {
            "TYPENAMES": "georama:layer1,georama:layer2",
        }

        queries = wfs_get_feature.prepare_queries(query_params)
        assert queries == [
            Query(
                handle=None,
                property_name=[],
                filter=None,
                sort_by=None,
                type_names=["georama:layer1", "georama:layer2"],
                aliases=[],
                srs_name=None,
                feature_version=None,
            )
        ]

    def test_prepare_queries_list_encoding(self, wfs_get_feature, simple_filter):
        # List encoded alias params must be the same length
        query_params = {
            "TYPENAMES": "(ns1:F1,ns2:F2)",
            "ALIASES": "(A,B)(C,D)",
        }

        with pytest.raises(AttributeError) as excinfo:
            wfs_get_feature.prepare_queries(query_params)

        assert "List encoded params have to be same lenght!" in str(excinfo.value)

        # List encoded filter params must be same length
        query_params = {
            "TYPENAMES": "(ns1:F1,ns2:F2)",
            "FILTER": "(f1,f2)(f3,f4)",
        }

        with pytest.raises(AttributeError) as excinfo:
            wfs_get_feature.prepare_queries(query_params)

        assert "List encoded params have to be same lenght!" in str(excinfo.value)

        # Valid combination of list encoded typenames, aliases and filters
        query_params = {
            "TYPENAMES": "(ns1:F1,ns1:F2)(ns2:F1,ns2:F1)",
            "ALIASES": "(A,B)(C,D)",
            "FILTER": f"({simple_filter},{simple_filter})({simple_filter},{simple_filter})",
        }

        queries = wfs_get_feature.prepare_queries(query_params)
        query = queries[0]

        assert query.type_names == ["ns1:F1", "ns1:F2"]
        assert query.aliases == ["A", "B"]
        assert isinstance(query.filter, wfs_2_0_0.Filter)

    def test_prepare_queries_aliases(self, wfs_get_feature):
        # Aliases must be same length
        query_params = {
            "TYPENAMES": "georama:layer1,georama:layer2",
            "ALIASES": "t1",
        }

        with pytest.raises(AttributeError) as excinfo:
            wfs_get_feature.prepare_queries(query_params)

        assert "List of aliases and typenames has to be of same length." in str(excinfo.value)

        # Valid aliases
        query_params = {
            "TYPENAMES": "georama:layer1,georama:layer2",
            "ALIASES": "t1,t2",
        }

        queries = wfs_get_feature.prepare_queries(query_params)
        assert queries == [
            Query(
                handle=None,
                property_name=[],
                filter=None,
                sort_by=None,
                type_names=["georama:layer1", "georama:layer2"],
                aliases=["t1", "t2"],
                srs_name=None,
                feature_version=None,
            )
        ]

    def test_prepare_queries_filters(self, wfs_get_feature, simple_filter):
        # Filter params
        query_params = {
            "TYPENAMES": "georama:layer1,georama:layer2",
            "FILTER": simple_filter,
        }

        queries = wfs_get_feature.prepare_queries(query_params)
        query = queries[0]

        assert query.filter == wfs_2_0_0.Filter(
            choice=[
                wfs_2_0_0.PropertyIsGreaterThan(
                    literal_or_function_or_value_reference=[
                        wfs_2_0_0.ValueReference(value="fid"),
                        wfs_2_0_0.Literal(type_value=None, content=["1"]),
                    ],
                    match_case=True,
                    match_action=MatchActionType.ANY,
                )
            ]
        )

    def test_prepare_queries_with_bbox(self, wfs_get_feature, simple_filter):
        # Bounding box with SRS
        query_params = {
            "TYPENAMES": "georama:layer1,georama:layer2",
            "BBOX": "1,2,3,4,URN:OGC:DEF:CRS:EPSG::4326",
            "FILTER": simple_filter,
        }

        queries = wfs_get_feature.prepare_queries(query_params)
        query = queries[0]

        assert isinstance(query.filter, wfs_2_0_0.Filter)
        assert query.filter.bbox == wfs_2_0_0.Bbox(
            choice=[
                wfs_2_0_0.ValueReference(value="georama:layer1"),
                wfs_2_0_0.ValueReference(value="georama:layer2"),
                Envelope(
                    lower_corner=DirectPositionType(
                        value=["1", "2"],
                        srs_name=None,
                        srs_dimension=None,
                        axis_labels=[],
                        uom_labels=[],
                    ),
                    upper_corner=DirectPositionType(
                        value=["3", "4"],
                        srs_name=None,
                        srs_dimension=None,
                        axis_labels=[],
                        uom_labels=[],
                    ),
                    pos=[],
                    coordinates=None,
                    # XXX: This is a bug that needs to be fixed. CRS at the end of BBOX never gets respected.
                    srs_name=None,
                    srs_dimension=2,
                    axis_labels=[],
                    uom_labels=[],
                ),
            ]
        )

    def test_prepare_queries_without_bbox(self, wfs_get_feature, simple_filter):
        # Bounding box without SRS defaults to request SRS
        query_params = {
            "TYPENAMES": "georama:layer1,georama:layer2",
            "BBOX": "1,2,3,4",
            "FILTER": simple_filter,
            "SRSNAME": "URN:OGC:DEF:CRS:EPSG::4326",
        }

        queries = wfs_get_feature.prepare_queries(query_params)
        query = queries[0]

        assert isinstance(query.filter, wfs_2_0_0.Filter)
        envelope = query.filter.bbox.choice[2]

        assert envelope.srs_name == "URN:OGC:DEF:CRS:EPSG::4326"

    def test_query_parameters_to_get_feature_request(self, wfs_get_feature):
        query_params = {
            "TYPENAMES": "layer1,layer2,layer3",
            "VERSION": "2.0.0",
        }
        wfs_get_feature.query_parameters_to_get_feature_request(query_params)

    def test_prepare_feature_collection(self, wfs_get_feature):
        collection = wfs_2_0_0.FeatureCollection()
        now = datetime.now()
        prepared = wfs_get_feature.prepare_feature_collection(collection)
        assert isinstance(prepared, wfs_2_0_0.FeatureCollection)
        assert prepared.number_returned == len(prepared.member)

        assert isinstance(prepared.time_stamp, XmlDateTime)
        assert prepared.time_stamp.year == now.year
        assert prepared.time_stamp.month == now.month
        assert prepared.time_stamp.day == now.day

    def test_unwrap_type_names(self, wfs_get_feature):
        q1 = Query(type_names=["georama:layer1", "georama:layer2"])
        q2 = Query(type_names=["georama:layer2", "georama:layer3"])
        get_feature_params = wfs_2_0_0.GetFeature(stored_query_or_query=[q1, q2])

        type_names = wfs_get_feature.unwrap_type_names(get_feature_params, unique=False)
        assert type_names == [
            "georama:layer1",
            "georama:layer2",
            "georama:layer2",
            "georama:layer3",
        ]

        type_names = wfs_get_feature.unwrap_type_names(get_feature_params, unique=True)
        assert type_names == [
            "georama:layer1",
            "georama:layer2",
            "georama:layer3",
        ]

    def test_getfeature_to_qslgetfeaturejob(self, wfs_get_feature, mock_layer, simple_filter):

        obtain_layers_method = (
            "georama.maps.services.wfs_2_0_0.get_feature."
            "WfsGetFeature.obtain_accessible_layers"
        )
        with patch(obtain_layers_method) as mock_get:
            mock_get.return_value = [mock_layer]

            # Basic Query
            get_feature_params = wfs_2_0_0.GetFeature(
                stored_query_or_query=[
                    Query(
                        type_names=["georama:TestPointLayer_1234_5678"],
                    )
                ],
                start_index=7,
                count=42,
            )
            job1 = wfs_get_feature.getfeature_to_qslgetfeaturejob(get_feature_params)

            assert isinstance(job1, QslGetFeatureJob)
            assert len(job1.queries) == 1
            assert job1.queries[0].datasets == [mock_layer.vector_dataset.to_qsl]
            assert job1.start_index == 7
            assert job1.count == 42

            # Query with filter
            fes_filter = wfs_get_feature.prepare_filter_element(simple_filter)
            get_feature_params = wfs_2_0_0.GetFeature(
                stored_query_or_query=[
                    Query(
                        type_names=["georama:TestPointLayer_1234_5678"],
                        filter=fes_filter,
                    )
                ]
            )
            job2 = wfs_get_feature.getfeature_to_qslgetfeaturejob(get_feature_params)

            assert isinstance(job2, QslGetFeatureJob)
            assert len(job2.queries) == 1
            query = job2.queries[0]

            assert query.datasets == [mock_layer.vector_dataset.to_qsl]
            assert wfs_get_feature.prepare_filter_element(query.filter) == fes_filter

            # Query with filter and multiple layers
            mock_get.return_value = [mock_layer, mock_layer]
            get_feature_params = wfs_2_0_0.GetFeature(
                stored_query_or_query=[
                    Query(
                        type_names=["georama:TestPointLayer_1234_5678"],
                        filter=wfs_get_feature.prepare_filter_element(simple_filter),
                    )
                ]
            )
            with pytest.raises(AttributeError) as excinfo:
                wfs_get_feature.getfeature_to_qslgetfeaturejob(get_feature_params)

            assert (
                "Currently QGIS-Server-Light does not support querying multiple "
                "layers in one query and passing a filter on that." in str(excinfo.value)
            )

    def test_render_xml(self, wfs_get_feature):
        feature_collection = wfs_2_0_0.FeatureCollection()
        requested_typenames = ["georama:layer1"]

        rendered = wfs_get_feature.render_xml(
            feature_collection=feature_collection,
            requested_typenames=requested_typenames,
        )
        assert isinstance(rendered, str)
        assert "<FeatureCollection" in rendered

    def test_render_json(self, wfs_get_feature):
        feature_collection = wfs_2_0_0.FeatureCollection()

        rendered = wfs_get_feature.render_json(
            feature_collection=feature_collection,
        )
        assert isinstance(rendered, str)
        assert isinstance(json.loads(rendered), dict)

    def test_render(self, wfs_get_feature):
        render_xml = Mock(return_value=("content"))
        render_json = Mock(return_value=("content"))

        wfs_get_feature.render_xml = render_xml
        wfs_get_feature.render_json = render_json

        requested_typenames = ["georama:layer1"]
        feature_collection = wfs_2_0_0.FeatureCollection()

        expectations = [
            (
                "TEXT/XML",
                "text/xml; charset=utf-8",
                render_xml,
                (feature_collection, requested_typenames),
            ),
            (
                "APPLICATION/GML+XML; VERSION=3.2",
                "application/gml+xml; version=3.2; charset=utf-8",
                render_xml,
                (feature_collection, requested_typenames),
            ),
            (
                "GML3",
                "application/gml+xml; version=3.2; charset=utf-8",
                render_xml,
                (feature_collection, requested_typenames),
            ),
            (
                "APPLICATION/JSON",
                "application/json; charset=utf-8",
                render_json,
                (feature_collection,),
            ),
            (
                "TEXT/JSON",
                "text/json; charset=utf-8",
                render_json,
                (feature_collection,),
            ),
        ]

        for format, content_type, render_method, args in expectations:
            render_xml.reset_mock()
            render_json.reset_mock()
            result = wfs_get_feature.render(
                requested_format=format,
                feature_collection=feature_collection,
                requested_typenames=requested_typenames,
            )
            render_method.assert_called_with(*args)
            assert result[1:] == (content_type, True)

        failure_response = wfs_get_feature.render(
            "UNKNOWN", feature_collection, requested_typenames
        )
        assert "Format UNKNOWN is not allowed" in failure_response[0]
        assert failure_response[1] == "text/xml; charset=utf-8"
        assert failure_response[2] is False


class TestWfsNumpyArrayConverter:
    def test_converter_serialization(self):
        converter = NumpyArrayConverter()
        arr = np.array([8.04829301, 47.39112107])
        assert converter.serialize(arr) == "8.04829301 47.39112107"

    def test_converter_deserialization(self):
        converter = NumpyArrayConverter()
        value = "8.04829301 47.39112107"
        assert (
            converter.deserialize(value, types=[np.ndarray])
            == np.array([8.04829301, 47.39112107])
        ).all()

    def test_xsdata_serialization(self):
        serializer = XmlSerializer(config=SerializerConfig(xml_declaration=False))
        pos = Pos(np.array([8.04829301, 47.39112107]))
        rendered = serializer.render(pos)
        assert (
            rendered
            == '<ns0:pos xmlns:ns0="http://www.opengis.net/gml/3.2">8.04829301 47.39112107</ns0:pos>'
        )

    def test_xsdata_deserialization(self):
        xml = BytesIO(
            b'<ns0:pos xmlns:ns0="http://www.opengis.net/gml/3.2">8.04829301 47.39112107</ns0:pos>'
        )
        pos = XmlParser().parse(xml, Pos)
        assert (pos.value == np.array([8.04829301, 47.39112107])).all()
