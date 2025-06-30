from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class OutputFormat:
    """Reference to a format in which this data can be encoded and transferred.

    More specific parameter names should be used by specific OWS
    specifications wherever applicable. More than one such parameter can
    be included for different purposes.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        },
    )
