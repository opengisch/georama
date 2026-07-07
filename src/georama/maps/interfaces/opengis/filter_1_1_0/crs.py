from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_type import (
    AbstractReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Crs(AbstractReferenceSystemType):
    """Abstract coordinate reference system, usually defined by a coordinate system
    and a datum.

    This abstract complexType shall not be used, extended, or
    restricted, in an Application Schema, to define a concrete subtype
    with a meaning equivalent to a concrete subtype specified in this
    document.
    """

    class Meta:
        name = "_CRS"
        namespace = "http://www.opengis.net/gml"
