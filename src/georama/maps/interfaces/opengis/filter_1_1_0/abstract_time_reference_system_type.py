from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeReferenceSystemType(DefinitionType):
    """A value in the time domain is measured relative to a temporal reference
    system.

    Common types of reference systems include calendars, ordinal
    temporal reference systems, and temporal coordinate systems (time
    elapsed since some epoch, e.g. UNIX time).
    """

    domain_of_validity: Optional[str] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
