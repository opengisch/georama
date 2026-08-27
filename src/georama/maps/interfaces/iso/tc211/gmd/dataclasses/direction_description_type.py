from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.compass_point_enumeration import (
    CompassPointEnumeration,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.reference_type import (
    ReferenceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionDescriptionType:
    """Direction descriptions are specified by a compass point code, a keyword, a
    textual description or a reference to a description.

    A gml:compassPoint is specified by a simple enumeration. In
    addition, thre elements to contain text-based descriptions of
    direction are provided. If the direction is specified using a term
    from a list, gml:keyword should be used, and the list indicated
    using the value of the codeSpace attribute. if the direction is
    decribed in prose, gml:direction or gml:reference should be used,
    allowing the value to be included inline or by reference.
    """

    compass_point: CompassPointEnumeration | None = field(
        default=None,
        metadata={
            "name": "compassPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    keyword: CodeType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    reference: ReferenceType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
