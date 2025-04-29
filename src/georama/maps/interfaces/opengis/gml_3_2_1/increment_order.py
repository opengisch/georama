from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class IncrementOrder(Enum):
    X_Y = "+x+y"
    Y_X = "+y+x"
    X_Y_1 = "+x-y"
    X_Y_2 = "-x-y"
