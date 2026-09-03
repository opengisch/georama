from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TargetDimensions:
    """
    Gml:targetDimensions is the number of dimensions in the target CRS of this
    operation method.
    """

    class Meta:
        name = "targetDimensions"
        namespace = "http://www.opengis.net/gml/3.2"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
