from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class CodeListValueType:
    class Meta:
        name = "CodeListValue_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code_list: str | None = field(
        default=None,
        metadata={
            "name": "codeList",
            "type": "Attribute",
            "required": True,
        },
    )
    code_list_value: str | None = field(
        default=None,
        metadata={
            "name": "codeListValue",
            "type": "Attribute",
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
