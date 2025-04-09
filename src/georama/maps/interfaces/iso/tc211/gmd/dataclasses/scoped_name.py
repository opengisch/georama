from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class ScopedName(CodeType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
