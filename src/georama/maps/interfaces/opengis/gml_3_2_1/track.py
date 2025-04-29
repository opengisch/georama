from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.history_property_type import (
    HistoryPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Track(HistoryPropertyType):
    class Meta:
        name = "track"
        namespace = "http://www.opengis.net/gml/3.2"
