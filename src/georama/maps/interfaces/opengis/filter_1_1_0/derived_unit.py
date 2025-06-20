from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.derived_unit_type import (
    DerivedUnitType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedUnit(DerivedUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
