from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.insert_type import InsertType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Insert(InsertType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
