from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.geodesic_string_type import (
    GeodesicStringType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodesicType(GeodesicStringType):
    pass
