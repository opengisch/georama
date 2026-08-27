from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_indeterminate_value_type import (
    TimeIndeterminateValueType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimePositionType:
    """The method for identifying a temporal position is specific to each temporal
    reference system.

    gml:TimePositionType supports the description of temporal position
    according to the subtypes described in ISO 19108. Values based on
    calendars and clocks use lexical formats that are based on ISO 8601,
    as described in XML Schema Part 2:2001. A decimal value may be used
    with coordinate systems such as GPS time or UNIX time. A URI may be
    used to provide a reference to some era in an ordinal reference
    system . In common with many of the components modelled as data
    types in the ISO 19100 series of International Standards, the
    corresponding GML component has simple content. However, the content
    model gml:TimePositionType is defined in several steps. Three XML
    attributes appear on gml:TimePositionType: A time value shall be
    associated with a temporal reference system through the frame
    attribute that provides a URI reference that identifies a
    description of the reference system. Following ISO 19108, the
    Gregorian calendar with UTC is the default reference system, but
    others may also be used. Components for describing temporal
    reference systems are described in 14.4, but it is not required that
    the reference system be described in this, as the reference may
    refer to anything that may be indentified with a URI. For time
    values using a calendar containing more than one era, the (optional)
    calendarEraName attribute provides the name of the calendar era.
    Inexact temporal positions may be expressed using the optional
    indeterminatePosition attribute.  This takes a value from an
    enumeration.
    """

    value: XmlDate | XmlPeriod | XmlTime | XmlDateTime | str | Decimal = field(
        default=""
    )
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        },
    )
    calendar_era_name: str | None = field(
        default=None,
        metadata={
            "name": "calendarEraName",
            "type": "Attribute",
        },
    )
    indeterminate_position: TimeIndeterminateValueType | None = field(
        default=None,
        metadata={
            "name": "indeterminatePosition",
            "type": "Attribute",
        },
    )
