from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_solid_type import (
    AbstractSolidType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSolid(AbstractSolidType):
    """
    The AbstractSolid element is the abstract head of the substituition group for
    all (continuous) solid elements.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
