from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.gml_object_id_type import (
    GmlObjectIdType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class GmlObjectId(GmlObjectIdType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
