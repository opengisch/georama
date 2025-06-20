from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import (
    FeatureCollectionType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.data_source import DataSource
from georama.maps.interfaces.opengis.filter_1_1_0.history import History
from georama.maps.interfaces.opengis.filter_1_1_0.track import Track
from georama.maps.interfaces.opengis.filter_1_1_0.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DynamicFeatureCollectionType(FeatureCollectionType):
    """
    A dynamic feature collection may possess a history and/or a timestamp.
    """

    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    track: Optional[Track] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    history: Optional[History] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
