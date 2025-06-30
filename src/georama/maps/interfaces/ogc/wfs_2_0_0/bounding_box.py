from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.bounding_box_type import BoundingBoxType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class BoundingBox(BoundingBoxType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
