from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.indirect_entry_type import (
    IndirectEntryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IndirectEntry(IndirectEntryType):
    class Meta:
        name = "indirectEntry"
        namespace = "http://www.opengis.net/gml"
