from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_data_quality_type import (
    DqDataQualityType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqDataQuality(DqDataQualityType):
    class Meta:
        name = "DQ_DataQuality"
        namespace = "http://www.isotc211.org/2005/gmd"
