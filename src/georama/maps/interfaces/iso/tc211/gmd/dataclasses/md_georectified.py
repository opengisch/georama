from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_georectified_type import (
    MdGeorectifiedType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeorectified(MdGeorectifiedType):
    class Meta:
        name = "MD_Georectified"
        namespace = "http://www.isotc211.org/2005/gmd"
