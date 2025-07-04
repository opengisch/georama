from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ServiceException:
    """
    Represents a single ServiceException element.
    """
    class Meta:
        name = "ServiceException"
        namespace = "http://www.opengis.net/ogc"

    code: Optional[str] = field(
        default=None,
        metadata={"type": "Attribute"}
    )

    locator: Optional[str] = field(
        default=None,
        metadata={"type": "Attribute"}
    )

    value: Optional[str] = field(
        default=None,
        metadata={"type": "Text"}
    )


@dataclass
class ServiceExceptionReport:
    """
    Represents the root ServiceExceptionReport element.
    """
    class Meta:
        name = "ServiceExceptionReport"
        namespace = "http://www.opengis.net/ogc"

    version: str = field(
        default="1.3.0",
        metadata={"type": "Attribute"}
    )

    service_exception: List[ServiceException] = field(
        default_factory=list,
        metadata={"name": "ServiceException", "type": "Element"}
    )