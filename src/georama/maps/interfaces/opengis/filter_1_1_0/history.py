from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.history_property_type import (
    HistoryPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class History(HistoryPropertyType):
    class Meta:
        name = "history"
        namespace = "http://www.opengis.net/gml"
