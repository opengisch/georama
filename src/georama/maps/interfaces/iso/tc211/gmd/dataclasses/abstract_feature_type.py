from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gmltype import (
    AbstractGmltype,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.bounded_by import BoundedBy
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.location import Location
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.priority_location import (
    PriorityLocation,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractFeatureType(AbstractGmltype):
    """The basic feature model is given by the gml:AbstractFeatureType.

    The content model for gml:AbstractFeatureType adds two specific
    properties suitable for geographic features to the content model
    defined in gml:AbstractGMLType. The value of the gml:boundedBy
    property describes an envelope that encloses the entire feature
    instance, and is primarily useful for supporting rapid searching for
    features that occur in a particular location. The value of the
    gml:location property describes the extent, position or relative
    location of the feature.
    """

    bounded_by: BoundedBy | None = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    priority_location: PriorityLocation | None = field(
        default=None,
        metadata={
            "name": "priorityLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    location: Location | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
