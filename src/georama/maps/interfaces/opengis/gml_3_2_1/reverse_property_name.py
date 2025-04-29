from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ReversePropertyName:
    """If the value of an object property is another object and that object
    contains also a property for the association between the two objects, then this
    name of the reverse property may be encoded in a gml:reversePropertyName
    element in an appinfo annotation of the property element to document the
    constraint between the two properties.

    The value of the element shall contain the qualified name of the
    property element.
    """

    class Meta:
        name = "reversePropertyName"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
