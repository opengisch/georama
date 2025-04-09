from enum import Enum

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


class MdPixelOrientationCodeType(Enum):
    CENTER = "center"
    LOWER_LEFT = "lowerLeft"
    LOWER_RIGHT = "lowerRight"
    UPPER_RIGHT = "upperRight"
    UPPER_LEFT = "upperLeft"
