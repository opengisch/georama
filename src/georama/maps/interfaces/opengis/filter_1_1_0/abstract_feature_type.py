from dataclasses import dataclass, field
from typing import Optional

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

    :ivar bounded_by:
    :ivar priority_location:
    :ivar location: deprecated in GML version 3.1
    """

    bounded_by: Optional[BoundedBy] = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    priority_location: Optional[PriorityLocation] = field(
        default=None,
        metadata={
            "name": "priorityLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
