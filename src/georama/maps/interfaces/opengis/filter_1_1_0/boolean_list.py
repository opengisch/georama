from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.null_enumeration_value import (
    NullEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BooleanList:
    """XML List based on XML Schema boolean type.

    An element of this type contains a space-separated list of boolean
    values {0,1,true,false}
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: list[str | NullEnumerationValue] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
