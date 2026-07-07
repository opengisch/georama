from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSolidType(AbstractGeometricPrimitiveType):
    """Gml:AbstractSolidType is an abstraction of a solid to support the different
    levels of complexity.

    The solid may always be viewed as a geometric primitive, i.e. is
    contiguous.
    """
