from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractSolidType(AbstractGeometricPrimitiveType):
    """Gml:AbstractSolidType is an abstraction of a solid to support the different
    levels of complexity.

    The solid may always be viewed as a geometric primitive, i.e. is
    contiguous.
    """
