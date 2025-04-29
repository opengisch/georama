from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_distribution_units import (
    MdDistributionUnits,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributionUnitsPropertyType:
    class Meta:
        name = "MD_DistributionUnits_PropertyType"

    md_distribution_units: Optional[MdDistributionUnits] = field(
        default=None,
        metadata={
            "name": "MD_DistributionUnits",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
