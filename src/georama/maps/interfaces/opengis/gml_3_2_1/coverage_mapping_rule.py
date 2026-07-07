from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.mapping_rule_type import MappingRuleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoverageMappingRule(MappingRuleType):
    """Gml:CoverageMappingRule provides a formal or informal description of the
    coverage function.

    The mapping rule may be defined as an in-line string
    (gml:ruleDefinition) or via a remote reference through xlink:href
    (gml:ruleReference). If no rule name is specified, the default is
    'Linear' with respect to members of the domain in document order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
