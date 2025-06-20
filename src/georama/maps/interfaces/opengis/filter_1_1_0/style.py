from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.style_type import StyleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Style(StyleType):
    """Predefined concrete value of the top-level property.

    Encapsulates all other styling information.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
