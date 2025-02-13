from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.insert_type import InsertType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Insert(InsertType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
