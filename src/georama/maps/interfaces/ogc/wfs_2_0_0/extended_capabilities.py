from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ExtendedCapabilities:
    """
    Individual software vendors and servers can use this element to provide
    metadata about any additional server abilities.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
