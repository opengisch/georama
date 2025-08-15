from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.image_datum_type import ImageDatumType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageDatum(ImageDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
