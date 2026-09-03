from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class AbstractTransactionActionType:
    handle: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
