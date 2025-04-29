from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.title_elt_type import TitleEltType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Title(TitleEltType):
    class Meta:
        name = "title"
        namespace = "http://www.w3.org/1999/xlink"
