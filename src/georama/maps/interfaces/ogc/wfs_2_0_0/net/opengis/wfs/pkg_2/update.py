from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.update_type import UpdateType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Update(UpdateType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
