from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometry_type import (
    AbstractGeometryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


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
        namespace = "http://www.opengis.net/gml"
