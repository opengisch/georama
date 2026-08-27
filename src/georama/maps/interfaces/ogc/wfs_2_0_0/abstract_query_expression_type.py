from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractQueryExpressionType:
    handle: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
