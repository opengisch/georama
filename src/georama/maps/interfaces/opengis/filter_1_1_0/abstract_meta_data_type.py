from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractMetaDataType:
    """
    An abstract base type for complex metadata types.
    """

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
