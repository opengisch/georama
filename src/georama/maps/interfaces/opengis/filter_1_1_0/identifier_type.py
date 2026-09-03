from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_operation_name import (
    CoordinateOperationName,
)
from georama.maps.interfaces.opengis.filter_1_1_0.cs_name import CsName
from georama.maps.interfaces.opengis.filter_1_1_0.datum_name import DatumName
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid_name import EllipsoidName
from georama.maps.interfaces.opengis.filter_1_1_0.group_name import GroupName
from georama.maps.interfaces.opengis.filter_1_1_0.meridian_name import MeridianName
from georama.maps.interfaces.opengis.filter_1_1_0.method_name import MethodName
from georama.maps.interfaces.opengis.filter_1_1_0.name import Name
from georama.maps.interfaces.opengis.filter_1_1_0.parameter_name import ParameterName
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks
from georama.maps.interfaces.opengis.filter_1_1_0.srs_name import SrsName
from georama.maps.interfaces.opengis.filter_1_1_0.version import Version

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IdentifierType:
    """An identification of a CRS object.

    The first use of the IdentifierType for an object, if any, is
    normally the primary identification code, and any others are
    aliases.

    :ivar choice:
    :ivar version:
    :ivar remarks: Remarks about this code or alias.
    """

    choice: (
        GroupName
        | ParameterName
        | MethodName
        | CoordinateOperationName
        | EllipsoidName
        | MeridianName
        | DatumName
        | CsName
        | SrsName
        | Name
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "groupName",
                    "type": GroupName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "parameterName",
                    "type": ParameterName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "methodName",
                    "type": MethodName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "coordinateOperationName",
                    "type": CoordinateOperationName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ellipsoidName",
                    "type": EllipsoidName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "meridianName",
                    "type": MeridianName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "datumName",
                    "type": DatumName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "csName",
                    "type": CsName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "srsName",
                    "type": SrsName,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "name",
                    "type": Name,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    version: Version | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    remarks: Remarks | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
