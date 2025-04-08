from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.mapping_rule_type import (
    MappingRuleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoverageMappingRule(MappingRuleType):
    """Gml:CoverageMappingRule provides a formal or informal description of the
    coverage function.

    The mapping rule may be defined as an in-line string
    (gml:ruleDefinition) or via a remote reference through xlink:href
    (gml:ruleReference). If no rule name is specified, the default is
    ‘Linear’ with respect to members of the domain in document order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
