from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Version:
    """Identifier of the version of the associated codeSpace or code, as specified
    by the codeSpace or code authority.

    This version is included only when the "code" or "codeSpace" uses
    versions. When appropriate, the version is identified by the
    effective date, coded using ISO 8601 date format.
    """

    class Meta:
        name = "version"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
