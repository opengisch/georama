from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.md_legal_constraints import (
    MdLegalConstraints,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdLegalConstraintsPropertyType:
    class Meta:
        name = "MD_LegalConstraints_PropertyType"

    md_legal_constraints: Optional[MdLegalConstraints] = field(
        default=None,
        metadata={
            "name": "MD_LegalConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
