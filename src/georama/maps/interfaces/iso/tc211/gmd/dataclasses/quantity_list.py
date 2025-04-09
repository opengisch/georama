from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.measure_or_nil_reason_list_type import (
    MeasureOrNilReasonListType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityList(MeasureOrNilReasonListType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
