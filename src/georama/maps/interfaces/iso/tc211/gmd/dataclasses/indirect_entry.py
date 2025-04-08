from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.indirect_entry_type import (
    IndirectEntryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IndirectEntry(IndirectEntryType):
    class Meta:
        name = "indirectEntry"
        namespace = "http://www.opengis.net/gml"
