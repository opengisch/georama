from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_operation_name import (
    CoordinateOperationName,
)
from georama.maps.interfaces.opengis.filter_1_1_0.cs_name import CsName
from georama.maps.interfaces.opengis.filter_1_1_0.datum_name import DatumName
from georama.maps.interfaces.opengis.filter_1_1_0.description import Description
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid_name import EllipsoidName
from georama.maps.interfaces.opengis.filter_1_1_0.group_name import GroupName
from georama.maps.interfaces.opengis.filter_1_1_0.meridian_name import MeridianName
from georama.maps.interfaces.opengis.filter_1_1_0.meta_data_property import (
    MetaDataProperty,
)
from georama.maps.interfaces.opengis.filter_1_1_0.method_name import MethodName
from georama.maps.interfaces.opengis.filter_1_1_0.name import Name
from georama.maps.interfaces.opengis.filter_1_1_0.parameter_name import ParameterName
from georama.maps.interfaces.opengis.filter_1_1_0.srs_name import SrsName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGmltype:
    """All complexContent GML elements are directly or indirectly derived from this
    abstract supertype to establish a hierarchy of GML types that may be
    distinguished from other XML types by their ancestry.

    Elements in this hierarchy may have an ID and are thus
    referenceable.
    """

    class Meta:
        name = "AbstractGMLType"

    meta_data_property: list[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    choice: list[
        Union[
            GroupName,
            ParameterName,
            MethodName,
            CoordinateOperationName,
            EllipsoidName,
            MeridianName,
            DatumName,
            CsName,
            SrsName,
            Name,
        ]
    ] = field(
        default_factory=list,
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
