from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.expression_type import ExpressionType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Expression(ExpressionType):
    class Meta:
        name = "expression"
        namespace = "http://www.opengis.net/ogc"
