from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TargetDimensions:
    """
    Number of dimensions in the target CRS of this operation method.
    """

    class Meta:
        name = "targetDimensions"
        namespace = "http://www.opengis.net/gml"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
