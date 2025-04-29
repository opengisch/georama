from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UserDefinedCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "UserDefinedCSType"
