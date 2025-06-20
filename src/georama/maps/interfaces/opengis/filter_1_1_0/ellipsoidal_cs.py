from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoidal_cstype import (
    EllipsoidalCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCs(EllipsoidalCstype):
    class Meta:
        name = "EllipsoidalCS"
        namespace = "http://www.opengis.net/gml"
