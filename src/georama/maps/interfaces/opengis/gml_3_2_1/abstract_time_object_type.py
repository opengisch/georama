from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_gmltype import AbstractGmltype

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimeObjectType(AbstractGmltype):
    pass
