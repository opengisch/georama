from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.base_unit_type import BaseUnitType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BaseUnit(BaseUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
