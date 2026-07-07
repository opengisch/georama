from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityType(StringOrRefType):
    """The gml:quantityType property indicates the phenomenon to which the units
    apply.

    This element contains an informal description of the phenomenon or
    type of physical quantity that is measured or observed. When the
    physical quantity is the result of an observation or measurement,
    this term is known as observable type or measurand. The use of
    gml:quantityType for references to remote values is deprecated.
    """

    class Meta:
        name = "quantityType"
        namespace = "http://www.opengis.net/gml"
