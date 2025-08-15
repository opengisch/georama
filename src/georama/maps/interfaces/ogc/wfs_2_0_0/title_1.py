from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.language_string_type import (
    LanguageStringType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Title1(LanguageStringType):
    """
    Title of this resource, normally used for display to a human.
    """

    class Meta:
        name = "Title"
        namespace = "http://www.opengis.net/ows/1.1"
