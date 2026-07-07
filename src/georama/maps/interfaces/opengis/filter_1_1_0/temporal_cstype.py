from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCstype(AbstractCoordinateSystemType):
    """A one-dimensional coordinate system containing a single time axis, used to
    describe the temporal position of a point in the specified time units from a
    specified time origin.

    A TemporalCS shall have one usesAxis association.
    """

    class Meta:
        name = "TemporalCSType"
