from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.title_elt_type import TitleEltType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Title3(TitleEltType):
    class Meta:
        name = "title"
        namespace = "http://www.w3.org/1999/xlink"
