from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.dq_completeness_commission_type import (
    DqCompletenessCommissionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqCompletenessCommission(DqCompletenessCommissionType):
    class Meta:
        name = "DQ_CompletenessCommission"
        namespace = "http://www.isotc211.org/2005/gmd"
