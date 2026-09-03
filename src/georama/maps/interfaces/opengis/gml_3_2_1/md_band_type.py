from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.integer_property_type import (
    IntegerPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_range_dimension_type import (
    MdRangeDimensionType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.real_property_type import (
    RealPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.uom_length_property_type import (
    UomLengthPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdBandType(MdRangeDimensionType):
    class Meta:
        name = "MD_Band_Type"

    max_value: RealPropertyType | None = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    min_value: RealPropertyType | None = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    units: UomLengthPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    peak_response: RealPropertyType | None = field(
        default=None,
        metadata={
            "name": "peakResponse",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    bits_per_value: IntegerPropertyType | None = field(
        default=None,
        metadata={
            "name": "bitsPerValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    tone_gradation: IntegerPropertyType | None = field(
        default=None,
        metadata={
            "name": "toneGradation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    scale_factor: RealPropertyType | None = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    offset: RealPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
