from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.user_defined_cstype import (
    UserDefinedCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UserDefinedCs1(UserDefinedCstype):
    """Gml:UserDefinedCS is a two- or three-dimensional coordinate system that
    consists of any combination of coordinate axes not covered by any other
    coordinate system type.

    A UserDefinedCS shall have two or three gml:axis property elements;
    the number of property elements shall equal the dimension of the CS.
    """

    class Meta:
        name = "UserDefinedCS"
        namespace = "http://www.opengis.net/gml/3.2"
