from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractSelectionClause:
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"

    any_element: object | None = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
