from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.get_property_value_type import GetPropertyValueType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetPropertyValue(GetPropertyValueType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
