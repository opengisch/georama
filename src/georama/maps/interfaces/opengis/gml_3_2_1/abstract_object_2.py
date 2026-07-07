from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class AbstractObject2(AbstractObjectType):
    class Meta:
        name = "AbstractObject"
        namespace = "http://www.isotc211.org/2005/gco"
