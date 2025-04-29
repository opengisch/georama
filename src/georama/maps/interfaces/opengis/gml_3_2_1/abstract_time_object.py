from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_object_type import (
    AbstractTimeObjectType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimeObject(AbstractTimeObjectType):
    """
    Gml:AbstractTimeObject acts as the head of a substitution group for all
    temporal primitives and complexes.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
