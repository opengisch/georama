from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.filter_type import FilterType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Filter(FilterType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
