from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_feature_type import (
    AbstractFeatureType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.bounded_by import BoundedBy

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundedFeatureType(AbstractFeatureType):
    bounded_by: BoundedBy | None = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
