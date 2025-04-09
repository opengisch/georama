from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.binary_type import BinaryType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Binary(BinaryType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
