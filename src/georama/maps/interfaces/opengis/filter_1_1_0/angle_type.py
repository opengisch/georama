from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AngleType(MeasureType):
    """Value of an angle quantity recorded as a single number, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for an angle, such as degrees or
    radians.
    """
