"""
This module implements necessary WFS 2.0 handling. It mainly deals with the interfaces
of OGC and ISO.

In general, we have to handle 2 incoming request types:
  1. So called "ad-hoc" query which is a GET request where query parameters define the
    data extraction by key value pairs (KVP).
  2. Request originating to POST request where query content is passed as payload in
    the body.

In both cases we need to parse these inputs into the interface for WFS 2.0 GetFeature
requests: `GetFeature`

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
import time
from dataclasses import field, make_dataclass
from typing import Any

import numpy as np
from django.db.models import Model
from guardian.shortcuts import get_perms
from qgis_server_light.interface.job.common.input import OgcFilterFES20
from qgis_server_light.interface.job.common.output import JobResult
from qgis_server_light.interface.job.feature.input import FeatureQuery, QslJobParameterFeature
from qgis_server_light.interface.job.feature.output import QueryCollection
from xsdata.formats.converter import Converter, converter
from xsdata.formats.dataclass.parsers import JsonParser, XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from georama.maps.interfaces.georama.requests import handle_list_encoding
from georama.maps.interfaces.ogc.wfs_2_0_0 import (
    Bbox,
    FeatureCollection,
    Filter,
    GetFeature,
    Member,
    Query,
    ValueReference,
)
from georama.maps.interfaces.opengis.gml_3_2_1 import (
    CurveMembers,
    DirectPositionType,
    Envelope,
    Exterior,
    GeometryMember,
    GeometryMembers,
    Interior,
    LinearRing,
    LineString,
    MultiCurve,
    MultiPoint,
    MultiSurface,
    Point,
    PointMembers,
    Polygon,
    Pos,
    PosList,
    SurfaceMembers,
)
from georama.maps.models import WmsLayer
from georama.maps.services.wfs_2_0_0 import WfsOperation


class NumpyArrayConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> np.ndarray:
        return np.fromstring(value, dtype=float, sep=" ")

    def serialize(self, value: Any, **kwargs: Any) -> str | None:
        if isinstance(value, np.ndarray):
            return " ".join(value.astype(str))


converter.register_converter(np.ndarray, NumpyArrayConverter())


class WfsGetFeature(WfsOperation):
    def __init__(self, appname: str, url: str, user, model: Model):
        super().__init__(appname, url, user, model)
        self.name_space_map = {
            "": "http://www.opengis.net/wfs/2.0",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "gml": "http://www.opengis.net/gml/3.2",
            self.own_namespace: self.own_namespace_domain,
        }
        self.geometry_types = {
            "point": [1, 1001, 2001, 3001],
            "linestring": [2, 1002, 2002, 3002],
            "polygon": [3, 1003, 2003, 3003],
            "multipoint": [4, 1004, 2004, 3004],
            "multilinestring": [5, 1005, 2005, 3005],
            "multipolygon": [6, 1006, 2006, 3006],
            "geometrycollection": [7, 1007, 2007, 3007],
        }

    @property
    def allowed_formats(self) -> list[str]:
        return [
            "APPLICATION/GML+XML; VERSION=3.2",
            "GML3",
            "TEXT/XML",
            "APPLICATION/JSON",
            "TEXT/JSON",
        ]

    def obtain_accessible_layers(self, layer_names: list[str] | None = None) -> list[WmsLayer]:
        """
        This method derives the layers which are available for WFS operation.
        This Method solves multiple purposes:
            1. Find configured VECTOR layers from Georama database
            2. Check if layers queried in request but not configured in Georama database
            3. Check permissions of layers
        Args:
            layer_names: Optional list of layer names which are checked against the
                Georama database (default: None)

        Returns:
            List of accessible layers.
        """
        accessible_layers = []
        # we do want only published vector datasets!
        query = self.model.objects.filter(datasource__vector__isnull=False)
        if layer_names:
            query = query.filter(id__in=layer_names)
        found_layers = query.all()
        found_difference = set(layer_names) - {layer.identifier for layer in found_layers}
        if len(found_difference) > 0:
            raise AttributeError(
                self.render_exception(f"Layer(s) not found: {list(found_difference)}")
            )
        for wms_layer in found_layers:
            if "view_wmslayer" in get_perms(self.user, wms_layer) and wms_layer.queryable:
                accessible_layers.append(wms_layer)
        permission_difference = set(layer_names) - {layer.identifier for layer in accessible_layers}
        if len(permission_difference) > 0:
            raise PermissionError(
                self.render_exception(f"Layer(s) not permitted: {list(permission_difference)}")
            )
        return accessible_layers

    def prepare_filter_element(self, filter_definition: str) -> Filter:
        """
        Creates an instance of Filter from the passed XML string filter definition.

        Args:
            filter_definition: The XML string from which the Filter instance will be created.

        Returns:
            The Filter instance.
        """

        parser = XmlParser()
        fes_filter = parser.from_string(filter_definition, Filter)
        return fes_filter

    def check_filter_empty(self, filter: Filter) -> bool:
        """
        Little helper method to check if a filter does not contain any set
        attributes. This is important,
        since empty filters can cause trouble.

        Args:
            filter: The filter which should be checked.

        Returns:
            Whether the filter is empty or not.
        """
        if len(filter.choice) > 0:  # noqa: SIM103
            return False
        else:
            return True

    def prepare_queries(self, query_params: dict) -> list[Query]:
        """
        This implements the part of the spec to construct a query object out of simple
        KVP (key value pair)
        encoded parameters from GET URL request.

        It mainly is about chapter 6.2.5.3 of the spec PDF.

        This list encoded query:
        TYPENAMES=(ns1:F1,ns2:F2)(ns1:F1,ns1:F1)&
        ALIASES=(A,B)(C,D)&
        FILTER=(<Filter> … for A,B … </Filter>)(<Filter>…for C,D…</Filter>)
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
            type_names_lists = handle_list_encoding(type_names_param_value)
        else:
            raise AttributeError(self.render_exception("TypeNames is a mandatory parameter!"))
        if aliases_param_value:
            # we have aliases in the query
            aliases_lists = handle_list_encoding(aliases_param_value)
            if aliases_lists and not len(aliases_lists) == len(type_names_lists):
                raise AttributeError(
                    self.render_exception("List encoded params have to be same lenght!")
                )
        else:
            # no aliases were passed, we create an empty list of same length as type_names
            aliases_lists = [None] * len(type_names_lists)
        if filter_param_value:
            # we have filters in the query
            filters_lists = handle_list_encoding(filter_param_value)
            if filters_lists and not len(filters_lists) == len(type_names_lists):
                raise AttributeError(
                    self.render_exception("List encoded params have to be same lenght!")
                )
        else:
            # no filters were passed, we create an empty list of same length as type_names
            filters_lists = [None] * len(type_names_lists)

        combined_lists = zip(type_names_lists, aliases_lists, filters_lists, strict=False)
        for type_names, aliases, filter_definition in combined_lists:
            type_names_value_list = type_names.split(",")
            if aliases:
                aliases_value_list = aliases.split(",")
                if len(type_names_value_list) != len(aliases_value_list):
                    raise AttributeError(
                        self.render_exception(
                            "List of aliases and typenames has to be of same length."
                            " Situation is:"
                            f" typenames: {type_names_value_list},"
                            f" length: {len(type_names_value_list)}"
                            f" aliases: {aliases_value_list},"
                            f" length: {len(aliases_value_list)}"
                        )
                    )
            else:
                aliases_value_list = []
            if filter_definition:
                fes_filter = self.prepare_filter_element(filter_definition)
            else:
                fes_filter = Filter()
            if bbox_definition:
                bbox_list = bbox_definition.split(",")
                try:
                    bbox_crs = bbox_list[4]
                except IndexError:
                    logging.info(
                        f"There was no SRS definition in the BBOX parameter, we assume"
                        f" it has the SRS of the request: {srs_name}"
                    )
                    bbox_crs = srs_name
                # we expect one optional BBOX which is assigned to all passed typenames!
                # This aligns with spec as it 7.9.2.3 of the spec doc. However, there is
                # one example wich supports that B.8.5.4
                # and one which states a conflicting situation B.8.5.5
                # TODO: Check how the conflict can be explained?
                fes_filter.bbox = Bbox(
                    choice=[ValueReference(type_name) for type_name in type_names_value_list]
                    + [
                        Envelope(
                            lower_corner=DirectPositionType(value=bbox_list[0:2]),
                            upper_corner=DirectPositionType(value=bbox_list[2:4]),
                            srs_name=bbox_crs,
                            srs_dimension=2,
                        )
                    ]
                )
            queries.append(
                Query(
                    srs_name=srs_name,
                    type_names=type_names_value_list,
                    aliases=aliases_value_list,
                    filter=fes_filter if not self.check_filter_empty(fes_filter) else None,
                )
            )
        return queries

    def query_parameters_to_get_feature_request(self, query_params: dict) -> GetFeature:
        """
        Transforms a dictionary of query parameters to a GetFeature object.

        Args:
            query_params: The dictionary of query parameters as they are coming from the
            request.

        Returns:
            The instance of GetFeature.
        """
        return GetFeature(
            version=query_params["VERSION"],
            stored_query_or_query=self.prepare_queries(query_params),
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

    def unwrap_type_names(self, get_feature_params: GetFeature, unique: bool = True) -> list[str]:
        """
        Get a list of all typenames
        Args:
            get_feature_params: The parameter how it was taken from request
            unique: If the list should not contain duplicates
        Returns:
            flat list of type names
        """
        type_names = []
        for query in get_feature_params.stored_query_or_query:
            if unique:
                for type_name in query.type_names:
                    if type_name not in type_names:
                        type_names.append(type_name)
            else:
                type_names.extend(query.type_names)
        return type_names

    def getfeature_to_qslgetfeaturejob(
        self, get_feature_parameter: GetFeature
    ) -> QslJobParameterFeature:
        """
        This method transforms a
        georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.get_feature.GetFeature
        constructed from the original request towards Georama into a
        qgis_server_light.interface.job.QslGetFeatureJob. This is done to minimize the
        interface and keep control about what we send over to the worker.
        Args:
            get_feature_parameter: The query parameters coming in from Django request.

        Returns:
            A constructed instance of QslGetFeatureJob which can be sent to QGIS-Server-Light.
        """
        qsl_feature_queries = []
        for query in get_feature_parameter.stored_query_or_query:
            # based on the sanitized list of requested layer names we fetch then
            # the definitions of these
            # layers (this includes permission check and existence check)
            accessible_datasets = []
            for layer in self.obtain_accessible_layers(self.sanitized_typenames(query.type_names)):
                accessible_datasets.append(layer.datasource.to_qsl_job_layer())
            if query.filter:
                if len(accessible_datasets) > 1:
                    # we dont allow that, since its not possible to create filter
                    # from expression on multiple
                    # layers in QGIS currently.
                    raise AttributeError(
                        self.render_exception(
                            "Currently QGIS-Server-Light does not support querying multiple"
                            " layers in one"
                            " query and passing a filter on that. This is a"
                            " limitation of QGIS."
                        )
                    )
                filter = XmlSerializer().render(
                    query.filter,
                    ns_map={
                        "": "http://www.opengis.net/fes/2.0",
                        "gml": "http://www.opengis.net/gml/3.2",
                    },
                )
            else:
                filter = None
            qsl_feature_queries.append(
                FeatureQuery(
                    layers=accessible_datasets,
                    aliases=query.aliases,
                    filter=OgcFilterFES20(definition=filter),
                )
            )
        return QslJobParameterFeature(
            start_index=get_feature_parameter.start_index,
            count=get_feature_parameter.count,
            queries=qsl_feature_queries,
        )

    def parse_wkb_to_gml3(
        self, wkb: bytes, srs_definition: str
    ) -> GeometryMember | GeometryMembers:
        """
        This method directly reads the bytes of WKB representation and shreds them into the
        desired objects from the GML3 interface. This avoids nested iterations where ever
        possible as it often comes by libraries which are parsing WKB in some GeoJSON like
        structure before transforming it to the desired format (GML3 in our case).Some tests
        show, that this is as fast as it can be.

        Args:
            wkb: The WKB representation of the geometry to parse. We directly use that to
                have a common and described interface to transport things between QSL and
                Georama. Parsing WKB on Georama side also enables us to do postprocessing
                (permission stuff etc.).
            srs_definition: The definition string of the SRS of the WKB geometry. This is
                usually something like URN e.g. ``urn:ogc:def:crs:EPSG::2056`` or URL e.g.
                ``http://www.opengis.net/def/crs/EPSG/0/2056``

        Returns:
            A GML3 object representing the parsed geometry. The exact type depends on the
            geometry type. Single geomtry types will return an ``GeometryMember`` instance.
            Multi geometry types will return an ``GeometryMembers`` instance.
        """
        # read first byte for byteorder information
        endian = "<" if wkb[0] == 1 else ">"  # < is little endian
        wkb = wkb[1:]

        # read following 4 bytes for geometry type information
        geometry_type = np.frombuffer(wkb[0:4], dtype=endian + "I")[0]
        wkb = wkb[4:]

        is_multipoint = geometry_type in self.geometry_types["multipoint"]
        if geometry_type in self.geometry_types["point"] or is_multipoint:
            # POINT or MULTIPOINT
            # ==================================================================

            if geometry_type == 1:
                # XY
                dimensions = 2
            elif geometry_type == 1001:
                # XYZ
                dimensions = 3
            elif geometry_type == 2001:
                # XYM
                dimensions = 3
            elif geometry_type == 3001:
                # XYZM
                dimensions = 4
            elif geometry_type == 4:
                # XY
                dimensions = 2
            elif geometry_type == 1004:
                # XYZ
                dimensions = 3
            elif geometry_type == 2004:
                # XYM
                dimensions = 3
            elif geometry_type == 3004:
                # XYZM
                dimensions = 4
            else:
                logging.debug(f"Geometry type '{geometry_type}' is not in supported list")
                raise NotImplementedError()

            if is_multipoint:
                number_of_wkb_points = np.frombuffer(wkb[0:4], dtype=endian + "I")[0]
                wkb = wkb[4:]
            else:
                number_of_wkb_points = 1

            geometry_part_offset = dimensions * 8

            points = [None] * number_of_wkb_points

            for i in range(number_of_wkb_points):
                # Parsing single point
                # -------------------------------------------

                if is_multipoint:
                    # checking bytes for geometry type information
                    m_geometry_type = np.frombuffer(wkb[1:5], dtype=endian + "I")[0]
                    wkb = wkb[5:]

                    if geometry_type - m_geometry_type != 3:
                        raise ValueError(
                            f"Multipoint of type '{geometry_type}' contains non-confirming"
                            f"geometry of type '{m_geometry_type}'. "
                            f"Supported point types are {self.geometry_types['point']}."
                        )

                geometry_part_offset = dimensions * 8
                points[i] = Point(
                    srs_name=srs_definition,
                    srs_dimension=dimensions,
                    pos=Pos(value=np.frombuffer(wkb[0:geometry_part_offset], dtype=endian + "f8")),
                )
                wkb = wkb[geometry_part_offset:]

            if is_multipoint:
                return GeometryMember(
                    multi_point=MultiPoint(
                        srs_name=srs_definition,
                        srs_dimension=dimensions,
                        point_members=PointMembers(points),
                    )
                )
            else:
                return GeometryMember(point=points[0])
        elif (
            geometry_type in self.geometry_types["linestring"]
            or geometry_type in self.geometry_types["multilinestring"]
        ):
            # LINESTRING and MULTILINE
            # ==================================================================

            is_multiline = geometry_type in self.geometry_types["multilinestring"]

            if geometry_type == 2:
                # XY
                dimensions = 2
            elif geometry_type == 1002:
                # XYZ
                dimensions = 3
            elif geometry_type == 2002:
                # XYM
                dimensions = 3
            elif geometry_type == 3002:
                # XYZM
                dimensions = 4
            elif geometry_type == 5:
                # XY
                dimensions = 2
            elif geometry_type == 1005:
                # XYZ
                dimensions = 3
            elif geometry_type == 2005:
                # XYM
                dimensions = 3
            elif geometry_type == 3005:
                # XYZM
                dimensions = 4
            else:
                logging.debug(f"Geometry type '{geometry_type}' is not in supported list")
                raise NotImplementedError()

            if is_multiline:
                number_of_wkb_lines = np.frombuffer(wkb[0:4], dtype=endian + "I")[0]
                wkb = wkb[4:]
            else:
                number_of_wkb_lines = 1

            lines = [None] * number_of_wkb_lines

            for i in range(number_of_wkb_lines):
                # Parsing single LineString
                # -------------------------------------------

                if is_multiline:
                    # checking bytes for geometry type information
                    m_geometry_type = np.frombuffer(wkb[1:5], dtype=endian + "I")[0]
                    wkb = wkb[5:]

                    if geometry_type - m_geometry_type != 3:
                        raise ValueError(
                            f"Multiline of type '{geometry_type}' contains non-confirming"
                            f"geometry of type '{m_geometry_type}'. "
                            f"Supported point types are {self.geometry_types['linestring']}."
                        )

                number_of_points = np.frombuffer(wkb[0:4], dtype=endian + "I")[0]
                wkb = wkb[4:]
                geometry_part_offset = number_of_points * dimensions * 8
                lines[i] = LineString(
                    srs_name=srs_definition,
                    srs_dimension=dimensions,
                    pos_list=PosList(
                        value=np.frombuffer(wkb[0:geometry_part_offset], dtype=endian + "f8")
                    ),
                )

                # slicing wkb by geometry part offset
                wkb = wkb[geometry_part_offset:]

            if is_multiline:
                return GeometryMember(
                    multi_curve=MultiCurve(
                        srs_name=srs_definition,
                        srs_dimension=dimensions,
                        curve_members=CurveMembers(line_string=lines),
                    )
                )
            else:
                return GeometryMember(line_string=lines[0])
        elif (
            geometry_type in self.geometry_types["polygon"]
            or geometry_type in self.geometry_types["multipolygon"]
        ):
            # POLYGON and MULTIPOLYGON
            # ==================================================================

            is_multipolygon = geometry_type in self.geometry_types["multipolygon"]

            if geometry_type == 3:
                # XY
                dimensions = 2
            elif geometry_type == 1003:
                # XYZ
                dimensions = 3
            elif geometry_type == 2003:
                # XYM
                dimensions = 3
            elif geometry_type == 3003:
                # XYZM
                dimensions = 4
            elif geometry_type == 6:
                # XY
                dimensions = 2
            elif geometry_type == 1006:
                # XYZ
                dimensions = 3
            elif geometry_type == 2006:
                # XYM
                dimensions = 3
            elif geometry_type == 3006:
                # XYZM
                dimensions = 4
            else:
                logging.debug(f"Geometry type '{geometry_type}' is not in supported list")
                raise NotImplementedError()

            if is_multipolygon:
                number_of_wkb_polygons = np.frombuffer(wkb[0:4], dtype=endian + "I")[0]
                wkb = wkb[4:]
            else:
                number_of_wkb_polygons = 1

            polygons = [None] * number_of_wkb_polygons

            for i in range(number_of_wkb_polygons):
                # Parsing single Polygon
                # -------------------------------------------

                if is_multipolygon:
                    # checking bytes for geometry type information
                    m_geometry_type = np.frombuffer(wkb[1:5], dtype=endian + "I")[0]
                    wkb = wkb[5:]

                    if geometry_type - m_geometry_type != 3:
                        raise ValueError(
                            f"Multipolygon of type '{geometry_type}' contains non-confirming"
                            f"geometry of type '{m_geometry_type}'. "
                            f"Supported point types are {self.geometry_types['polygon']}."
                        )

                number_of_rings = np.frombuffer(wkb[0:4], dtype=endian + "I")[0]
                logging.debug(f"  parsing polygon with {number_of_rings} rings")
                polygon = Polygon(srs_name=srs_definition, srs_dimension=dimensions)
                # slicing wkb by interpreted parts
                wkb = wkb[4:]
                for ring in range(number_of_rings):
                    # reading next 4 bytes of wkb
                    number_of_points = np.frombuffer(wkb[0:4], dtype=endian + "I")[0]
                    # slicing wkb by read 4 bytes
                    wkb = wkb[4:]
                    # calculating offset to read geometry part
                    geometry_part_offset = number_of_points * dimensions * 8
                    logging.debug(f"  parsing ring:{ring} with: {number_of_points} points")

                    pos_list = PosList(
                        value=np.frombuffer(wkb[0:geometry_part_offset], dtype=endian + "f8")
                    )
                    # slicing wkb be geometry part offset
                    wkb = wkb[geometry_part_offset:]
                    if ring == 0:
                        # this is the exterior ring
                        polygon.exterior = Exterior(linear_ring=LinearRing(pos_list=pos_list))
                    else:
                        # all others are interior rings
                        polygon.interior.append(Interior(linear_ring=LinearRing(pos_list=pos_list)))
                polygons[i] = polygon

            if is_multipolygon:
                return GeometryMember(
                    multi_surface=MultiSurface(
                        srs_name=srs_definition,
                        srs_dimension=dimensions,
                        surface_members=SurfaceMembers(polygon=polygons),
                    )
                )
            else:
                return GeometryMember(polygon=polygons[0])

    def get_feature(
        self, get_feature_parameter: GetFeature, result: JobResult, job: QslJobParameterFeature
    ):
        qsl_query_collection = JsonParser().from_bytes(result.data, QueryCollection)
        wfs_feature_collection = FeatureCollection(
            number_returned=0, number_matched=qsl_query_collection.numbers_matched
        )

        class GeoramaMeta:
            namespace = self.own_namespace_domain

        for feature_collection_index, feature_collection in enumerate(
            qsl_query_collection.feature_collections
        ):
            wfs_feature_collection.number_returned += len(feature_collection.features)
            for feature_sequence, feature in enumerate(feature_collection.features):
                fields = []
                feature_dict = {}
                for attribute in feature.attributes:
                    if attribute.value is not None:  # noqa: SIM108
                        type_name = type(attribute.value)
                    else:
                        # we take a save exit here, since we do not want to validate
                        # data in this step we
                        # define all None values to be str, which can be None then -.-
                        type_name = str
                    field_metadata = {}
                    if isinstance(attribute.value, bytes):
                        field_metadata["format"] = "base64"
                    fields.append(
                        (
                            attribute.name,
                            type_name,
                            field(default=None, metadata=field_metadata),
                        )
                    )
                    if attribute.value is None:
                        # related to: https://github.com/tefra/xsdata/issues/408
                        feature_dict[attribute.name] = ""
                    else:
                        feature_dict[attribute.name] = attribute.value
                # TODO: This has to be fixed, we need to respect actual PK fields for
                #  that! Currently a
                #  feature can have a column with name id which might not
                #  be the actual primary key
                #  but it gets treated like one...
                if "id" not in feature_dict:
                    fields.append(
                        (
                            "id",
                            str,
                            field(
                                default=None,
                                metadata={
                                    "type": "Attribute",
                                    "namespace": "http://www.opengis.net/gml/3.2",
                                    "nillable": True,
                                },
                            ),
                        )
                    )
                    feature_dict["id"] = (
                        f"{self.own_namespace}:{feature_collection.name}.{feature_sequence}"
                    )
                fields.append(("geometry", GeometryMember | GeometryMembers, field(default=None)))
                feature_dataclass = make_dataclass(feature_collection.name, fields=fields)
                feature_dataclass.Meta = GeoramaMeta
                feature_object = feature_dataclass(**feature_dict)
                start = time.time()
                if get_feature_parameter.stored_query_or_query[0].srs_name:
                    srs = get_feature_parameter.stored_query_or_query[
                        feature_collection_index
                    ].srs_name
                else:
                    srs = None
                    # TODO@vvmruder: Patch this logic
                    for dataset in job.queries[feature_collection_index].layers:
                        if dataset == feature_collection.name:
                            srs = dataset.crs.ogc_uri
                            break
                feature_object.geometry = self.parse_wkb_to_gml3(
                    feature.geometry.value,
                    srs,
                )
                logging.debug(f"Rendered GML3 from WKB direct: {time.time() - start}")
                wfs_feature_collection.member.append(Member(content=[feature_object]))
        return wfs_feature_collection

    def render_xml(
        self, feature_collection: FeatureCollection, requested_typenames: list[str]
    ) -> str:
        serializer = XmlSerializer(
            config=SerializerConfig(
                xml_declaration=True,
                xml_version="1.0",
                ignore_default_attributes=True,
                schema_location=" ".join(
                    [
                        self.own_namespace_domain,
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
        requested_typenames: list[str],
    ) -> tuple[str, str, bool]:
        if requested_format == "TEXT/XML" or requested_format == "APPLICATION/GML+XML; VERSION=3.2":
            return (
                self.render_xml(feature_collection, requested_typenames),
                f"{requested_format.lower()}; charset=utf-8",
                True,
            )
        elif requested_format == "GML3":
            return (
                self.render_xml(feature_collection, requested_typenames),
                f"{'APPLICATION/GML+XML; VERSION=3.2'.lower()}; charset=utf-8",
                True,
            )
        elif requested_format == "APPLICATION/JSON" or requested_format == "TEXT/JSON":
            return (
                self.render_json(feature_collection),
                f"{requested_format.lower()}; charset=utf-8",
                True,
            )
        else:
            logging.debug("No matching Format was found.")
            return (
                self.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed.Allowed is {self.allowed_formats}"
                ),
                "text/xml; charset=utf-8",
                False,
            )
