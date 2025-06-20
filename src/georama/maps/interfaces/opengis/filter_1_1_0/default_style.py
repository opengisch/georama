from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.default_style_property_type import (
    DefaultStylePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefaultStyle(DefaultStylePropertyType):
    """Top-level property.

    Used in application schemas to "attach" the styling information to
    GML data. The link between the data and the style should be
    established through this property only.
    """

    class Meta:
        name = "defaultStyle"
        namespace = "http://www.opengis.net/gml"
