from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateSystem(AbstractCoordinateSystemType):
    """Gml:AbstractCoordinateSystem is a coordinate system (CS) is the non-
    repeating sequence of coordinate system axes that spans a given coordinate
    space.

    A CS is derived from a set of mathematical rules for specifying how
    coordinates in a given space are to be assigned to points. The
    coordinate values in a coordinate tuple shall be recorded in the
    order in which the coordinate system axes associations are recorded.
    This abstract complex type shall not be used, extended, or
    restricted, in an Application Schema, to define a concrete subtype
    with a meaning equivalent to a concrete subtype specified in this
    document.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
