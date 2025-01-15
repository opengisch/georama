from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Address:
    class Meta:
        name = "address"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Admin:
    class Meta:
        name = "admin"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ApiVersion:
    class Meta:
        name = "api_version"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Attribution:
    class Meta:
        name = "attribution"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BackupCount:
    class Meta:
        name = "backup_count"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Begin:
    class Meta:
        name = "begin"

    type_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    nullable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class City:
    class Meta:
        name = "city"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConnectTimeout:
    class Meta:
        name = "connect_timeout"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Connection:
    class Meta:
        name = "connection"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Cors:
    class Meta:
        name = "cors"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Country:
    class Meta:
        name = "country"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Dateformat:
    class Meta:
        name = "dateformat"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Default:
    class Meta:
        name = "default"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Description:
    class Meta:
        name = "description"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Editable:
    class Meta:
        name = "editable"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Email:
    class Meta:
        name = "email"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Encoding:
    class Meta:
        name = "encoding"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class End:
    class Meta:
        name = "end"

    type_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    nullable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Fax:
    class Meta:
        name = "fax"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Gzip:
    class Meta:
        name = "gzip"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Host:
    class Meta:
        name = "host"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Hours:
    class Meta:
        name = "hours"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Href:
    class Meta:
        name = "href"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Hreflang:
    class Meta:
        name = "hreflang"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IdField:
    class Meta:
        name = "id_field"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Instructions:
    class Meta:
        name = "instructions"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Interval:
    class Meta:
        name = "interval"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ItemTemplate:
    class Meta:
        name = "item_template"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Keepalives:
    class Meta:
        name = "keepalives"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KeepalivesCount:
    class Meta:
        name = "keepalives_count"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KeepalivesIdle:
    class Meta:
        name = "keepalives_idle"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KeepalivesInterval:
    class Meta:
        name = "keepalives_interval"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Keywords:
    class Meta:
        name = "keywords"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KeywordsType:
    class Meta:
        name = "keywords_type"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Language:
    class Meta:
        name = "language"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Length:
    class Meta:
        name = "length"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Level:
    class Meta:
        name = "level"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Limit:
    class Meta:
        name = "limit"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LocaleDir:
    class Meta:
        name = "locale_dir"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Logfile:
    class Meta:
        name = "logfile"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Logformat:
    class Meta:
        name = "logformat"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MaxBytes:
    class Meta:
        name = "max_bytes"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Mimetype:
    class Meta:
        name = "mimetype"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Mode:
    class Meta:
        name = "mode"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Name:
    class Meta:
        name = "name"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OgcSchemasLocation:
    class Meta:
        name = "ogc_schemas_location"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OutputDir:
    class Meta:
        name = "output_dir"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Path:
    class Meta:
        name = "path"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Phone:
    class Meta:
        name = "phone"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Port:
    class Meta:
        name = "port"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Position:
    class Meta:
        name = "position"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Postalcode:
    class Meta:
        name = "postalcode"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PrettyPrint:
    class Meta:
        name = "pretty_print"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Rel:
    class Meta:
        name = "rel"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Role:
    class Meta:
        name = "role"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Stateorprovince:
    class Meta:
        name = "stateorprovince"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Static:
    class Meta:
        name = "static"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StorageCrs:
    class Meta:
        name = "storage_crs"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StorageCrsCoordinateEpoch:
    class Meta:
        name = "storage_crs_coordinate_epoch"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    example: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StrictSlashes:
    class Meta:
        name = "strict_slashes"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Table:
    class Meta:
        name = "table"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TcpUserTimeout:
    class Meta:
        name = "tcp_user_timeout"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TermsOfService:
    class Meta:
        name = "terms_of_service"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TimeField:
    class Meta:
        name = "time_field"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Title:
    class Meta:
        name = "title"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TitleField:
    class Meta:
        name = "title_field"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Trs:
    class Meta:
        name = "trs"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TypeType:
    class Meta:
        name = "type"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Url:
    class Meta:
        name = "url"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class UrlPrefix:
    class Meta:
        name = "url_prefix"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VersionHeader:
    class Meta:
        name = "version_header"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Visibility:
    class Meta:
        name = "visibility"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class When:
    class Meta:
        name = "when"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class XField:
    class Meta:
        name = "x_field"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class YField:
    class Meta:
        name = "y_field"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Properties:
    class Meta:
        name = "properties"

    bind: Optional["Bind"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    position: Optional[Position] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    city: Optional[City] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    stateorprovince: Optional[Stateorprovince] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    postalcode: Optional[Postalcode] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    phone: Optional[Phone] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fax: Optional[Fax] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    email: Optional[Email] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    keywords_type: Optional[KeywordsType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    terms_of_service: Optional[TermsOfService] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    url: Optional[Url] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    admin: Optional[Admin] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mimetype: Optional[Mimetype] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    encoding: Optional[Encoding] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gzip: Optional[Gzip] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    languages: Optional["Languages"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    locale_dir: Optional[LocaleDir] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cors: Optional[Cors] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pretty_print: Optional[PrettyPrint] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    limit: Optional[Limit] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    templates: Optional["Templates"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    map: Optional["Map"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ogc_schemas_location: Optional[OgcSchemasLocation] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    manager: Optional["Manager"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    api_rules: Optional["ApiRules"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    type_value: Optional[Union[TypeType, str]] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    default: Optional[Default] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data: Optional["Data"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    editable: Optional[Editable] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    table: Optional[Table] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id_field: Optional[IdField] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    geometry: Optional["Geometry"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time_field: Optional[TimeField] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title_field: Optional[TitleField] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    format: Optional["Format"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    options: Optional["Options"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bbox: Optional["Bbox"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    crs: Optional["Crs"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    storage_crs: Optional[StorageCrs] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    storage_crs_coordinate_epoch: Optional[StorageCrsCoordinateEpoch] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    hours: Optional[Hours] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    instructions: Optional[Instructions] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rel: Optional[Rel] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    description: Optional[Union[Description, str]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    keywords: Optional[Keywords] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    linked_data: Optional["LinkedData"] = field(
        default=None,
        metadata={
            "name": "linked-data",
            "type": "Element",
        },
    )
    links: Optional["Links"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    extents: Optional["Extents"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    providers: Optional["Providers"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    connect_timeout: Optional[ConnectTimeout] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tcp_user_timeout: Optional[TcpUserTimeout] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    keepalives: Optional[Keepalives] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    keepalives_idle: Optional[KeepalivesIdle] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    keepalives_count: Optional[KeepalivesCount] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    keepalives_interval: Optional[KeepalivesInterval] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    href: Optional[Href] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    hreflang: Optional[Hreflang] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    length: Optional[Length] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    items: Optional["Items"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    min_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "minItems",
            "type": "Element",
        },
    )
    unique_items: Optional[bool] = field(
        default=None,
        metadata={
            "name": "uniqueItems",
            "type": "Element",
        },
    )
    mode: Optional[Mode] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    when: Optional[When] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    interval: Optional[Interval] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    max_bytes: Optional[MaxBytes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    backup_count: Optional[BackupCount] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    level: Optional[Level] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    logfile: Optional[Logfile] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    logformat: Optional[Logformat] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dateformat: Optional[Dateformat] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rotation: Optional["Rotation"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    identification: Optional["Identification"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    license: Optional["License"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    provider: Optional["Provider"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    contact: Optional["Contact"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    api_version: Optional[ApiVersion] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    strict_slashes: Optional[StrictSlashes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    url_prefix: Optional[UrlPrefix] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    version_header: Optional[VersionHeader] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    server: Optional["Server"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    logging: Optional["Logging"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    metadata: Optional["Metadata"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    resources: Optional["Resources"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    begin: Optional[Begin] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    end: Optional[End] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    trs: Optional[Trs] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    connection: Optional[Connection] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    output_dir: Optional[OutputDir] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    processor: Optional["Processor"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    x_field: Optional[XField] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    y_field: Optional[YField] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    spatial: Optional["Spatial"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    temporal: Optional["Temporal"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    item_template: Optional[ItemTemplate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    context: Optional["Context"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    attribution: Optional[Attribution] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    path: Optional[Path] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    static: Optional[Static] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    host: Optional[Host] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    port: Optional[Port] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    config: Optional["Config"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    postgre_sql: Optional["PostgreSql"] = field(
        default=None,
        metadata={
            "name": "PostgreSQL",
            "type": "Element",
        },
    )


@dataclass
class PostgreSql:
    class Meta:
        name = "PostgreSQL"

    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AnyOf:
    class Meta:
        name = "anyOf"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ApiRules:
    class Meta:
        name = "api_rules"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Bind:
    class Meta:
        name = "bind"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Config:
    class Meta:
        name = "config"

    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Contact:
    class Meta:
        name = "contact"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Extents:
    class Meta:
        name = "extents"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Format:
    class Meta:
        name = "format"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Geometry:
    class Meta:
        name = "geometry"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Identification:
    class Meta:
        name = "identification"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Items:
    class Meta:
        name = "items"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pattern_properties: Optional["PatternProperties"] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class License:
    class Meta:
        name = "license"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class LinkedData:
    class Meta:
        name = "linked-data"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Logging:
    class Meta:
        name = "logging"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Manager:
    class Meta:
        name = "manager"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Map:
    class Meta:
        name = "map"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Metadata:
    class Meta:
        name = "metadata"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Processor:
    class Meta:
        name = "processor"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Provider:
    class Meta:
        name = "provider"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Rotation:
    class Meta:
        name = "rotation"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Spatial:
    class Meta:
        name = "spatial"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Templates:
    class Meta:
        name = "templates"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Temporal:
    class Meta:
        name = "temporal"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TypeType:
    class Meta:
        name = "^.*$"

    any_of: List[AnyOf] = field(
        default_factory=list,
        metadata={
            "name": "anyOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class AllOf:
    class Meta:
        name = "allOf"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Bbox:
    class Meta:
        name = "bbox"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    min_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "minItems",
            "type": "Element",
            "required": True,
        },
    )
    max_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxItems",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Context:
    class Meta:
        name = "context"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Crs:
    class Meta:
        name = "crs"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    default: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    unique_items: Optional[bool] = field(
        default=None,
        metadata={
            "name": "uniqueItems",
            "type": "Element",
        },
    )


@dataclass
class Data:
    class Meta:
        name = "data"

    any_of: List[AnyOf] = field(
        default_factory=list,
        metadata={
            "name": "anyOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Languages:
    class Meta:
        name = "languages"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Links:
    class Meta:
        name = "links"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    min_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "minItems",
            "type": "Element",
            "required": True,
        },
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Providers:
    class Meta:
        name = "providers"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AZAZ23AZAZ0923:
    class Meta:
        name = "^[a-zA-Z]{2,3}([-_][a-zA-Z0-9]{2,3})?$"

    all_of: List[AllOf] = field(
        default_factory=list,
        metadata={
            "name": "allOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class PatternProperties:
    class Meta:
        name = "patternProperties"

    a_z_a_z_2_3_a_z_a_z0_9_2_3: Optional[AZAZ23AZAZ0923] = field(
        default=None,
        metadata={
            "name": "^[a-zA-Z]{2,3}([-_][a-zA-Z0-9]{2,3})?$",
            "type": "Element",
        },
    )
    circumflex_accent_full_stop_asterisk_dollar_sign: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "^.*$",
            "type": "Element",
        },
    )


@dataclass
class OneOf:
    class Meta:
        name = "oneOf"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
        },
    )
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
        },
    )


@dataclass
class Resources:
    class Meta:
        name = "resources"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class I18NArray:
    class Meta:
        name = "i18n_array"

    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class I18NString:
    class Meta:
        name = "i18n_string"

    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Options:
    class Meta:
        name = "options"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Definitions:
    class Meta:
        name = "definitions"

    i18n_string: Optional[I18NString] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    i18n_array: Optional[I18NArray] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    provider: Optional[Provider] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Server:
    class Meta:
        name = "server"

    schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "$schema",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "$id",
            "type": "Element",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    definitions: Optional[Definitions] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
