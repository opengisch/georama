from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.inline_property_type import (
    InlinePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractInlineProperty(InlinePropertyType):
    """
    Gml:abstractInlineProperty may be used as the head of a subtitution group of
    more specific elements providing a value inline.
    """

    class Meta:
        name = "abstractInlineProperty"
        namespace = "http://www.opengis.net/gml/3.2"
