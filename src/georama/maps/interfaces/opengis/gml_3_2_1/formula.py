from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Formula(CodeType):
    """Gml:formula Formula(s) or procedure used by an operation method.

    The use of the codespace attribite has been deprecated. The property
    value shall be a character string.
    """

    class Meta:
        name = "formula"
        namespace = "http://www.opengis.net/gml/3.2"
