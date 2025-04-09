from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_with_authority_type import (
    CodeWithAuthorityType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AxisDirection(CodeWithAuthorityType):
    """Gml:axisDirection is the direction of this coordinate system axis (or in the
    case of Cartesian projected coordinates, the direction of this coordinate
    system axis at the origin).

    Within any set of coordinate system axes, only one of each pair of
    terms may be used. For earth-fixed CRSs, this direction is often
    approximate and intended to provide a human interpretable meaning to
    the axis. When a geodetic datum is used, the precise directions of
    the axes may therefore vary slightly from this approximate
    direction. The codeSpace attribute shall reference a source of
    information specifying the values and meanings of all the allowed
    string values for this property.
    """

    class Meta:
        name = "axisDirection"
        namespace = "http://www.opengis.net/gml"
