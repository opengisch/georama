from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.solid_type import SolidType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Solid(SolidType):
    """A solid is the basis for 3-dimensional geometry.

    The extent of a solid is defined by the boundary surfaces as
    specified in ISO 19107:2003, 6.3.18. exterior specifies the outer
    boundary, interior the inner boundary of the solid.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
