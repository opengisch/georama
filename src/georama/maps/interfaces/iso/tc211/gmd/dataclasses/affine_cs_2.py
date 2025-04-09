from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.affine_csproperty_type import (
    AffineCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AffineCs2(AffineCspropertyType):
    """
    Gml:affineCS is an association role to the affine coordinate system used by
    this CRS.
    """

    class Meta:
        name = "affineCS"
        namespace = "http://www.opengis.net/gml"
