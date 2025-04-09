from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.basic_identification_type import (
    BasicIdentificationType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.reference import (
    Reference,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.service_reference import (
    ServiceReference,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ReferenceGroupType(BasicIdentificationType):
    """Logical group of one or more references to remote and/or local resources,
    allowing including metadata about that group.

    A Group can be used instead of a Manifest that can only contain one
    group.
    """

    service_reference: list[ServiceReference] = field(
        default_factory=list,
        metadata={
            "name": "ServiceReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    reference: list[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
