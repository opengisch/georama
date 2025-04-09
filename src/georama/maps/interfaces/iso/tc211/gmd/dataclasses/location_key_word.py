from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LocationKeyWord(CodeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
