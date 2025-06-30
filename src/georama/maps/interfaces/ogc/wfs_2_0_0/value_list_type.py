from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.value_2 import Value2

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ValueListType:
    value: list[Value2] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        },
    )
