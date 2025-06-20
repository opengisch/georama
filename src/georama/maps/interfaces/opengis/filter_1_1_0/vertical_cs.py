from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vertical_cstype import VerticalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCs(VerticalCstype):
    class Meta:
        name = "VerticalCS"
        namespace = "http://www.opengis.net/gml"
