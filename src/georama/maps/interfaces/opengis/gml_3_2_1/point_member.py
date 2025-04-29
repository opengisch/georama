from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.point_property_type import (
    PointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointMember(PointPropertyType):
    """
    This property element either references a Point via the XLink-attributes or
    contains the Point element.
    """

    class Meta:
        name = "pointMember"
        namespace = "http://www.opengis.net/gml/3.2"
