from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CsName(CodeType):
    """
    The name by which this coordinate system is identified.
    """

    class Meta:
        name = "csName"
        namespace = "http://www.opengis.net/gml"
