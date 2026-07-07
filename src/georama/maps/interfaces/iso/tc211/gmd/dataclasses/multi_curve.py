from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_curve_type import (
    MultiCurveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurve(MultiCurveType):
    """A gml:MultiCurve is defined by one or more gml:AbstractCurves.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:curveMember) or the array property
    (gml:curveMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
