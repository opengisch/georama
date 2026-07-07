from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_datum_type import (
    AbstractDatumType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.pixel_in_cell import PixelInCell

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageDatumType(AbstractDatumType):
    """An image datum defines the origin of an image coordinate reference system,
    and is used in a local context only.

    For more information, see OGC Abstract Specification Topic 2.
    """

    pixel_in_cell: Optional[PixelInCell] = field(
        default=None,
        metadata={
            "name": "pixelInCell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
