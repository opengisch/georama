from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    ImageDatumPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageDatumRef(ImageDatumPropertyType):
    class Meta:
        name = "imageDatumRef"
        namespace = "http://www.opengis.net/gml"
