from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.angle_type import AngleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Angle2(AngleType):
    """
    The gml:angle property element is used to record the value of an angle quantity
    as a single number, with its units.
    """

    class Meta:
        name = "angle"
        namespace = "http://www.opengis.net/gml/3.2"
