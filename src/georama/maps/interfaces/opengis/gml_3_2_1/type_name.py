from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.type_name_type import TypeNameType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class TypeName(TypeNameType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
