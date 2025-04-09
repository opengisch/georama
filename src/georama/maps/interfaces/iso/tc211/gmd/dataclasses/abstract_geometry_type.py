from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gmltype import (
    AbstractGmltype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometryType(AbstractGmltype):
    """All geometry elements are derived directly or indirectly from this abstract
    supertype. A geometry element may have an identifying attribute (gml:id), one
    or more names (elements identifier and name) and a description (elements
    description and descriptionReference) . It may be associated with a spatial
    reference system (attribute group gml:SRSReferenceGroup).

    The following rules shall be adhered to:
    -       Every geometry type shall derive from this abstract type.
    -       Every geometry element (i.e. an element of a geometry type) shall be directly or indirectly in the substitution group of AbstractGeometry.
    """

    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    axis_labels_attribute: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
    uom_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
