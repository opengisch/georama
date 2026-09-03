from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.distance_property_type import (
    DistancePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_representative_fraction_property_type import (
    MdRepresentativeFractionPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdResolutionType:
    class Meta:
        name = "MD_Resolution_Type"

    equivalent_scale: MdRepresentativeFractionPropertyType | None = field(
        default=None,
        metadata={
            "name": "equivalentScale",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    distance: DistancePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
