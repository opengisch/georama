from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_curve_property_type import (
    MultiCurvePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurveProperty(MultiCurvePropertyType):
    """This property element either references a curve aggregate via the XLink-
    attributes or contains the "multi curve" element.

    multiCurveProperty is the predefined property, which may be used by
    GML Application Schemas whenever a GML feature has a property with a
    value that is substitutable for MultiCurve.
    """

    class Meta:
        name = "multiCurveProperty"
        namespace = "http://www.opengis.net/gml"
