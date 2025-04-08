from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vertical_cstype import (
    VerticalCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCs1(VerticalCstype):
    """Gml:VerticalCS is a one-dimensional coordinate system used to record the
    heights or depths of points.

    Such a coordinate system is usually dependent on the Earth's gravity
    field, perhaps loosely as when atmospheric pressure is the basis for
    the vertical coordinate system axis. A VerticalCS shall have one
    gml:axis property element.
    """

    class Meta:
        name = "VerticalCS"
        namespace = "http://www.opengis.net/gml"
