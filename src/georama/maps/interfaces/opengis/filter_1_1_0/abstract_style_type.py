from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractStyleType(AbstractGmltype):
    """[complexType of] The value of the top-level property.

    It is an abstract element. Used as the head element of the
    substitution group for extensibility purposes.
    """
