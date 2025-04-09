from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AcceptFormatsType:
    """Prioritized sequence of zero or more GetCapabilities operation response
    formats desired by client, with preferred formats listed first.

    Each response format shall be identified by its MIME type. See
    AcceptFormats parameter use subclause for more information.
    """

    output_format: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OutputFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        },
    )
