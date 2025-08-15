from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ValueFile:
    """Gml:valueFile is a reference to a file or a part of a file containing one or
    more parameter values, each numeric value with its associated unit of measure.

    When referencing a part of a file, that file shall contain multiple
    identified parts, such as an XML encoded document. Furthermore, the
    referenced file or part of a file may reference another part of the
    same or different files, as allowed in XML documents.
    """

    class Meta:
        name = "valueFile"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
