from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_range_dimension_type import (
    MdRangeDimensionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdRangeDimension(MdRangeDimensionType):
    class Meta:
        name = "MD_RangeDimension"
        namespace = "http://www.isotc211.org/2005/gmd"
