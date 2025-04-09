from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.prime_meridian_type import (
    PrimeMeridianType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridian1(PrimeMeridianType):
    """A gml:PrimeMeridian defines the origin from which longitude values are
    determined.

    The default value for the prime meridian gml:identifier value is
    "Greenwich".
    """

    class Meta:
        name = "PrimeMeridian"
        namespace = "http://www.opengis.net/gml"
