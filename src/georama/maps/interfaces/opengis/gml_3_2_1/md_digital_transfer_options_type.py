from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_online_resource_property_type import (
    CiOnlineResourcePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_medium_property_type import (
    MdMediumPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.real_property_type import (
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

    units_of_distribution: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "unitsOfDistribution",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    transfer_size: RealPropertyType | None = field(
        default=None,
        metadata={
            "name": "transferSize",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    on_line: list[CiOnlineResourcePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "onLine",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    off_line: MdMediumPropertyType | None = field(
        default=None,
        metadata={
            "name": "offLine",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
