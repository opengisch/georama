from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationVersion:
    """Version of the coordinate transformation (i.e., instantiation due to the
    stochastic nature of the parameters).

    Mandatory when describing a transformation, and should not be
    supplied for a conversion.
    """

    class Meta:
        name = "operationVersion"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
