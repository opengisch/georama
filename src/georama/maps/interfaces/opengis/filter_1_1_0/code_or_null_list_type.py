from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.null_enumeration_value import (
    NullEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CodeOrNullListType:
    """List of values on a uniform nominal scale.

    List of text tokens. In a list context a token should not include
    any spaces, so xsd:Name is used instead of xsd:string. A member of
    the list may be a typed null. If a codeSpace attribute is present,
    then its value is a reference to a Reference System for the value, a
    dictionary or code list.
    """

    value: list[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
