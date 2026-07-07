from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.measure_or_null_list_type import (
    MeasureOrNullListType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityExtentType(MeasureOrNullListType):
    """Restriction of list type to store a 2-point range of numeric values.

    If one member is a null, then this is a single ended interval.
    """
