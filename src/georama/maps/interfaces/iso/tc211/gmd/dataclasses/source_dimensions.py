from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SourceDimensions:
    """
    Gml:sourceDimensions is the number of dimensions in the source CRS of this
    operation method.
    """

    class Meta:
        name = "sourceDimensions"
        namespace = "http://www.opengis.net/gml"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
