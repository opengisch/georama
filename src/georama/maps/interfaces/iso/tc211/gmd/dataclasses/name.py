from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Name(CodeType):
    """The gml:name property provides a label or identifier for the object,
    commonly a descriptive name.

    An object may have several names, typically assigned by different
    authorities. gml:name uses the gml:CodeType content model.  The
    authority for a name is indicated by the value of its (optional)
    codeSpace attribute.  The name may or may not be unique, as
    determined by the rules of the organization responsible for the
    codeSpace.  In common usage there will be one name per authority, so
    a processing application may select the name from its preferred
    codeSpace.
    """

    class Meta:
        name = "name"
        namespace = "http://www.opengis.net/gml"
