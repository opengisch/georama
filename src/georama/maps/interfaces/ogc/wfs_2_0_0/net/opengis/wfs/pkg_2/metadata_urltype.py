from dataclasses import dataclass, field
from typing import Optional

from wfs_2_0_0.org.w3.pkg_1999.xlink.actuate_type import ActuateType
from wfs_2_0_0.org.w3.pkg_1999.xlink.show_type import ShowType
from wfs_2_0_0.org.w3.pkg_1999.xlink.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class MetadataUrltype:
    class Meta:
        name = "MetadataURLType"

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
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
