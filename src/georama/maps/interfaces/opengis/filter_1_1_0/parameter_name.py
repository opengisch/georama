from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterName(CodeType):
    """
    The name by which this operation parameter is identified.
    """

    class Meta:
        name = "parameterName"
        namespace = "http://www.opengis.net/gml"
