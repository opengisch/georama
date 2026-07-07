from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_conformance_result_type import (
    DqConformanceResultType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqConformanceResult(DqConformanceResultType):
    class Meta:
        name = "DQ_ConformanceResult"
        namespace = "http://www.isotc211.org/2005/gmd"
