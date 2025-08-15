from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_or_null_list_type import (
    CodeOrNullListType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CategoryList(CodeOrNullListType):
    """A space-separated list of terms or nulls.

    A single XML attribute codeSpace may be provided, which authorises
    all the terms in the list.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
