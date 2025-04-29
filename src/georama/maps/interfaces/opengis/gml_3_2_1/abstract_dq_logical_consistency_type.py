from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_dq_element_type import (
    AbstractDqElementType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqLogicalConsistencyType(AbstractDqElementType):
    class Meta:
        name = "AbstractDQ_LogicalConsistency_Type"
