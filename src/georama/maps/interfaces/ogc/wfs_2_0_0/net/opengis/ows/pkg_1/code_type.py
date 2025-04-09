from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class CodeType:
    """Name or code with an (optional) authority.

    If the codeSpace attribute is present, its value shall reference a
    dictionary, thesaurus, or authority for the name or code, such as
    the organisation who assigned the value, or the dictionary from
    which it is taken. Type copied from basicTypes.xsd of GML 3 with
    documentation edited, for possible use outside the
    ServiceIdentification section of a service metadata document.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
