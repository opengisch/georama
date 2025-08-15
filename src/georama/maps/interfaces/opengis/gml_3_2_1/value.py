from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Value(MeasureType):
    """
    Gml:value is a numeric value of an operation parameter, with its associated
    unit of measure.
    """

    class Meta:
        name = "value"
        namespace = "http://www.opengis.net/gml/3.2"
