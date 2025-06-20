from dataclasses import dataclass, field
from typing import Optional

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

    :ivar meta_data_property:
    :ivar description:
    :ivar group_name:
    :ivar parameter_name:
    :ivar method_name:
    :ivar coordinate_operation_name:
    :ivar ellipsoid_name:
    :ivar meridian_name:
    :ivar datum_name:
    :ivar cs_name:
    :ivar srs_name:
    :ivar name: Multiple names may be provided.  These will often be
        distinguished by being assigned by different authorities, as
        indicated by the value of the codeSpace attribute.  In an
        instance document there will usually only be one name per
        authority.
    :ivar id:
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
    group_name: list[GroupName] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    parameter_name: list[ParameterName] = field(
        default_factory=list,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    method_name: list[MethodName] = field(
        default_factory=list,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_operation_name: list[CoordinateOperationName] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid_name: list[EllipsoidName] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    meridian_name: list[MeridianName] = field(
        default_factory=list,
        metadata={
            "name": "meridianName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    datum_name: list[DatumName] = field(
        default_factory=list,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cs_name: list[CsName] = field(
        default_factory=list,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    srs_name: list[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    name: list[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
