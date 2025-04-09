from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.sort_by_type import (
    SortByType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SortBy(SortByType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
