from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.bounding_shape_type import (
    BoundingShapeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundedBy(BoundingShapeType):
    class Meta:
        name = "boundedBy"
        namespace = "http://www.opengis.net/gml"
