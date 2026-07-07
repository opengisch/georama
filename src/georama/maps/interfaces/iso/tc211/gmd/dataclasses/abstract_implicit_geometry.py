from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometry_type import (
    AbstractGeometryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractImplicitGeometry(AbstractGeometryType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
