from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValueFile:
    """Reference to a file or a part of a file containing one or more parameter
    values, each numeric value with its associated unit of measure.

    When referencing a part of a file, that file must contain multiple
    identified parts, such as an XML encoded document. Furthermore, the
    referenced file or part of a file can reference another part of the
    same or different files, as allowed in XML documents.
    """

    class Meta:
        name = "valueFile"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
