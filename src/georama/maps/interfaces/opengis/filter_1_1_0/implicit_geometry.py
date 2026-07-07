from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometry_type import (
    AbstractGeometryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImplicitGeometry(AbstractGeometryType):
    class Meta:
        name = "_ImplicitGeometry"
        namespace = "http://www.opengis.net/gml"
