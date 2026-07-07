from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.md_range_dimension_type import (
    MdRangeDimensionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdRangeDimension(MdRangeDimensionType):
    class Meta:
        name = "MD_RangeDimension"
        namespace = "http://www.isotc211.org/2005/gmd"
