from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import AssociationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StrictAssociation(AssociationType):
    """
    Must carry a reference to an object or contain an object but not both.
    """

    class Meta:
        name = "_strictAssociation"
        namespace = "http://www.opengis.net/gml"
