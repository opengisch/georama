from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.sort_property_type import (
    SortPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SortByType:
    sort_property: list[SortPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "SortProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        },
    )
