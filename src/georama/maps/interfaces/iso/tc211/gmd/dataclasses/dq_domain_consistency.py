from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_domain_consistency_type import (
    DqDomainConsistencyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqDomainConsistency(DqDomainConsistencyType):
    class Meta:
        name = "DQ_DomainConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
