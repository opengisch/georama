from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.li_lineage_type import (
    LiLineageType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiLineage(LiLineageType):
    class Meta:
        name = "LI_Lineage"
        namespace = "http://www.isotc211.org/2005/gmd"
