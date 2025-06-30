from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.value_type import ValueType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Value1(ValueType):
    class Meta:
        name = "Value"
        namespace = "http://www.opengis.net/ows/1.1"
