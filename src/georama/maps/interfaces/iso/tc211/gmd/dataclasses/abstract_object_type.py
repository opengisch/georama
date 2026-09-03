from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class AbstractObjectType:
    class Meta:
        name = "AbstractObject_Type"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    uuid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
