from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.prime_meridian_property_type import (
    PrimeMeridianPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridian2(PrimeMeridianPropertyType):
    """
    Gml:primeMeridian is an association role to the prime meridian used by this
    geodetic datum.
    """

    class Meta:
        name = "primeMeridian"
        namespace = "http://www.opengis.net/gml"
