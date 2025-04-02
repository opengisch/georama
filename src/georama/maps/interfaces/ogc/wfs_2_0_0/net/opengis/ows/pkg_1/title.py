from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.language_string_type import (
    LanguageStringType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Title(LanguageStringType):
    """
    Title of this resource, normally used for display to a human.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
