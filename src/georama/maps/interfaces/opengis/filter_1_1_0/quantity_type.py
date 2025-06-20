from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityType(StringOrRefType):
    """Informal description of the phenomenon or type of quantity that is measured
    or observed.

    For example, "length", "angle", "time", "pressure", or
    "temperature". When the quantity is the result of an observation or
    measurement, this term is known as Observable Type or Measurand.
    """

    class Meta:
        name = "quantityType"
        namespace = "http://www.opengis.net/gml"
