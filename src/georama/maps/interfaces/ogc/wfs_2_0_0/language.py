from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Language:
    """Identifier of a language used by the data(set) contents.

    This language identifier shall be as specified in IETF RFC 4646.
    When this element is omitted, the language used is not identified.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
