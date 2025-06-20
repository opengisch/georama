from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometryType(AbstractGmltype):
    """All geometry elements are derived directly or indirectly from this abstract
    supertype. A geometry element may.

    have an identifying attribute ("gml:id"), a name (attribute "name") and a description (attribute "description"). It may be associated
    with a spatial reference system (attribute "srsName"). The following rules shall be adhered: - Every geometry type shall derive
    from this abstract type. - Every geometry element (i.e. an element of a geometry type) shall be directly or indirectly in the
    substitution group of _Geometry.

    :ivar gid: This attribute is included for backward compatibility
        with GML 2 and is deprecated with GML 3. This identifer is
        superceded by "gml:id" inherited from AbstractGMLType. The
        attribute "gid" should not be used anymore and may be deleted in
        future versions of GML without further notice.
    :ivar srs_name_attribute: In general this reference points to a CRS
        instance of gml:CoordinateReferenceSystemType (see
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

    gid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    srs_name_attribute: Optional[str] = field(
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
