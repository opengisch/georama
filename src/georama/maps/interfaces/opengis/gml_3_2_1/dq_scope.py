from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.dq_scope_type import DqScopeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqScope(DqScopeType):
    class Meta:
        name = "DQ_Scope"
        namespace = "http://www.isotc211.org/2005/gmd"
