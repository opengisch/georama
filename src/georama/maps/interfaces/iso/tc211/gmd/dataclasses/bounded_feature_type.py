from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_feature_type import (
    AbstractFeatureType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.bounded_by import BoundedBy

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundedFeatureType(AbstractFeatureType):
    bounded_by: BoundedBy | None = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
