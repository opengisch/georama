from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.linear_csproperty_type import (
    LinearCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearCs2(LinearCspropertyType):
    """
    Gml:linearCS is an association role to the linear coordinate system used by
    this CRS.
    """

    class Meta:
        name = "linearCS"
        namespace = "http://www.opengis.net/gml/3.2"
