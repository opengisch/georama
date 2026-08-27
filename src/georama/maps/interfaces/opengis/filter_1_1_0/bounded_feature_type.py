from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_feature_type import (
    AbstractFeatureType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.bounded_by import BoundedBy

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundedFeatureType(AbstractFeatureType):
    """
    Makes boundedBy mandatory.
    """

    bounded_by: BoundedBy | None = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
