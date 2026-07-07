from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Description(StringOrRefType):
    """
    Contains a simple text description of the object, or refers to an external
    description.
    """

    class Meta:
        name = "description"
        namespace = "http://www.opengis.net/gml"
