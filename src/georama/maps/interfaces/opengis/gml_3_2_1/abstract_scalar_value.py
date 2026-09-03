from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractScalarValue:
    """
    Gml:AbstractScalarValue is an abstract element which acts as the head of a
    substitution group which contains gml:Boolean, gml:Category, gml:Count and
    gml:Quantity, and (transitively) the elements in their substitution groups.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    any_element: object | None = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
