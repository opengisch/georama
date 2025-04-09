from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.history_property_type import (
    HistoryPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Track(HistoryPropertyType):
    class Meta:
        name = "track"
        namespace = "http://www.opengis.net/gml"
