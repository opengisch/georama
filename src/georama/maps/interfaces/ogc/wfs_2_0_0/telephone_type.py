from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class TelephoneType:
    """
    Telephone numbers for contacting the responsible individual or organization.

    :ivar voice: Telephone number by which individuals can speak to the
        responsible organization or individual.
    :ivar facsimile: Telephone number of a facsimile machine for the
        responsible organization or individual.
    """

    voice: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Voice",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    facsimile: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Facsimile",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
