from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    AbstractGeneralDerivedCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralDerivedCrs(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "_GeneralDerivedCRS"
        namespace = "http://www.opengis.net/gml"
