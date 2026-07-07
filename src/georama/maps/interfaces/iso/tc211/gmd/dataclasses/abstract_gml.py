from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gmltype import (
    AbstractGmltype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGml(AbstractGmltype):
    """The abstract element gml:AbstractGML is “any GML object having identity”.

    It acts as the head of an XML Schema substitution group, which may
    include any element which is a GML feature, or other object, with
    identity.  This is used as a variable in content models in GML core
    and application schemas.  It is effectively an abstract superclass
    for all GML objects.
    """

    class Meta:
        name = "AbstractGML"
        namespace = "http://www.opengis.net/gml"
