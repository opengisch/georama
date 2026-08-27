from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.lang_value import LangValue

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Abstract2:
    class Meta:
        name = "Abstract"
        namespace = "http://www.opengis.net/wfs/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: str | LangValue = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
