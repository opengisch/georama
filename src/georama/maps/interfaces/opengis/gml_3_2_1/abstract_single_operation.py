from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.sc_crs_property_type import (
    AbstractCoordinateOperationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSingleOperation(AbstractCoordinateOperationType):
    """
    Gml:AbstractSingleOperation is a single (not concatenated) coordinate
    operation.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
