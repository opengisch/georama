from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdSpatialRepresentationType(AbstractObjectType):
    """
    Digital mechanism used to represent spatial information.
    """

    class Meta:
        name = "AbstractMD_SpatialRepresentation_Type"
