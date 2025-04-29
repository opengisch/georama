from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.member_name_type import MemberNameType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MemberName(MemberNameType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
