from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.language_string_type import (
    LanguageStringType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Abstract1(LanguageStringType):
    """
    Brief narrative description of this resource, normally used for display to a
    human.
    """

    class Meta:
        name = "Abstract"
        namespace = "http://www.opengis.net/ows/1.1"
