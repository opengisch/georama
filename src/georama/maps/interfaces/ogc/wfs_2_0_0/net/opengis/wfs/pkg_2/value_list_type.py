from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.wfs.pkg_2.value import Value

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ValueListType:
    value: list[Value] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        },
    )
