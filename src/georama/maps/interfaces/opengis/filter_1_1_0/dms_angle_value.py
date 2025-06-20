from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.dmsangle_type import DmsangleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DmsAngleValue(DmsangleType):
    """
    Value of an angle operation parameter, in either degree-minute-second format or
    single value format.
    """

    class Meta:
        name = "dmsAngleValue"
        namespace = "http://www.opengis.net/gml"
