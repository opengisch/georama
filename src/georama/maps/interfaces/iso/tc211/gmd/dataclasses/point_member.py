from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_property_type import (
    PointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointMember(PointPropertyType):
    """
    This property element either references a Point via the XLink-attributes or
    contains the Point element.
    """

    class Meta:
        name = "pointMember"
        namespace = "http://www.opengis.net/gml"
