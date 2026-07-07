from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AreaType(MeasureType):
    pass
