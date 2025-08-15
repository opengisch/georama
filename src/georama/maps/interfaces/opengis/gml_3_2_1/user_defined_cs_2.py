from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.user_defined_csproperty_type import (
    UserDefinedCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UserDefinedCs2(UserDefinedCspropertyType):
    """
    Gml:userDefinedCS is an association role to the user defined coordinate system
    used by this CRS.
    """

    class Meta:
        name = "userDefinedCS"
        namespace = "http://www.opengis.net/gml/3.2"
