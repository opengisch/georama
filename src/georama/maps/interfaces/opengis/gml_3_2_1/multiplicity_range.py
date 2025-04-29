from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.multiplicity_range_type import (
    MultiplicityRangeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MultiplicityRange(MultiplicityRangeType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
