from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Object:
    """This abstract element is the head of a substitutionGroup hierararchy which
    may contain either simpleContent or complexContent elements.

    It is used to assert the model position of "class" elements declared
    in other GML schemas.
    """

    class Meta:
        name = "_Object"
        namespace = "http://www.opengis.net/gml"
