from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.replace_type import ReplaceType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Replace(ReplaceType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
