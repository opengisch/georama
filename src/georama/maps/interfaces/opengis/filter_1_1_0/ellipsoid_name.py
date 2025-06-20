from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidName(CodeType):
    """
    The name by which this ellipsoid is identified.
    """

    class Meta:
        name = "ellipsoidName"
        namespace = "http://www.opengis.net/gml"
