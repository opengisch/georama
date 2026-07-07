from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.range_parameters_type import (
    RangeParametersType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RangeParameters(RangeParametersType):
    class Meta:
        name = "rangeParameters"
        namespace = "http://www.opengis.net/gml"
