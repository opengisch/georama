from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)
from georama.maps.interfaces.opengis.filter_1_1_0.bounded_by import BoundedBy
from georama.maps.interfaces.opengis.filter_1_1_0.location import Location
from georama.maps.interfaces.opengis.filter_1_1_0.priority_location import (
    PriorityLocation,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractFeatureType(AbstractGmltype):
    """An abstract feature provides a set of common properties, including id,
    metaDataProperty, name and description inherited from AbstractGMLType, plus
    boundedBy.

    A concrete feature type must derive from this type and specify additional  properties in an application schema. A feature must possess an identifying attribute ('id' - 'fid' has been deprecated).
    """

    bounded_by: BoundedBy | None = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    priority_location_or_location: PriorityLocation | Location | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "priorityLocation",
                    "type": PriorityLocation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "location",
                    "type": Location,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
