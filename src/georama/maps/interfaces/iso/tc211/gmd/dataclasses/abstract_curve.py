from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_curve_type import (
    AbstractCurveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCurve(AbstractCurveType):
    """
    The AbstractCurve element is the abstract head of the substitution group for
    all (continuous) curve elements.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
