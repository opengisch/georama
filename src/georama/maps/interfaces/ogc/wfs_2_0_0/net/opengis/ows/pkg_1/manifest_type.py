from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.ows.pkg_1.basic_identification_type import (
    BasicIdentificationType,
)
from wfs_2_0_0.net.opengis.ows.pkg_1.reference_group import ReferenceGroup

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ManifestType(BasicIdentificationType):
    """
    Unordered list of one or more groups of references to remote and/or local
    resources.
    """

    reference_group: list[ReferenceGroup] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "min_occurs": 1,
        },
    )
