from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CodeListType:
    """List of values on a uniform nominal scale.

    List of text tokens. In a list context a token should not include
    any spaces, so xsd:Name is used instead of xsd:string. If a
    codeSpace attribute is present, then its value is a reference to a
    Reference System for the value, a dictionary or code list.
    """

    value: list[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    code_space: str | None = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
