from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.measure_type import MeasureType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Measure1(MeasureType):
    class Meta:
        name = "Measure"
        namespace = "http://www.isotc211.org/2005/gco"
