from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.bboxtype import (
    Bboxtype,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Bbox(Bboxtype):
    class Meta:
        name = "BBOX"
        namespace = "http://www.opengis.net/fes/2.0"
