from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.value_list_type import ValueListType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ValueList(ValueListType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
