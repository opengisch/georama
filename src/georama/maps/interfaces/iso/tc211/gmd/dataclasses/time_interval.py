from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_interval_length_type import (
    TimeIntervalLengthType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeInterval(TimeIntervalLengthType):
    """Gml:timeInterval conforms to ISO 11404 which is based on floating point
    values for temporal length.

    ISO 11404 syntax specifies the use of a positiveInteger together
    with appropriate values for radix and factor. The resolution of the
    time interval is to one radix ^(-factor) of the specified time unit.
    The value of the unit is either selected from the units for time
    intervals from ISO 31-1:1992, or is another suitable unit.  The
    encoding is defined for GML in gml:TimeUnitType. The second
    component of this union type provides a method for indicating time
    units other than the six standard units given in the enumeration.
    """

    class Meta:
        name = "timeInterval"
        namespace = "http://www.opengis.net/gml"
