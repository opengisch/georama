from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class OutputFormatListType:
    format: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        },
    )
