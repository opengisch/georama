from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.polygon_type import PolygonType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundingPolygon(PolygonType):
    """
    A bounding polygon defining the horizontal spatial domain of this object.
    """

    class Meta:
        name = "boundingPolygon"
        namespace = "http://www.opengis.net/gml"
