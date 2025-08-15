from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.code_list_value_type import (
    CodeListValueType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdTopologyLevelCode(CodeListValueType):
    class Meta:
        name = "MD_TopologyLevelCode"
        namespace = "http://www.isotc211.org/2005/gmd"
