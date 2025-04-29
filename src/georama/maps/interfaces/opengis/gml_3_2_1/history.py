from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.history_property_type import (
    HistoryPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class History(HistoryPropertyType):
    """A generic sequence of events constitute a gml:history of an object.

    The gml:history element contains a set of elements in the
    substitution group headed by the abstract element
    gml:AbstractTimeSlice, representing the time-varying properties of
    interest. The history property of a dynamic feature associates a
    feature instance with a sequence of time slices (i.e. change events)
    that encapsulate the evolution of the feature.
    """

    class Meta:
        name = "history"
        namespace = "http://www.opengis.net/gml/3.2"
