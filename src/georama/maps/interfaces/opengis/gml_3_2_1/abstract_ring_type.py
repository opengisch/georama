from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_curve_type import (
    AbstractCurveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractRingType(AbstractCurveType):
    pass
