from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.user_defined_csproperty_type import (
    UserDefinedCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UserDefinedCsref(UserDefinedCspropertyType):
    class Meta:
        name = "userDefinedCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
