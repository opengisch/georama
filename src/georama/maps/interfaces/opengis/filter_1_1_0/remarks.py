from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Remarks(StringOrRefType):
    """Information about this object or code.

    Contains text or refers to external text.
    """

    class Meta:
        name = "remarks"
        namespace = "http://www.opengis.net/gml"
