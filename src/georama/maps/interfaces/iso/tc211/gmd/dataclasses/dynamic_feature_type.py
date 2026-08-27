from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_feature_type import (
    AbstractFeatureType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.data_source import DataSource
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.data_source_reference import (
    DataSourceReference,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.history import History
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.track import Track
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DynamicFeatureType(AbstractFeatureType):
    valid_time: ValidTime | None = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    track: Track | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    history: History | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    data_source_reference: DataSourceReference | None = field(
        default=None,
        metadata={
            "name": "dataSourceReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
