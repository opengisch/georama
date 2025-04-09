from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gmltype import (
    AbstractGmltype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTopologyType(AbstractGmltype):
    """This abstract type supplies the root or base type for all topological
    elements including primitives and complexes.

    It inherits AbstractGMLType and hence can be identified using the
    gml:id attribute.
    """
