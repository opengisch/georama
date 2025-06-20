from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeasureDescription(CodeType):
    """
    A description of the position accuracy parameter(s) provided.
    """

    class Meta:
        name = "measureDescription"
        namespace = "http://www.opengis.net/gml"
