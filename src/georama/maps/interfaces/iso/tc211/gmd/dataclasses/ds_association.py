from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ds_association_type import (
    DsAssociationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsAssociation(DsAssociationType):
    class Meta:
        name = "DS_Association"
        namespace = "http://www.isotc211.org/2005/gmd"
