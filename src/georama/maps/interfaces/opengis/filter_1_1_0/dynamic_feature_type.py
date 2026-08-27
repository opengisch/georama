from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_feature_type import (
    AbstractFeatureType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.data_source import DataSource
from georama.maps.interfaces.opengis.filter_1_1_0.history import History
from georama.maps.interfaces.opengis.filter_1_1_0.track import Track
from georama.maps.interfaces.opengis.filter_1_1_0.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DynamicFeatureType(AbstractFeatureType):
    """
    A dynamic feature may possess a history and/or a timestamp.
    """

    valid_time: ValidTime | None = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    track_or_history: Track | History | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "track",
                    "type": Track,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "history",
                    "type": History,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
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
