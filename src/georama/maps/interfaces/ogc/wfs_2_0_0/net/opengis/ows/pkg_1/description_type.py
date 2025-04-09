from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.abstract import (
    Abstract,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.keywords import (
    Keywords,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.title import Title

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class DescriptionType:
    """Human-readable descriptive information for the object it is included within.

    This type shall be extended if needed for specific OWS use to
    include additional metadata for each type of information. This type
    shall not be restricted for a specific OWS to change the
    multiplicity (or optionality) of some elements. If the xml:lang
    attribute is not included in a Title, Abstract or Keyword element,
    then no language is specified for that element unless specified by
    another means.  All Title, Abstract and Keyword elements in the same
    Description that share the same xml:lang attribute value represent
    the description of the parent object in that language. Multiple
    Title or Abstract elements shall not exist in the same Description
    with the same xml:lang attribute value unless otherwise specified.
    """

    title: list[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    keywords: list[Keywords] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
