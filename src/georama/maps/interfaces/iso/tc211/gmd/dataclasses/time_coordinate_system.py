from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_coordinate_system_type import (
    TimeCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCoordinateSystem(TimeCoordinateSystemType):
    """A temporal coordinate system shall be based on a continuous interval scale
    defined in terms of a single time interval.

    The differences to ISO 19108 TM_CoordinateSystem are:
    -       the origin is specified either using the property gml:originPosition whose value is a direct time position, or using the property gml:origin whose model is gml:TimeInstantPropertyType; this permits more flexibility in representation and also supports referring to a value fixed elsewhere;
    -       the interval uses gml:TimeIntervalLengthType.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
