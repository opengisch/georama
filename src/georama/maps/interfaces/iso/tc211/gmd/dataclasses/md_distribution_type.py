from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_digital_transfer_options_property_type import (
    MdDigitalTransferOptionsPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_distributor_type import (
    MdDistributorPropertyType,
    MdFormatPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributionType(AbstractObjectType):
    """
    Information about the distributor of and options for obtaining the dataset.
    """

    class Meta:
        name = "MD_Distribution_Type"

    distribution_format: list[MdFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributionFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    distributor: list[MdDistributorPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    transfer_options: list[MdDigitalTransferOptionsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "transferOptions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
