from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_ex_geographic_extent_type import (
    AbstractExGeographicExtentType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractExGeographicExtent(AbstractExGeographicExtentType):
    class Meta:
        name = "AbstractEX_GeographicExtent"
        namespace = "http://www.isotc211.org/2005/gmd"
