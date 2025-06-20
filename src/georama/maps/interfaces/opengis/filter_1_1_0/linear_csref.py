from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.linear_csref_type import (
    LinearCsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearCsref(LinearCsrefType):
    class Meta:
        name = "linearCSRef"
        namespace = "http://www.opengis.net/gml"
