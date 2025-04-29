from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractObject1:
    """This element has no type defined, and is therefore implicitly (according to
    the rules of W3C XML Schema) an XML Schema anyType.

    It is used as the head of an XML Schema substitution group which
    unifies complex content and certain simple content elements used for
    datatypes in GML, including the gml:AbstractGML substitution group.
    """

    class Meta:
        name = "AbstractObject"
        namespace = "http://www.opengis.net/gml/3.2"
