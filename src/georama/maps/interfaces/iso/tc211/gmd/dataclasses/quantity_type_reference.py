from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.reference_type import (
    ReferenceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityTypeReference(ReferenceType):
    """The gml:quantityTypeReference property indicates the phenomenon to which the
    units apply.

    The content is a reference to a remote value.
    """

    class Meta:
        name = "quantityTypeReference"
        namespace = "http://www.opengis.net/gml"
