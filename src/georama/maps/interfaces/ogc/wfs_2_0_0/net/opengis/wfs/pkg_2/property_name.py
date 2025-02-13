from dataclasses import dataclass, field
from typing import Optional, Union
from xml.etree.ElementTree import QName

from wfs_2_0_0.net.opengis.wfs.pkg_2.resolve_value_type import ResolveValueType
from wfs_2_0_0.net.opengis.wfs.pkg_2.star_string_type import StarStringType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class PropertyName:
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    resolve: ResolveValueType = field(
        default=ResolveValueType.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_depth: Union[int, StarStringType] = field(
        default=StarStringType.ASTERISK,
        metadata={
            "name": "resolveDepth",
            "type": "Attribute",
        },
    )
    resolve_timeout: int = field(
        default=300,
        metadata={
            "name": "resolveTimeout",
            "type": "Attribute",
        },
    )
    resolve_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "resolvePath",
            "type": "Attribute",
        },
    )
