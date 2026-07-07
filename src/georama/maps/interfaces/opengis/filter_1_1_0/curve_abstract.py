from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_curve_type import (
    AbstractCurveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveAbstract(AbstractCurveType):
    """
    The "_Curve" element is the abstract head of the substituition group for all
    (continuous) curve elements.
    """

    class Meta:
        name = "_Curve"
        namespace = "http://www.opengis.net/gml"
