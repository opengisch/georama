from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.sort_property_type import (
    SortPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SortByType:
    sort_property: list[SortPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "SortProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
