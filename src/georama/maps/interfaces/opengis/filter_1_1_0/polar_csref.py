from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.polar_csref_type import PolarCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolarCsref(PolarCsrefType):
    class Meta:
        name = "polarCSRef"
        namespace = "http://www.opengis.net/gml"
