from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class SectionsType:
    """Unordered list of zero or more names of requested sections in complete
    service metadata document.

    Each Section value shall contain an allowed section name as
    specified by each OWS specification. See Sections parameter
    subclause for more information.
    """

    section: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Section",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
