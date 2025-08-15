from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_solid_type import (
    AbstractSolidType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidAbstract(AbstractSolidType):
    """
    The "_Solid" element is the abstract head of the substituition group for all
    (continuous) solid elements.
    """

    class Meta:
        name = "_Solid"
        namespace = "http://www.opengis.net/gml"
