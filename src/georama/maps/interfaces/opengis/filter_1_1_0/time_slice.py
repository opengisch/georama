from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_slice_type import (
    AbstractTimeSliceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeSlice(AbstractTimeSliceType):
    class Meta:
        name = "_TimeSlice"
        namespace = "http://www.opengis.net/gml"
