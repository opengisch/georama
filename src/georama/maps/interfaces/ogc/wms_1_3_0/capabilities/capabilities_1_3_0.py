from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/wms"


@dataclass
class Abstract:
    """
    The abstract is a longer narrative description of an object.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AccessConstraints:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Address:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AddressType:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class BoundingBox:
    """
    The BoundingBox attributes indicate the limits of the bounding box in units of
    the specified coordinate reference system.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    crs: Optional[str] = field(
        default=None,
        metadata={
            "name": "CRS",
            "type": "Attribute",
            "required": True,
        },
    )
    minx: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    miny: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    maxx: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    maxy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    resx: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    resy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Crs:
    """
    Identifier for a single Coordinate Reference System (CRS).
    """

    class Meta:
        name = "CRS"
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class City:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ContactElectronicMailAddress:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ContactFacsimileTelephone:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ContactOrganization:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ContactPerson:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ContactPosition:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ContactVoiceTelephone:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Country:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Dimension:
    """
    The Dimension element declares the existence of a dimension and indicates what
    values along a dimension are valid.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    unit_symbol: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitSymbol",
            "type": "Attribute",
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    multiple_values: Optional[bool] = field(
        default=None,
        metadata={
            "name": "multipleValues",
            "type": "Attribute",
        },
    )
    nearest_value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "nearestValue",
            "type": "Attribute",
        },
    )
    current: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ExGeographicBoundingBox:
    """
    The EX_GeographicBoundingBox attributes indicate the limits of the enclosing
    rectangle in longitude and latitude decimal degrees.
    """

    class Meta:
        name = "EX_GeographicBoundingBox"
        namespace = "http://www.opengis.net/wms"

    west_bound_longitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "westBoundLongitude",
            "type": "Element",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        },
    )
    east_bound_longitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "eastBoundLongitude",
            "type": "Element",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        },
    )
    south_bound_latitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "southBoundLatitude",
            "type": "Element",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        },
    )
    north_bound_latitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "northBoundLatitude",
            "type": "Element",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        },
    )


@dataclass
class Fees:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Format:
    """
    A container for listing an available format's MIME type.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Identifier:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Keyword:
    """
    A single keyword or phrase.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    vocabulary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LayerLimit:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MaxHeight:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MaxScaleDenominator:
    """
    Maximum scale denominator for which it is appropriate to display this layer.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MaxWidth:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MinScaleDenominator:
    """
    Minimum scale denominator for which it is appropriate to display this layer.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Name:
    """
    The Name is typically for machine-to-machine communication.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class PostCode:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class ServiceName(Enum):
    WMS = "WMS"


@dataclass
class StateOrProvince:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Title:
    """
    The Title is for informative display to a human.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ExtendedCapabilities:
    """
    Individual service providers may use this element to report extended
    capabilities.
    """

    class Meta:
        name = "_ExtendedCapabilities"
        namespace = "http://www.opengis.net/wms"


@dataclass
class ContactAddress:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    address_type: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "AddressType",
            "type": "Element",
            "required": True,
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "required": True,
        },
    )
    city: Optional[City] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "required": True,
        },
    )
    state_or_province: Optional[StateOrProvince] = field(
        default=None,
        metadata={
            "name": "StateOrProvince",
            "type": "Element",
            "required": True,
        },
    )
    post_code: Optional[PostCode] = field(
        default=None,
        metadata={
            "name": "PostCode",
            "type": "Element",
            "required": True,
        },
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ContactPersonPrimary:
    class Meta:
        namespace = "http://www.opengis.net/wms"

    contact_person: Optional[ContactPerson] = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "required": True,
        },
    )
    contact_organization: Optional[ContactOrganization] = field(
        default=None,
        metadata={
            "name": "ContactOrganization",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Exception:
    """
    An Exception element indicates which error-reporting formats are supported.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    format: List[Format] = field(
        default_factory=list,
        metadata={
            "name": "Format",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class KeywordList:
    """
    List of keywords or keyword phrases to help catalog searching.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    keyword: List[Keyword] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
        },
    )


@dataclass
class OnlineResource:
    """An OnlineResource is typically an HTTP URL.

    The URL is placed in the xlink:href attribute, and the value
    "simple" is placed in the xlink:type attribute.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )


@dataclass
class AuthorityUrl:
    """A Map Server may use zero or more Identifier elements to list ID numbers or
    labels defined by a particular Authority.

    For example, the Global Change Master Directory (gcmd.gsfc.nasa.gov)
    defines a DIF_ID label for every dataset.  The authority name and
    explanatory URL are defined in a separate AuthorityURL element,
    which may be defined once and inherited by subsidiary layers.
    Identifiers themselves are not inherited.
    """

    class Meta:
        name = "AuthorityURL"
        namespace = "http://www.opengis.net/wms"

    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ContactInformation:
    """
    Information about a contact person for the service.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    contact_person_primary: Optional[ContactPersonPrimary] = field(
        default=None,
        metadata={
            "name": "ContactPersonPrimary",
            "type": "Element",
        },
    )
    contact_position: Optional[ContactPosition] = field(
        default=None,
        metadata={
            "name": "ContactPosition",
            "type": "Element",
        },
    )
    contact_address: Optional[ContactAddress] = field(
        default=None,
        metadata={
            "name": "ContactAddress",
            "type": "Element",
        },
    )
    contact_voice_telephone: Optional[ContactVoiceTelephone] = field(
        default=None,
        metadata={
            "name": "ContactVoiceTelephone",
            "type": "Element",
        },
    )
    contact_facsimile_telephone: Optional[ContactFacsimileTelephone] = field(
        default=None,
        metadata={
            "name": "ContactFacsimileTelephone",
            "type": "Element",
        },
    )
    contact_electronic_mail_address: Optional[ContactElectronicMailAddress] = field(
        default=None,
        metadata={
            "name": "ContactElectronicMailAddress",
            "type": "Element",
        },
    )


@dataclass
class DataUrl:
    """
    A Map Server may use DataURL offer a link to the underlying data represented by
    a particular layer.
    """

    class Meta:
        name = "DataURL"
        namespace = "http://www.opengis.net/wms"

    format: Optional[Format] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "required": True,
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FeatureListUrl:
    """
    A Map Server may use FeatureListURL to point to a list of the features
    represented in a Layer.
    """

    class Meta:
        name = "FeatureListURL"
        namespace = "http://www.opengis.net/wms"

    format: Optional[Format] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "required": True,
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Get:
    """
    The URL prefix for the HTTP "Get" request method.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LegendUrl:
    """A Map Server may use zero or more LegendURL elements to provide an image(s)
    of a legend relevant to each Style of a Layer.

    The Format element indicates the MIME type of the legend. Width and
    height attributes may be provided to assist client applications in
    laying out space to display the legend.
    """

    class Meta:
        name = "LegendURL"
        namespace = "http://www.opengis.net/wms"

    format: Optional[Format] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "required": True,
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LogoUrl:
    class Meta:
        name = "LogoURL"
        namespace = "http://www.opengis.net/wms"

    format: Optional[Format] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "required": True,
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MetadataUrl:
    """A Map Server may use zero or more MetadataURL elements to offer detailed,
    standardized metadata about the data underneath a particular layer.

    The type attribute indicates the standard to which the metadata
    complies.  The format element indicates how the metadata is
    structured.
    """

    class Meta:
        name = "MetadataURL"
        namespace = "http://www.opengis.net/wms"

    format: Optional[Format] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "required": True,
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Post:
    """
    The URL prefix for the HTTP "Post" request method.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StyleSheetUrl:
    """
    StyleSheeetURL provides symbology information for each Style of a Layer.
    """

    class Meta:
        name = "StyleSheetURL"
        namespace = "http://www.opengis.net/wms"

    format: Optional[Format] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "required": True,
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StyleUrl:
    """A Map Server may use StyleURL to offer more information about the data or
    symbology underlying a particular Style.

    While the semantics are not well-defined, as long as the results of
    an HTTP GET request against the StyleURL are properly MIME-typed,
    Viewer Clients and Cascading Map Servers can make use of this. A
    possible use could be to allow a Map Server to provide legend
    information.
    """

    class Meta:
        name = "StyleURL"
        namespace = "http://www.opengis.net/wms"

    format: Optional[Format] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "required": True,
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Attribution:
    """Attribution indicates the provider of a Layer or collection of Layers.

    The provider's URL, descriptive title string, and/or logo image URL
    may be supplied.  Client applications may choose to display one or
    more of these items.  A format element indicates the MIME type of
    the logo image located at LogoURL.  The logo image's width and
    height assist client applications in laying out space to display the
    logo.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
        },
    )
    logo_url: Optional[LogoUrl] = field(
        default=None,
        metadata={
            "name": "LogoURL",
            "type": "Element",
        },
    )


@dataclass
class Http:
    """Available HTTP request methods.

    At least "Get" shall be supported.
    """

    class Meta:
        name = "HTTP"
        namespace = "http://www.opengis.net/wms"

    get: Optional[Get] = field(
        default=None,
        metadata={
            "name": "Get",
            "type": "Element",
            "required": True,
        },
    )
    post: Optional[Post] = field(
        default=None,
        metadata={
            "name": "Post",
            "type": "Element",
        },
    )


@dataclass
class Service:
    """
    General service metadata.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    name: Optional[ServiceName] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[Abstract] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        },
    )
    keyword_list: Optional[KeywordList] = field(
        default=None,
        metadata={
            "name": "KeywordList",
            "type": "Element",
        },
    )
    online_resource: Optional[OnlineResource] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "required": True,
        },
    )
    contact_information: Optional[ContactInformation] = field(
        default=None,
        metadata={
            "name": "ContactInformation",
            "type": "Element",
        },
    )
    fees: Optional[Fees] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Element",
        },
    )
    access_constraints: Optional[AccessConstraints] = field(
        default=None,
        metadata={
            "name": "AccessConstraints",
            "type": "Element",
        },
    )
    layer_limit: Optional[LayerLimit] = field(
        default=None,
        metadata={
            "name": "LayerLimit",
            "type": "Element",
        },
    )
    max_width: Optional[MaxWidth] = field(
        default=None,
        metadata={
            "name": "MaxWidth",
            "type": "Element",
        },
    )
    max_height: Optional[MaxHeight] = field(
        default=None,
        metadata={
            "name": "MaxHeight",
            "type": "Element",
        },
    )


@dataclass
class Style:
    """
    A Style element lists the name by which a style is requested and a human-
    readable title for pick lists, optionally (and ideally) provides a human-
    readable description, and optionally gives a style URL.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[Abstract] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        },
    )
    legend_url: List[LegendUrl] = field(
        default_factory=list,
        metadata={
            "name": "LegendURL",
            "type": "Element",
        },
    )
    style_sheet_url: Optional[StyleSheetUrl] = field(
        default=None,
        metadata={
            "name": "StyleSheetURL",
            "type": "Element",
        },
    )
    style_url: Optional[StyleUrl] = field(
        default=None,
        metadata={
            "name": "StyleURL",
            "type": "Element",
        },
    )


@dataclass
class Dcptype:
    """Available Distributed Computing Platforms (DCPs) are listed here.

    At present, only HTTP is defined.
    """

    class Meta:
        name = "DCPType"
        namespace = "http://www.opengis.net/wms"

    http: Optional[Http] = field(
        default=None,
        metadata={
            "name": "HTTP",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Layer:
    """
    Nested list of zero or more map Layers offered by this server.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        },
    )
    abstract: Optional[Abstract] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        },
    )
    keyword_list: Optional[KeywordList] = field(
        default=None,
        metadata={
            "name": "KeywordList",
            "type": "Element",
        },
    )
    crs: List[Crs] = field(
        default_factory=list,
        metadata={
            "name": "CRS",
            "type": "Element",
        },
    )
    ex_geographic_bounding_box: Optional[ExGeographicBoundingBox] = field(
        default=None,
        metadata={
            "name": "EX_GeographicBoundingBox",
            "type": "Element",
        },
    )
    bounding_box: List[BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
        },
    )
    dimension: List[Dimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
        },
    )
    attribution: Optional[Attribution] = field(
        default=None,
        metadata={
            "name": "Attribution",
            "type": "Element",
        },
    )
    authority_url: List[AuthorityUrl] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityURL",
            "type": "Element",
        },
    )
    identifier: List[Identifier] = field(
        default_factory=list,
        metadata={
            "name": "Identifier",
            "type": "Element",
        },
    )
    metadata_url: List[MetadataUrl] = field(
        default_factory=list,
        metadata={
            "name": "MetadataURL",
            "type": "Element",
        },
    )
    data_url: List[DataUrl] = field(
        default_factory=list,
        metadata={
            "name": "DataURL",
            "type": "Element",
        },
    )
    feature_list_url: List[FeatureListUrl] = field(
        default_factory=list,
        metadata={
            "name": "FeatureListURL",
            "type": "Element",
        },
    )
    style: List[Style] = field(
        default_factory=list,
        metadata={
            "name": "Style",
            "type": "Element",
        },
    )
    min_scale_denominator: Optional[MinScaleDenominator] = field(
        default=None,
        metadata={
            "name": "MinScaleDenominator",
            "type": "Element",
        },
    )
    max_scale_denominator: Optional[MaxScaleDenominator] = field(
        default=None,
        metadata={
            "name": "MaxScaleDenominator",
            "type": "Element",
        },
    )
    layer: List["Layer"] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
        },
    )
    queryable: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    cascaded: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    opaque: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    no_subsets: bool = field(
        default=False,
        metadata={
            "name": "noSubsets",
            "type": "Attribute",
        },
    )
    fixed_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "fixedWidth",
            "type": "Attribute",
        },
    )
    fixed_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "fixedHeight",
            "type": "Attribute",
        },
    )


@dataclass
class OperationType:
    """
    For each operation offered by the server, list the available output formats and
    the online resource.
    """

    format: List[Format] = field(
        default_factory=list,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.opengis.net/wms",
            "min_occurs": 1,
        },
    )
    dcptype: List[Dcptype] = field(
        default_factory=list,
        metadata={
            "name": "DCPType",
            "type": "Element",
            "namespace": "http://www.opengis.net/wms",
            "min_occurs": 1,
        },
    )


@dataclass
class GetCapabilities(OperationType):
    class Meta:
        namespace = "http://www.opengis.net/wms"


@dataclass
class GetFeatureInfo(OperationType):
    class Meta:
        namespace = "http://www.opengis.net/wms"


@dataclass
class GetMap(OperationType):
    class Meta:
        namespace = "http://www.opengis.net/wms"


@dataclass
class ExtendedOperation(OperationType):
    class Meta:
        name = "_ExtendedOperation"
        namespace = "http://www.opengis.net/wms"


@dataclass
class Request:
    """
    Available WMS Operations are listed in a Request element.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    get_capabilities: Optional[GetCapabilities] = field(
        default=None,
        metadata={
            "name": "GetCapabilities",
            "type": "Element",
            "required": True,
        },
    )
    get_map: Optional[GetMap] = field(
        default=None,
        metadata={
            "name": "GetMap",
            "type": "Element",
            "required": True,
        },
    )
    get_feature_info: Optional[GetFeatureInfo] = field(
        default=None,
        metadata={
            "name": "GetFeatureInfo",
            "type": "Element",
        },
    )


@dataclass
class Capability:
    """A Capability lists available request types, how exceptions may be reported,
    and whether any extended capabilities are defined.

    It also includes an optional list of map layers available from this
    server.
    """

    class Meta:
        namespace = "http://www.opengis.net/wms"

    request: Optional[Request] = field(
        default=None,
        metadata={
            "name": "Request",
            "type": "Element",
            "required": True,
        },
    )
    exception: Optional[Exception] = field(
        default=None,
        metadata={
            "name": "Exception",
            "type": "Element",
            "required": True,
        },
    )
    layer: Optional[Layer] = field(
        default=None,
        metadata={
            "name": "Layer",
            "type": "Element",
        },
    )


@dataclass
class WmsCapabilities:
    """
    A WMS_Capabilities document is returned in response to a GetCapabilities
    request made on a WMS.
    """

    class Meta:
        name = "WMS_Capabilities"
        namespace = "http://www.opengis.net/wms"

    service: Optional[Service] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "required": True,
        },
    )
    capability: Optional[Capability] = field(
        default=None,
        metadata={
            "name": "Capability",
            "type": "Element",
            "required": True,
        },
    )
    version: str = field(
        init=False,
        default="1.3.0",
        metadata={
            "type": "Attribute",
        },
    )
    update_sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "updateSequence",
            "type": "Attribute",
        },
    )
