from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MethodFormula(CodeType):
    """Formula(s) used by this operation method.

    The value may be a reference to a publication. Note that the
    operation method may not be analytic, in which case this element
    references or contains the procedure, not an analytic formula.
    """

    class Meta:
        name = "methodFormula"
        namespace = "http://www.opengis.net/gml"
