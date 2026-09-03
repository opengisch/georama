from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.lang_value import LangValue

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class LanguageStringType:
    """
    Text string with the language of the string identified as recommended in the
    XML 1.0 W3C Recommendation, section 2.12.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
