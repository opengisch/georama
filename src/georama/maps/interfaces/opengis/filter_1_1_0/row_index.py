from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RowIndex:
    """
    Row number of this covariance element value.
    """

    class Meta:
        name = "rowIndex"
        namespace = "http://www.opengis.net/gml"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
