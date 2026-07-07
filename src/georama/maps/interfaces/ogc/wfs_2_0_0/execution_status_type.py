from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ExecutionStatusType:
    status: str = field(
        init=False,
        default="OK",
        metadata={
            "type": "Attribute",
        },
    )
