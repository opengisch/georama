from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Name(CodeType):
    """Label for the object, normally a descriptive name.

    An object may have several names, typically assigned by different
    authorities.  The authority for a name is indicated by the value of
    its (optional) codeSpace attribute.  The name may or may not be
    unique, as determined by the rules of the organization responsible
    for the codeSpace.
    """

    class Meta:
        name = "name"
        namespace = "http://www.opengis.net/gml"
