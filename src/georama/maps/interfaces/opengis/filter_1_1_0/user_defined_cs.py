from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.user_defined_cstype import (
    UserDefinedCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UserDefinedCs(UserDefinedCstype):
    class Meta:
        name = "UserDefinedCS"
        namespace = "http://www.opengis.net/gml"
