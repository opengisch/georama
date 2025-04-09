from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_property_type import (
    CurvePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EdgeOf(CurvePropertyType):
    class Meta:
        name = "edgeOf"
        namespace = "http://www.opengis.net/gml"
