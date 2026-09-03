from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Record:
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"

    any_element: object | None = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
