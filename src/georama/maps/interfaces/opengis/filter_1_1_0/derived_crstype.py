from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.derived_crstype_type import (
    DerivedCrstypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrstype(DerivedCrstypeType):
    class Meta:
        name = "derivedCRSType"
        namespace = "http://www.opengis.net/gml"
