"""
This module implements necessary WFS 2.0 handling. It mainly deals with the interfaces of OGC and ISO.

In general, we have to handle 2 incoming request types:
  1. So called "ad-hoc" query which is a GET request where query parameters define the data extraction by
     key value pairs (KVP).
  2. Request originating to POST request where query content is passed as payload in the body.

In both cases we need to parse these inputs into the interface for WFS 2.0 GetFeature requests: `GetFeature`

```m̀ermaid
flowchart

get["GET"]
post["POST"]
xsdata["xsdata"]
wfsgetfeature["WfsGetFeature"]
getfeature_class["GetFeature"]
get-->wfsgetfeature
wfsgetfeature-->getfeature_class
post-->xsdata-->getfeature_class
```
"""

import datetime
import logging
import re
from dataclasses import field, make_dataclass
from typing import List, Tuple, Union

from geomet import wkb
from qgis_server_light.interface.job import FeatureQuery, JobResult, QslGetFeatureJob
from qgis_server_light.interface.qgis import QueryCollection
from xsdata.formats.dataclass.parsers import JsonParser, XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from georama.maps.interfaces.iso.tc211.gmd.dataclasses import (
    DirectPositionType,
    Envelope,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.bbox import Bbox
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.filter import Filter
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.value_reference import (
    ValueReference,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2 import (
    FeatureCollection,
    GetFeature,
    Member,
    Query,
)
from georama.maps.interfaces.opengis.gml_3_2_1 import (
    Exterior,
    GeometryMember,
    GeometryMembers,
    Interior,
    LinearRing,
    LineString,
    MultiPoint,
    Point,
    PointMembers,
    Polygon,
)
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation


class WfsGetFeature(WfsOperation):
    def __init__(self, appname: str, url: str, user):
        super().__init__(appname, url, user)
        self.name_space_map = {
            "wfs": "http://www.opengis.net/wfs/2.0",
            "fes": "http://www.opengis.net/fes/2.0",
            "ows": "http://www.opengis.net/ows/1.1",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "georama": "https://www.opengis.ch/georama",
            "gml": "http://www.opengis.net/gml/3.2",
        }

    @property
    def allowed_formats(self) -> List[str]:
        return [
            "APPLICATION/GML+XML; VERSION=3.2",
            "TEXT/XML",
            "APPLICATION/JSON",
            "TEXT/JSON",
        ]

    def obtain_accessible_layers(self, layer_names: List[str] | None = None):
        accessible_layers = []
        # we do want only published vector datasets!
        query = PublishedAsWms.objects.exclude(vector_dataset__isnull=True)
        if layer_names:
            query = query.filter(name__in=layer_names)
        found_layers = query.all()
        found_difference = set(layer_names) - {layer.name for layer in found_layers}
        if len(found_difference) > 0:
            raise AttributeError(f"Layer(s) not found: {list(found_difference)}")
        for published_as in found_layers:
            if published_as.has_read_permission(self.user, self.appname):
                accessible_layers.append(published_as)
        permission_difference = set(layer_names) - {layer.name for layer in accessible_layers}
        if len(permission_difference) > 0:
            raise PermissionError(f"Layer(s) not permitted: {list(permission_difference)}")
        return accessible_layers

    def handle_list_encoding(self, parameter_value: str) -> List[str]:
        pattern = r"\((.+?)\)"
        matches = re.findall(pattern, parameter_value)
        if len(matches) == 0:
            # typenames is not list encoded, we handle it as simple comma separated string
            return [parameter_value]
        else:
            return matches

    def prepare_filter_element(self, filter_definition: str) -> Filter:
        config = ParserConfig()
        parser = XmlParser(config=config)
        return parser.parse(filter_definition, Filter)

    def prepare_queries(self, query_params: dict) -> List[Query]:

        """
        This implements the part of the spec to construct a query object out of simple KVP (key value pair)
        encoded parameters from GET URL request.

        It mainly is about chapter 6.2.5.3 of the spec PDF.

        This list encoded query:
        TYPENAMES=(ns1:F1,ns2:F2)(ns1:F1,ns1:F1)&ALIASES=(A,B)(C,D)&FILTER=(<Filter> … for A,B … </Filter>)(<Filter>…for C,D…</Filter>)
        should be handled the same as this 2 separate would do:
        TYPENAMES=ns1:F1,ns2:F2&ALIASES=A,B&FILTER=<Filter>…for A,B…</Filter>
        TYPENAMES=ns1:F1,ns1:F1&ALIASES=C,D&FILTER=<Filter>…for C,D…</Filter>
        Args:
            query_params ():

        Returns:
            The prepared queries
        """

        type_names_param_value = query_params.get("TYPENAMES")
        aliases_param_value = query_params.get("ALIASES")
        filter_param_value = query_params.get("FILTER")
        srs_name = query_params.get("SRSNAME")
        bbox_definition = query_params.get("BBOX")
        queries = []
        if type_names_param_value:
            # we have typenames in the query
            type_names_lists = self.handle_list_encoding(type_names_param_value)
        else:
            raise AttributeError("TypeNames is a mandatory parameter!")
        if aliases_param_value:
            # we have aliases in the query
            aliases_lists = self.handle_list_encoding(aliases_param_value)
            if aliases_lists:
                if not len(aliases_lists) == len(type_names_lists):
                    raise AttributeError("List encoded params have to be same lenght!")
        else:
            # no filters were passed, we create an empty list of same length as type_names
            aliases_lists = [None] * len(type_names_lists)
        if filter_param_value:
            # we have filters in the query
            filters_lists = self.handle_list_encoding(filter_param_value)
            if filters_lists:
                if not len(filters_lists) == len(type_names_lists):
                    raise AttributeError("List encoded params have to be same lenght!")
        else:
            # no filters were passed, we create an empty list of same length as type_names
            filters_lists = [None] * len(type_names_lists)

        combined_lists = zip(type_names_lists, aliases_lists, filters_lists)
        for type_names, aliases, filter_definition in combined_lists:
            type_names_value_list = type_names.split(",")
            if aliases:
                aliases_value_list = aliases.split(",")
                if len(type_names_value_list) != len(aliases_value_list):
                    raise AttributeError(
                        "List of aliases and typenames has to be of same length. Situation is:"
                        f" typenames: {type_names_value_list}, length: {len(type_names_value_list)}"
                        f" aliases: {aliases_value_list}, length: {len(aliases_value_list)}"
                    )
            else:
                aliases_value_list = []
            if filter_definition or bbox_definition:
                if filter_definition:
                    fes_filter = self.prepare_filter_element(filter_definition)
                else:
                    fes_filter = Filter()
                # we expect one optional BBOX which is assigned to all passed typenames! This aligns with
                # spec as it 7.9.2.3 of the spec doc. However, there is one example wich supports that B.8.5.4
                # and one which states a conflicting situation B.8.5.5
                # TODO: Check how the conflict can be explained?
                fes_filter.bbox = Bbox(
                    value_reference=[
                        ValueReference(type_name) for type_name in type_names_value_list
                    ],
                    other_element=[
                        Envelope(
                            lower_corner=DirectPositionType(value=[]),
                            upper_corner=DirectPositionType(value=[]),
                        )
                    ],
                )
            else:
                fes_filter = None

            queries.append(
                Query(
                    srs_name=srs_name,
                    type_names=type_names_value_list,
                    aliases=aliases_value_list,
                    filter=fes_filter,
                )
            )
        return queries

    def query_parameters_to_get_feature_request(self, query_params: dict) -> GetFeature:
        return GetFeature(
            version=query_params["VERSION"],
            query=self.prepare_queries(query_params),
            start_index=query_params.get("STARTINDEX"),
            count=query_params.get("COUNT"),
            output_format=query_params.get(
                "OUTPUTFORMAT", "APPLICATION/GML+XML; VERSION=3.2"
            ).upper(),
        )

    def prepare_feature_collection(self, feature_collection: FeatureCollection):
        """
        Used to alter the feature collection with additional runtime configuration.

        Args:
            feature_collection: The feature collection which should be altered.

        Returns:
            The altered feature collection.
        """
        now = datetime.datetime.now()
        feature_collection.time_stamp = XmlDateTime(
            year=now.year,
            month=now.month,
            day=now.day,
            hour=now.hour,
            minute=now.minute,
            second=now.second,
        )
        feature_collection.number_returned = len(feature_collection.member)
        return feature_collection

    def unwrap_type_names(
        self, get_feature_params: GetFeature, unique: bool = True
    ) -> List[str]:
        """
        Get a list of all typenames
        Args:
            get_feature_params: The parameter how it was taken from request
            unique: If the list should not contain duplicates
        Returns:
            flat list of type names
        """
        type_names = []
        for query in get_feature_params.query:
            if unique:
                for type_name in query.type_names:
                    if type_name not in type_names:
                        type_names.append(type_name)
            else:
                type_names.extend(query.type_names)
        return type_names

    def getfeature_to_qslgetfeaturejob(
        self, get_feature_parameter: GetFeature
    ) -> QslGetFeatureJob:
        qsl_feature_queries = []
        for query in get_feature_parameter.query:
            qsl_feature_queries.append(
                FeatureQuery(
                    datasets=[
                        layer.vector_dataset.to_qsl
                        for layer in self.obtain_accessible_layers(query.type_names)
                    ],
                    alias=query.aliases,
                    filter=XmlSerializer().render(query.filter, ns_map=self.name_space_map)
                    if query.filter
                    else None,
                )
            )
        return QslGetFeatureJob(
            start_index=get_feature_parameter.start_index,
            count=get_feature_parameter.count,
            queries=qsl_feature_queries,
        )

    def prepare_geometry(
        self, geometry_wkb_definition: bytes, get_feature_parameter: GetFeature
    ) -> GeometryMember | GeometryMembers:
        geojson_dict = wkb.loads(geometry_wkb_definition)
        srs_name = get_feature_parameter.query[0].srs_name.lower()
        if geojson_dict["type"] == "Point":
            return GeometryMember(
                point=Point(srs_name=srs_name, pos=" ".join(geojson_dict["coordinates"]))
            )
        elif geojson_dict["type"] == "MultiPoint":
            point_members = []
            for point_pos in geojson_dict["coordinates"]:
                point_members.append(Point(pos=" ".join(point_pos)))
            return GeometryMembers(
                multi_point=[
                    MultiPoint(
                        srs_name=srs_name, point_members=PointMembers(point=point_members)
                    )
                ]
            )
        elif geojson_dict["type"] == "LineString":
            return GeometryMember(
                line_string=LineString(
                    srs_name=srs_name, pos_list=" ".join(geojson_dict["coordinates"])
                )
            )
        elif geojson_dict["type"] == "MultiLineString":
            # TODO: ...
            raise NotImplementedError(f"Currently not implemented: {geojson_dict['type']}")
        elif geojson_dict["type"] == "Polygon":
            polygon = Polygon(
                srs_name=srs_name,
                exterior=Exterior(
                    linear_ring=LinearRing(
                        pos_list=" ".join(
                            [
                                " ".join(map(str, inner))
                                for inner in geojson_dict["coordinates"][0]
                            ]
                        )
                    )
                ),
            )
            if len(geojson_dict["coordinates"]) > 1:
                for interior in geojson_dict["coordinates"][1:]:
                    polygon.interior.append(
                        Interior(
                            linear_ring=LinearRing(
                                pos_list=" ".join(
                                    [" ".join(map(str, inner)) for inner in interior]
                                )
                            )
                        )
                    )
            return GeometryMember(polygon=polygon)
        elif geojson_dict["type"] == "MultiPolygon":
            # TODO: ...
            raise NotImplementedError(f"Currently not implemented: {geojson_dict['type']}")
        elif geojson_dict["type"] == "GeometryCollection":
            # TODO: ...
            raise NotImplementedError(f"Currently not implemented: {geojson_dict['type']}")
        else:
            raise NotImplementedError(f"Currently not implemented: {geojson_dict['type']}")

    def get_feature(self, get_feature_parameter: GetFeature, result: JobResult):
        wfs_feature_collection = FeatureCollection()
        qsl_query_collection = JsonParser().from_bytes(result.data, QueryCollection)

        class GeoramaMeta:
            namespace = "https://www.opengis.ch/georama"

        for feature_collection in qsl_query_collection.feature_collections:
            for index, feature in enumerate(feature_collection.features):
                fields = []
                feature_dict = {}
                for attribute in feature.attributes:
                    fields.append((attribute.name, type(attribute.value)))
                    feature_dict[attribute.name] = attribute.value
                fields.append(
                    (
                        "id",
                        str,
                        field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                                "namespace": "http://www.opengis.net/gml/3.2",
                            },
                        ),
                    )
                )
                fields.append(
                    ("geometry", Union[GeometryMember, GeometryMembers], field(default=None))
                )
                feature_dataclass = make_dataclass(feature_collection.name, fields=fields)
                feature_dataclass.Meta = GeoramaMeta
                feature_object = feature_dataclass(**feature_dict)
                feature_object.geometry = self.prepare_geometry(
                    feature.geometry_as_bytes(), get_feature_parameter
                )
                # this has to be unique
                # TODO: How do we do that? Using the PK of the data?
                feature_object.id = f"TEST.{index}"
                wfs_feature_collection.member.append(Member(content=[feature_object]))
        return wfs_feature_collection

    def render_xml(
        self, feature_collection: FeatureCollection, requested_typenames: List[str]
    ) -> str:
        serializer = XmlSerializer(
            config=SerializerConfig(
                xml_declaration=True,
                xml_version="1.0",
                ignore_default_attributes=True,
                schema_location=" ".join(
                    [
                        "https://www.opengis.ch/georama",
                        f"{self.url}SERVICE=WFS&VERSION=2.0.0&REQUEST=DescribeFeatureType&TYPENAME={','.join(requested_typenames)}",
                        "http://www.opengis.net/wfs/2.0",
                        "http://schemas.opengis.net/wfs/2.0/wfs.xsd",
                        "http://www.opengis.net/gml/3.2",
                        "http://schemas.opengis.net/gml/3.2.1/gml.xsd",
                    ]
                ),
            )
        )

        return serializer.render(feature_collection, ns_map=self.name_space_map)

    @staticmethod
    def render_json(feature_collection: FeatureCollection) -> str:
        serializer = JsonSerializer(
            SerializerConfig(ignore_default_attributes=True, pretty_print=True)
        )
        return serializer.render(feature_collection)

    def render(
        self,
        requested_format: str,
        feature_collection: FeatureCollection,
        requested_typenames: List[str],
    ) -> Tuple[str, str, bool]:
        if requested_format == "TEXT/XML":
            return (
                self.render_xml(feature_collection, requested_typenames),
                requested_format.lower(),
                True,
            )
        elif requested_format == "APPLICATION/GML+XML; VERSION=3.2":
            return (
                self.render_xml(feature_collection, requested_typenames),
                requested_format.lower(),
                True,
            )
        elif requested_format == "APPLICATION/JSON":
            return self.render_json(feature_collection), requested_format.lower(), True
        elif requested_format == "TEXT/JSON":
            return self.render_json(feature_collection), requested_format.lower(), True
        else:
            logging.debug("No matching Format was found.")
            return (
                self.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed. Allowed is {self.allowed_formats}"
                ),
                "text/xml",
                False,
            )
