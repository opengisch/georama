from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ex_geographic_bounding_box_type import (
    ExGeographicBoundingBoxType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExGeographicBoundingBox(ExGeographicBoundingBoxType):
    class Meta:
        name = "EX_GeographicBoundingBox"
        namespace = "http://www.isotc211.org/2005/gmd"
