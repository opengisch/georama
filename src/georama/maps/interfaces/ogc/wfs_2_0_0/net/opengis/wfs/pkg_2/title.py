from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.xml.pkg_1998.namespace.lang_value import (
    LangValue,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Title:
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Union[str, LangValue] = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
