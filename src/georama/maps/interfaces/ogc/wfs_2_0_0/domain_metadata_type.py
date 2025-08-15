from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class DomainMetadataType:
    """References metadata about a quantity, and provides a name for this metadata.

    (Informative: This element was simplified from the metaDataProperty
    element in GML 3.0.)
    """

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
        },
    )
