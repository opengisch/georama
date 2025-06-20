from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.bboxtype import Bboxtype

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Bbox(Bboxtype):
    class Meta:
        name = "BBOX"
        namespace = "http://www.opengis.net/ogc"
