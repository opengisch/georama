from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import CrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CrsRef(CrsrefType):
    class Meta:
        name = "crsRef"
        namespace = "http://www.opengis.net/gml"
