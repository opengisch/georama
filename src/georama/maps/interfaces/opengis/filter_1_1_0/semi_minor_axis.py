from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SemiMinorAxis(MeasureType):
    """Length of the semi-minor axis of the ellipsoid.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a length, such as metres or
    feet.
    """

    class Meta:
        name = "semiMinorAxis"
        namespace = "http://www.opengis.net/gml"
