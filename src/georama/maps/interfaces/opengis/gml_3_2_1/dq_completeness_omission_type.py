from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_dq_completeness_type import (
    AbstractDqCompletenessType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqCompletenessOmissionType(AbstractDqCompletenessType):
    class Meta:
        name = "DQ_CompletenessOmission_Type"
