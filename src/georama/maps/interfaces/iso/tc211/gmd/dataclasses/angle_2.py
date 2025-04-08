from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.angle_type import AngleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Angle2(AngleType):
    """
    The gml:angle property element is used to record the value of an angle quantity
    as a single number, with its units.
    """

    class Meta:
        name = "angle"
        namespace = "http://www.opengis.net/gml"
