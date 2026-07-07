from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ValuesReference:
    """Reference to externally specified list of all the valid values and/or ranges
    of values for this quantity.

    (Informative: This element was simplified from the metaDataProperty
    element in GML 3.0.)
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/ows/1.1",
            "required": True,
        },
    )
