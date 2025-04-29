from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.angle_type import AngleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GreenwichLongitude(AngleType):
    """Gml:greenwichLongitude is the longitude of the prime meridian measured from
    the Greenwich meridian, positive eastward.

    If the value of the prime meridian "name" is "Greenwich" then the
    value of greenwichLongitude shall be 0 degrees.
    """

    class Meta:
        name = "greenwichLongitude"
        namespace = "http://www.opengis.net/gml/3.2"
