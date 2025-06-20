from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_base_type import (
    AbstractReferenceSystemBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks
from georama.maps.interfaces.opengis.filter_1_1_0.scope import Scope
from georama.maps.interfaces.opengis.filter_1_1_0.srs_id import SrsId
from georama.maps.interfaces.opengis.filter_1_1_0.valid_area import ValidArea

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractReferenceSystemType(AbstractReferenceSystemBaseType):
    """
    Description of a spatial and/or temporal reference system used by a dataset.

    :ivar srs_id: Set of alterative identifications of this reference
        system. The first srsID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this reference
        system, including source information.
    :ivar valid_area:
    :ivar scope:
    """

    srs_id: list[SrsId] = field(
        default_factory=list,
        metadata={
            "name": "srsID",
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
