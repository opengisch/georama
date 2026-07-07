from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_usage_type import MdUsageType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdUsage(MdUsageType):
    class Meta:
        name = "MD_Usage"
        namespace = "http://www.isotc211.org/2005/gmd"
