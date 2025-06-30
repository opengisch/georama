from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AccessConstraints:
    """Access constraint applied to assure the protection of privacy or
    intellectual property, or any other restrictions on retrieving or using data
    from or otherwise using this server.

    The reserved value NONE (case insensitive) shall be used to mean no
    access constraints are imposed.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
