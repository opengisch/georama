from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_id_type import AbstractIdType
from georama.maps.interfaces.ogc.wfs_2_0_0.version_action_tokens import (
    VersionActionTokens,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ResourceIdType(AbstractIdType):
    rid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    previous_rid: str | None = field(
        default=None,
        metadata={
            "name": "previousRid",
            "type": "Attribute",
        },
    )
    version: VersionActionTokens | int | XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    start_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Attribute",
        },
    )
    end_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Attribute",
        },
    )
