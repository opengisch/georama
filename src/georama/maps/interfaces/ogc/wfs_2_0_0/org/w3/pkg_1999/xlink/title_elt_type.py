from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.type_type import (
    TypeType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.xml.pkg_1998.namespace.lang_value import (
    LangValue,
)

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class TitleEltType:
    """
    :ivar type_value:
    :ivar lang: xml:lang is not required, but provides much of the
        motivation for title elements in addition to attributes, and so
        is provided here for convenience.
    :ivar content:
    """

    class Meta:
        name = "titleEltType"

    type_value: TypeType = field(
        init=False,
        default=TypeType.TITLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
