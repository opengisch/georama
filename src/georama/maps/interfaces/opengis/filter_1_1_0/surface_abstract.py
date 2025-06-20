from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_surface_type import (
    AbstractSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceAbstract(AbstractSurfaceType):
    """
    The "_Surface" element is the abstract head of the substituition group for all
    (continuous) surface elements.
    """

    class Meta:
        name = "_Surface"
        namespace = "http://www.opengis.net/gml"
