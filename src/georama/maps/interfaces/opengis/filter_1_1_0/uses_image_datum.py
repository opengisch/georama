from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.image_datum_ref_type import (
    ImageDatumRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesImageDatum(ImageDatumRefType):
    """
    Association to the image datum used by this CRS.
    """

    class Meta:
        name = "usesImageDatum"
        namespace = "http://www.opengis.net/gml"
