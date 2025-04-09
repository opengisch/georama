from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.domain_set_type import (
    DomainSetType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DomainSet(DomainSetType):
    """The gml:domainSet property element describes the spatio-temporal region of
    interest, within which the coverage is defined.

    Its content model is given by gml:DomainSetType. The value of the
    domain is thus a choice between a gml:AbstractGeometry and a
    gml:AbstractTimeObject.  In the instance these abstract elements
    will normally be substituted by a geometry complex or temporal
    complex, to represent spatial coverages and time-series,
    respectively. The presence of the gml:AssociationAttributeGroup
    means that domainSet follows the usual GML property model and may
    use the xlink:href attribute to point to the domain, as an
    alternative to describing the domain inline. Ownership semantics may
    be provided using the gml:OwnershipAttributeGroup.
    """

    class Meta:
        name = "domainSet"
        namespace = "http://www.opengis.net/gml"
