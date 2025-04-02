from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.created_or_modified_feature_type import (
    CreatedOrModifiedFeatureType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ActionResultsType:
    feature: list[CreatedOrModifiedFeatureType] = field(
        default_factory=list,
        metadata={
            "name": "Feature",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        },
    )
