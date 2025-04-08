from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gmltype import (
    AbstractGmltype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeObjectType(AbstractGmltype):
    pass
