from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_format_consistency_type import (
    DqFormatConsistencyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqFormatConsistency(DqFormatConsistencyType):
    class Meta:
        name = "DQ_FormatConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
