from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_slice_type import (
    AbstractTimeSliceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimeSlice(AbstractTimeSliceType):
    """To describe an event — an action that occurs at an instant or over an
    interval of time — GML provides the gml:AbtractTimeSlice element.

    A timeslice encapsulates the time-varying properties of a dynamic
    feature -- it shall be extended to represent a time stamped
    projection of a specific feature. The gml:dataSource property
    describes how the temporal data was acquired. A
    gml:AbstractTimeSlice instance is a GML object that encapsulates
    updates of the dynamic—or volatile—properties that reflect some
    change event; it thus includes only those feature properties that
    have actually changed due to some process. gml:AbstractTimeSlice
    basically provides a facility for attribute-level time stamping, in
    contrast to the object-level time stamping of dynamic feature
    instances. The time slice can thus be viewed as event or process-
    oriented, whereas a snapshot is more state or structure-oriented. A
    timeslice has richer causality, whereas a snapshot merely portrays
    the status of the whole.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
