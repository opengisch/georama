from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_curve_property_type import (
    MultiCurvePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCenterLineOf(MultiCurvePropertyType):
    class Meta:
        name = "multiCenterLineOf"
        namespace = "http://www.opengis.net/gml"
