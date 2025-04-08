from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.quantity_extent_type import (
    QuantityExtentType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityExtent(QuantityExtentType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
