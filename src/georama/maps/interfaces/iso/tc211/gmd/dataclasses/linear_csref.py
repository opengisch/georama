from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.linear_csproperty_type import (
    LinearCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearCsref(LinearCspropertyType):
    class Meta:
        name = "linearCSRef"
        namespace = "http://www.opengis.net/gml"
