from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.delete_type import DeleteType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Delete(DeleteType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
