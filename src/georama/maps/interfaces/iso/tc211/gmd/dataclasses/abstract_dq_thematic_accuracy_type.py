from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_dq_element_type import (
    AbstractDqElementType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqThematicAccuracyType(AbstractDqElementType):
    class Meta:
        name = "AbstractDQ_ThematicAccuracy_Type"
