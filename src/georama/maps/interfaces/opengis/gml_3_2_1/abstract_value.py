from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractValue:
    """Gml:AbstractValue is an abstract element which acts as the head of a
    substitution group which contains gml:AbstractScalarValue,
    gml:AbstractScalarValueList, gml:CompositeValue and gml:ValueExtent, and
    (transitively) the elements in their substitution groups.

    These elements may be used in an application schema as variables, so
    that in an XML instance document any member of its substitution
    group may occur.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
