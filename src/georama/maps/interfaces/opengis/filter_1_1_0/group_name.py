from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GroupName(CodeType):
    """
    The name by which this operation parameter group is identified.
    """

    class Meta:
        name = "groupName"
        namespace = "http://www.opengis.net/gml"
