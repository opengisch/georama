from dataclasses import dataclass, field
from typing import Optional, Union

from wfs_2_0_0.net.opengis.fes.pkg_2.abstract_id_type import AbstractIdType
from wfs_2_0_0.net.opengis.fes.pkg_2.version_action_tokens import VersionActionTokens
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ResourceIdType(AbstractIdType):
    rid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    previous_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "previousRid",
            "type": "Attribute",
        },
    )
    version: Optional[Union[VersionActionTokens, int, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Attribute",
        },
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Attribute",
        },
    )
