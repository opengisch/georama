from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ci_online_resource_property_type import (
    CiOnlineResourcePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_medium_property_type import (
    MdMediumPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.real_property_type import (
    RealPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDigitalTransferOptionsType(AbstractObjectType):
    """
    Technical means and media by which a dataset is obtained from the distributor.
    """

    class Meta:
        name = "MD_DigitalTransferOptions_Type"

    units_of_distribution: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "unitsOfDistribution",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    transfer_size: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "transferSize",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    on_line: List[CiOnlineResourcePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "onLine",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    off_line: Optional[MdMediumPropertyType] = field(
        default=None,
        metadata={
            "name": "offLine",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
