from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_crstype import (
    ImageDatumPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageDatumRef(ImageDatumPropertyType):
    class Meta:
        name = "imageDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"
