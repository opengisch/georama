from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCurveType(AbstractGeometricPrimitiveType):
    """Gml:AbstractCurveType is an abstraction of a curve to support the different
    levels of complexity.

    The curve may always be viewed as a geometric primitive, i.e. is
    continuous.
    """
