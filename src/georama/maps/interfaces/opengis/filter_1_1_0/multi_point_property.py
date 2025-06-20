from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_point_property_type import (
    MultiPointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointProperty(MultiPointPropertyType):
    """This property element either references a point aggregate via the XLink-
    attributes or contains the "multi point" element.

    multiPointProperty is the predefined property which can be used by
    GML Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for MultiPoint.
    """

    class Meta:
        name = "multiPointProperty"
        namespace = "http://www.opengis.net/gml"
