from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Covariance:
    """
    Value of covariance matrix element.
    """

    class Meta:
        name = "covariance"
        namespace = "http://www.opengis.net/gml"

    value: float | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
