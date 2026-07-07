from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.arc_type_1 import ArcType1

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Arc(ArcType1):
    class Meta:
        namespace = "http://www.opengis.net/gml"
