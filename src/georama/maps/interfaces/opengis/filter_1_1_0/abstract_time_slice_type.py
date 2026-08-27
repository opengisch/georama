from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)
from georama.maps.interfaces.opengis.filter_1_1_0.data_source import DataSource
from georama.maps.interfaces.opengis.filter_1_1_0.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeSliceType(AbstractGmltype):
    """A timeslice encapsulates the time-varying properties of a dynamic feature--
    it must be extended to represent a timestamped projection of a feature.

    The dataSource property describes how the temporal data was
    acquired.
    """

    valid_time: ValidTime | None = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    data_source: DataSource | None = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
