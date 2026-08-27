from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.dcp import Dcp
from georama.maps.interfaces.ogc.wfs_2_0_0.domain_type import DomainType
from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Operation:
    """
    Metadata for one operation that this server implements.

    :ivar dcp: Unordered list of Distributed Computing Platforms (DCPs)
        supported for this operation. At present, only the HTTP DCP is
        defined, so this element will appear only once.
    :ivar parameter: Optional unordered list of parameter domains that
        each apply to this operation which this server implements. If
        one of these Parameter elements has the same "name" attribute as
        a Parameter element in the OperationsMetadata element, this
        Parameter element shall override the other one for this
        operation. The list of required and optional parameter domain
        limitations for this operation shall be specified in the
        Implementation Specification for this service.
    :ivar constraint: Optional unordered list of valid domain
        constraints on non-parameter quantities that each apply to this
        operation. If one of these Constraint elements has the same
        "name" attribute as a Constraint element in the
        OperationsMetadata element, this Constraint element shall
        override the other one for this operation. The list of required
        and optional constraints for this operation shall be specified
        in the Implementation Specification for this service.
    :ivar metadata: Optional unordered list of additional metadata about
        this operation and its' implementation. A list of required and
        optional metadata elements for this operation should be
        specified in the Implementation Specification for this service.
        (Informative: This metadata might specify the operation request
        parameters or provide the XML Schemas for the operation
        request.)
    :ivar name: Name or identifier of this operation (request) (for
        example, GetCapabilities). The list of required and optional
        operations implemented shall be specified in the Implementation
        Specification for this service.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    dcp: list[Dcp] = field(
        default_factory=list,
        metadata={
            "name": "DCP",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    parameter: list[DomainType] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
        },
    )
    constraint: list[DomainType] = field(
        default_factory=list,
        metadata={
            "name": "Constraint",
            "type": "Element",
        },
    )
    metadata: list[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
