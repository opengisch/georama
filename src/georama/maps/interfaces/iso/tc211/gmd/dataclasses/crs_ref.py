from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    CrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CrsRef(CrspropertyType):
    """Gml:crsRef is an association role either referencing or containing the
    definition of a CRS.

    This property element has been deprecated.
    """

    class Meta:
        name = "crsRef"
        namespace = "http://www.opengis.net/gml"
