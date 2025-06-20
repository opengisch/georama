from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.coord import Coord
from georama.maps.interfaces.opengis.filter_1_1_0.coordinates import Coordinates
from georama.maps.interfaces.opengis.filter_1_1_0.direct_position_type import (
    DirectPositionType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EnvelopeType:
    """Envelope defines an extent using a pair of positions defining opposite
    corners in arbitrary dimensions.

    The first direct position is the "lower corner" (a coordinate
    position consisting of all the minimal ordinates for each dimension
    for all points within the envelope), the second one the "upper
    corner" (a coordinate position consisting of all the maximal
    ordinates for each dimension for all points within the envelope).

    :ivar lower_corner:
    :ivar upper_corner:
    :ivar coord: deprecated with GML version 3.0
    :ivar pos: Deprecated with GML version 3.1. Use the explicit
        properties "lowerCorner" and "upperCorner" instead.
    :ivar coordinates: Deprecated with GML version 3.1.0. Use the
        explicit properties "lowerCorner" and "upperCorner" instead.
    :ivar srs_name: In general this reference points to a CRS instance
        of gml:CoordinateReferenceSystemType (see
        coordinateReferenceSystems.xsd). For well known references it is
        not required that the CRS description exists at the location the
        URI points to. If no srsName attribute is given, the CRS must be
        specified as part of the larger context this geometry element is
        part of, e.g. a geometric element like point, curve, etc. It is
        expected that this attribute will be specified at the direct
        position level only in rare cases.
    :ivar srs_dimension: The "srsDimension" is the length of coordinate
        sequence (the number of entries in the list). This dimension is
        specified by the coordinate reference system. When the srsName
        attribute is omitted, this attribute shall be omitted.
    :ivar axis_labels: Ordered list of labels for all the axes of this
        CRS. The gml:axisAbbrev value should be used for these axis
        labels, after spaces and forbiddden characters are removed. When
        the srsName attribute is included, this attribute is optional.
        When the srsName attribute is omitted, this attribute shall also
        be omitted.
    :ivar uom_labels: Ordered list of unit of measure (uom) labels for
        all the axes of this CRS. The value of the string in the
        gml:catalogSymbol should be used for this uom labels, after
        spaces and forbiddden characters are removed. When the
        axisLabels attribute is included, this attribute shall also be
        included. When the axisLabels attribute is omitted, this
        attribute shall also be omitted.
    """

    lower_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "lowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    upper_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "upperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coord: list[Coord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "max_occurs": 2,
        },
    )
    pos: list[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "max_occurs": 2,
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    axis_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
    uom_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
