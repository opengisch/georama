from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.dq_data_quality_type import (
    DqDataQualityType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqDataQuality(DqDataQualityType):
    class Meta:
        name = "DQ_DataQuality"
        namespace = "http://www.isotc211.org/2005/gmd"
