from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinate_system_axis_type import (
    CoordinateSystemAxisType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxis(CoordinateSystemAxisType):
    """
    Gml:CoordinateSystemAxis is a definition of a coordinate system axis.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
