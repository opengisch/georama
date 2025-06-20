from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.sort_by_type import SortByType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SortBy(SortByType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
