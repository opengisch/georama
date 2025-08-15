from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.unit_of_measure_type import (
    UnitOfMeasureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UnitOfMeasure(UnitOfMeasureType):
    """The element gml:unitOfMeasure is a property element to refer to a unit of
    measure.

    This is an empty element which carries a reference to a unit of
    measure definition.
    """

    class Meta:
        name = "unitOfMeasure"
        namespace = "http://www.opengis.net/gml/3.2"
