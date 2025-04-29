from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class QuantityTypeReference(ReferenceType):
    """The gml:quantityTypeReference property indicates the phenomenon to which the
    units apply.

    The content is a reference to a remote value.
    """

    class Meta:
        name = "quantityTypeReference"
        namespace = "http://www.opengis.net/gml/3.2"
