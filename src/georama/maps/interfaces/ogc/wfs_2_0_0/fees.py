from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Fees:
    """Fees and terms for retrieving data from or otherwise using this server,
    including the monetary units as specified in ISO 4217.

    The reserved value NONE (case insensitive) shall be used to mean no
    fees or terms.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
