from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.wfs.pkg_2.element import Element

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ExtendedDescriptionType:
    element: list[Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        },
    )
