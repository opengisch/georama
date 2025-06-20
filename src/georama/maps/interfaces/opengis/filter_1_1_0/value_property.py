from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import ValuePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValueProperty(ValuePropertyType):
    """
    Element which refers to, or contains, a Value.
    """

    class Meta:
        name = "valueProperty"
        namespace = "http://www.opengis.net/gml"
