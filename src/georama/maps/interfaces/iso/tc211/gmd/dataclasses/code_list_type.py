from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CodeListType:
    """Gml:CodeListType provides for lists of terms.

    The values in an instance element shall all be valid according to
    the rules of the dictionary, classification scheme, or authority
    identified by the value of its codeSpace attribute.
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
