from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SrsName(CodeType):
    """
    The name by which this reference system is identified.
    """

    class Meta:
        name = "srsName"
        namespace = "http://www.opengis.net/gml"
