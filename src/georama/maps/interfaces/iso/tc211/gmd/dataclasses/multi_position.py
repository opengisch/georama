from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_point_property_type import (
    MultiPointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPosition(MultiPointPropertyType):
    class Meta:
        name = "multiPosition"
        namespace = "http://www.opengis.net/gml"
