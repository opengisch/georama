from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_gridded_data_positional_accuracy_type import (
    DqGriddedDataPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqGriddedDataPositionalAccuracy(DqGriddedDataPositionalAccuracyType):
    class Meta:
        name = "DQ_GriddedDataPositionalAccuracy"
        namespace = "http://www.isotc211.org/2005/gmd"
