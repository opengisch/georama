from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.code_or_nil_reason_list_type import (
    CodeOrNilReasonListType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CategoryExtentType(CodeOrNilReasonListType):
    pass
