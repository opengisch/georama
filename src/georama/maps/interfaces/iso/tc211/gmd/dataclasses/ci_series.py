from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ci_series_type import (
    CiSeriesType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiSeries(CiSeriesType):
    class Meta:
        name = "CI_Series"
        namespace = "http://www.isotc211.org/2005/gmd"
