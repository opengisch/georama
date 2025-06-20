from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Category(CodeType):
    """A term representing a classification.

    It has an optional XML attribute codeSpace, whose value is a URI
    which identifies a dictionary, codelist or authority for the term.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
