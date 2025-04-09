from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TargetElement:
    class Meta:
        name = "targetElement"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
