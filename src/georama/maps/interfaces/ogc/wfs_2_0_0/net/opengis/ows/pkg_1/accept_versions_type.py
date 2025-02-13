from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AcceptVersionsType:
    """Prioritized sequence of one or more specification versions accepted by
    client, with preferred versions listed first.

    See Version negotiation subclause for more information.
    """

    version: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "min_occurs": 1,
            "pattern": r"\d+\.\d?\d\.\d?\d",
        },
    )
