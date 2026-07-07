from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_georectified import (
    MdGeorectified,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_georeferenceable import (
    MdGeoreferenceable,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_grid_spatial_representation import (
    MdGridSpatialRepresentation,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_vector_spatial_representation import (
    MdVectorSpatialRepresentation,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdSpatialRepresentationPropertyType:
    class Meta:
        name = "MD_SpatialRepresentation_PropertyType"

    md_vector_spatial_representation: Optional[MdVectorSpatialRepresentation] = field(
        default=None,
        metadata={
            "name": "MD_VectorSpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_georectified: Optional[MdGeorectified] = field(
        default=None,
        metadata={
            "name": "MD_Georectified",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_georeferenceable: Optional[MdGeoreferenceable] = field(
        default=None,
        metadata={
            "name": "MD_Georeferenceable",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_grid_spatial_representation: Optional[MdGridSpatialRepresentation] = field(
        default=None,
        metadata={
            "name": "MD_GridSpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
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
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
