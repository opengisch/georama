from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_metadata_type import (
    AbstractDsAggregateType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDsAggregate(AbstractDsAggregateType):
    class Meta:
        name = "AbstractDS_Aggregate"
        namespace = "http://www.isotc211.org/2005/gmd"
