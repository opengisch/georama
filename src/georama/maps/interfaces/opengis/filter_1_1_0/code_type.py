from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CodeType:
    """Name or code with an (optional) authority.

    Text token. If the codeSpace attribute is present, then its value
    should identify a dictionary, thesaurus or authority for the term,
    such as the organisation who assigned the value, or the dictionary
    from which it is taken. A text string with an optional codeSpace
    attribute.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code_space: str | None = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
