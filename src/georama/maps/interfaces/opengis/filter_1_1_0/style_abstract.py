from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_style_type import (
    AbstractStyleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StyleAbstract(AbstractStyleType):
    """The value of the top-level property.

    It is an abstract element. Used as the head element of the
    substitution group for extensibility purposes.
    """

    class Meta:
        name = "_Style"
        namespace = "http://www.opengis.net/gml"
