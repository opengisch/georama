from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_dq_completeness_type import (
    AbstractDqCompletenessType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqCompleteness(AbstractDqCompletenessType):
    class Meta:
        name = "AbstractDQ_Completeness"
        namespace = "http://www.isotc211.org/2005/gmd"
