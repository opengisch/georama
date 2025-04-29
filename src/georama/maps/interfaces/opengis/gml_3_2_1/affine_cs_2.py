from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.affine_csproperty_type import (
    AffineCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AffineCs2(AffineCspropertyType):
    """
    Gml:affineCS is an association role to the affine coordinate system used by
    this CRS.
    """

    class Meta:
        name = "affineCS"
        namespace = "http://www.opengis.net/gml/3.2"
