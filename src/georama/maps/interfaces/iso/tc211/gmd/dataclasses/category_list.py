from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_or_nil_reason_list_type import (
    CodeOrNilReasonListType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CategoryList(CodeOrNilReasonListType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
