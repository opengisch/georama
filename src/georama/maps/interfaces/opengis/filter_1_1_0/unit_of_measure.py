from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.unit_of_measure_type import (
    UnitOfMeasureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UnitOfMeasure(UnitOfMeasureType):
    class Meta:
        name = "unitOfMeasure"
        namespace = "http://www.opengis.net/gml"
