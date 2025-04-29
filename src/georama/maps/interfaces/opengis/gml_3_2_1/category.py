from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Category:
    """
    A gml:Category has an optional XML attribute codeSpace, whose value is a URI
    which identifies a dictionary, codelist or authority for the term.
    """

    class Meta:
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"

    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
        },
    )
