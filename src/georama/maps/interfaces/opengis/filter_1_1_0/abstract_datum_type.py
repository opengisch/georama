from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_datum_base_type import (
    AbstractDatumBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.anchor_point import AnchorPoint
from georama.maps.interfaces.opengis.filter_1_1_0.datum_id import DatumId
from georama.maps.interfaces.opengis.filter_1_1_0.realization_epoch import (
    RealizationEpoch,
)
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks
from georama.maps.interfaces.opengis.filter_1_1_0.scope import Scope
from georama.maps.interfaces.opengis.filter_1_1_0.valid_area import ValidArea

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractDatumType(AbstractDatumBaseType):
    """A datum specifies the relationship of a coordinate system to the earth, thus
    creating a coordinate reference system.

    A datum uses a parameter or set of parameters that determine the
    location of the origin of the coordinate reference system. Each
    datum subtype can be associated with only specific types of
    coordinate systems. This abstract complexType shall not be used,
    extended, or restricted, in an Application Schema, to define a
    concrete subtype with a meaning equivalent to a concrete subtype
    specified in this document.

    :ivar datum_id: Set of alternative identifications of this datum.
        The first datumID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on this reference system, including source
        information.
    :ivar anchor_point:
    :ivar realization_epoch:
    :ivar valid_area:
    :ivar scope:
    """

    datum_id: list[DatumId] = field(
        default_factory=list,
        metadata={
            "name": "datumID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    anchor_point: Optional[AnchorPoint] = field(
        default=None,
        metadata={
            "name": "anchorPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    realization_epoch: Optional[RealizationEpoch] = field(
        default=None,
        metadata={
            "name": "realizationEpoch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    valid_area: Optional[ValidArea] = field(
        default=None,
        metadata={
            "name": "validArea",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    scope: Optional[Scope] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
