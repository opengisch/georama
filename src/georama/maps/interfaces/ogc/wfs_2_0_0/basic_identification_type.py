from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.description_type import DescriptionType
from georama.maps.interfaces.ogc.wfs_2_0_0.identifier import Identifier
from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class BasicIdentificationType(DescriptionType):
    """
    Basic metadata identifying and describing a set of data.

    :ivar identifier: Optional unique identifier or name of this
        dataset.
    :ivar metadata: Optional unordered list of additional metadata about
        this data(set). A list of optional metadata elements for this
        data identification could be specified in the Implementation
        Specification for this service.
    """

    identifier: Identifier | None = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    metadata: list[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
