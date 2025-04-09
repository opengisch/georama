from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Formula(CodeType):
    """Gml:formula specifies a formula or procedure used by this operation method.

    The value may be a reference to a publication. Note that the
    operation method may not be analytic, in which case this element
    references or contains the procedure, not an analytic formula.
    """

    class Meta:
        name = "formula"
        namespace = "http://www.opengis.net/gml"
