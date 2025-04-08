from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class CompassPointEnumeration(Enum):
    """These directions are necessarily approximate, giving direction with a
    precision of 22.5°.

    It is thus generally unnecessary to specify the reference frame,
    though this may be detailed in the definition of a GML application
    language.
    """

    N = "N"
    NNE = "NNE"
    NE = "NE"
    ENE = "ENE"
    E = "E"
    ESE = "ESE"
    SE = "SE"
    SSE = "SSE"
    S = "S"
    SSW = "SSW"
    SW = "SW"
    WSW = "WSW"
    W = "W"
    WNW = "WNW"
    NW = "NW"
    NNW = "NNW"
