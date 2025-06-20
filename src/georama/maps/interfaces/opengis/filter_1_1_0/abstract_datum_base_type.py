from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.datum_name import DatumName
from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractDatumBaseType(DefinitionType):
    """
    Basic encoding for datum objects, simplifying and restricting the
    DefinitionType as needed.

    :ivar description:
    :ivar group_name:
    :ivar parameter_name:
    :ivar method_name:
    :ivar coordinate_operation_name:
    :ivar ellipsoid_name:
    :ivar meridian_name:
    :ivar cs_name:
    :ivar srs_name:
    :ivar name: Multiple names may be provided.  These will often be
        distinguished by being assigned by different authorities, as
        indicated by the value of the codeSpace attribute.  In an
        instance document there will usually only be one name per
        authority.
    :ivar datum_name:
    """

    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    group_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    parameter_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    method_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    coordinate_operation_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ellipsoid_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    meridian_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    cs_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    srs_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    datum_name: list[DatumName] = field(
        default_factory=list,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
