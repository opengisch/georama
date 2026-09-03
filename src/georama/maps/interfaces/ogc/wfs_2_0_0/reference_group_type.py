from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.basic_identification_type import (
    BasicIdentificationType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.reference import Reference
from georama.maps.interfaces.ogc.wfs_2_0_0.service_reference import ServiceReference

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ReferenceGroupType(BasicIdentificationType):
    """Logical group of one or more references to remote and/or local resources,
    allowing including metadata about that group.

    A Group can be used instead of a Manifest that can only contain one
    group.
    """

    service_reference_or_reference: list[ServiceReference | Reference] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceReference",
                    "type": ServiceReference,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
                {
                    "name": "Reference",
                    "type": Reference,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
            ),
        },
    )
