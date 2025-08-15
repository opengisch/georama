from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.value_list_type import ValueListType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ValueList(ValueListType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
