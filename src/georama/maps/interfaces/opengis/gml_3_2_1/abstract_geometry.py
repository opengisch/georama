from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometry_type import (
    AbstractGeometryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometry(AbstractGeometryType):
    """The AbstractGeometry element is the abstract head of the substitution group
    for all geometry elements of GML.

    This includes pre-defined and user-defined geometry elements. Any
    geometry element shall be a direct or indirect extension/restriction
    of AbstractGeometryType and shall be directly or indirectly in the
    substitution group of AbstractGeometry.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
