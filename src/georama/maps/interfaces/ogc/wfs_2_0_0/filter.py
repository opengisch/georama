from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.filter_type import FilterType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Filter(FilterType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
