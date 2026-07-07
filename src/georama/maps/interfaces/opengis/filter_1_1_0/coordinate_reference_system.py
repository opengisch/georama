from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_type import (
    AbstractReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateReferenceSystem(AbstractReferenceSystemType):
    """A coordinate reference system consists of an ordered sequence of coordinate
    system axes that are related to the earth through a datum.

    A coordinate reference system is defined by one datum and by one
    coordinate system. Most coordinate reference system do not move
    relative to the earth, except for engineering coordinate reference
    systems defined on moving platforms such as cars, ships, aircraft,
    and spacecraft. For further information, see OGC Abstract
    Specification Topic 2. Coordinate reference systems are commonly
    divided into sub-types. The common classification criterion for sub-
    typing of coordinate reference systems is the way in which they deal
    with earth curvature. This has a direct effect on the portion of the
    earth's surface that can be covered by that type of CRS with an
    acceptable degree of error. The exception to the rule is the subtype
    "Temporal" which has been added by analogy.
    """

    class Meta:
        name = "_CoordinateReferenceSystem"
        namespace = "http://www.opengis.net/gml"
