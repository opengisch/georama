from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometry_type import (
    AbstractGeometryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Geometry(AbstractGeometryType):
    """The "_Geometry" element is the abstract head of the substituition group for
    all geometry elements of GML 3.

    This includes pre-defined and user-defined geometry elements. Any
    geometry element must be a direct or indirect extension/restriction
    of AbstractGeometryType and must be directly or indirectly in the
    substitution group of "_Geometry".
    """

    class Meta:
        name = "_Geometry"
        namespace = "http://www.opengis.net/gml"
