from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.conventional_unit_type import (
    ConventionalUnitType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConventionalUnit(ConventionalUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
