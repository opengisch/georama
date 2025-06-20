from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class IncrementOrder(Enum):
    """The enumeration value here indicates the incrementation order  to be used on
    the first 2 axes, i.e. "+x-y" means that the points on the first axis are to be
    traversed from lowest to highest and  the points on the second axis are to be
    traversed from highest to lowest.

    The points on all other axes (if any) beyond the first 2 are assumed
    to increment from lowest to highest.
    """

    X_Y = "+x+y"
    Y_X = "+y+x"
    X_Y_1 = "+x-y"
    X_Y_2 = "-x-y"
