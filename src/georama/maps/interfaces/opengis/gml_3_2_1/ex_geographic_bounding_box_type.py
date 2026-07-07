from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_ex_geographic_extent_type import (
    AbstractExGeographicExtentType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.decimal_property_type import (
    DecimalPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExGeographicBoundingBoxType(AbstractExGeographicExtentType):
    """
    Geographic area of the entire dataset referenced to WGS 84.
    """

    class Meta:
        name = "EX_GeographicBoundingBox_Type"

    west_bound_longitude: Optional[DecimalPropertyType] = field(
        default=None,
        metadata={
            "name": "westBoundLongitude",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    east_bound_longitude: Optional[DecimalPropertyType] = field(
        default=None,
        metadata={
            "name": "eastBoundLongitude",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    south_bound_latitude: Optional[DecimalPropertyType] = field(
        default=None,
        metadata={
            "name": "southBoundLatitude",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    north_bound_latitude: Optional[DecimalPropertyType] = field(
        default=None,
        metadata={
            "name": "northBoundLatitude",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
