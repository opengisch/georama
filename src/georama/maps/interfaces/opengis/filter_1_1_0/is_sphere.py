from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.is_sphere_value import IsSphereValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IsSphere:
    """The ellipsoid is degenerate and is actually a sphere.

    The sphere is completely defined by the semi-major axis, which is
    the radius of the sphere.
    """

    class Meta:
        name = "isSphere"
        namespace = "http://www.opengis.net/gml"

    value: IsSphereValue | None = field(default=None)
