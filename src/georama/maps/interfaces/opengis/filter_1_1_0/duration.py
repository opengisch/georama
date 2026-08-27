from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Duration:
    """This element is an instance of the primitive xsd:duration simple type to
    enable use of the ISO 8601 syntax for temporal length (e.g. P5DT4H30M).

    It is a valid subtype of TimeDurationType according to section
    3.14.6, rule 2.2.4 in XML Schema, Part 1.
    """

    class Meta:
        name = "duration"
        namespace = "http://www.opengis.net/gml"

    value: XmlDuration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
