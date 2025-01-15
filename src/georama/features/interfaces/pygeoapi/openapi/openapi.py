from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Ref1:
    class Meta:
        name = "$ref"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GetPutPostDeleteOptionsHeadPatchTrace:
    class Meta:
        name = "^(get|put|post|delete|options|head|patch|trace)$"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ref2:
    class Meta:
        name = r"^\$ref$"

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


@dataclass
class TypeType:
    class Meta:
        name = r"^\/"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class X:
    class Meta:
        name = "^x-"


@dataclass
class AdditionalProperties:
    class Meta:
        name = "additionalProperties"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    items: Optional["Items"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    one_of: List["OneOf"] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
        },
    )
    default: Optional[bool] = field(
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
class AllowEmptyValue:
    class Meta:
        name = "allowEmptyValue"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class AllowReserved:
    class Meta:
        name = "allowReserved"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class Attribute:
    class Meta:
        name = "attribute"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class AuthorizationCode:
    class Meta:
        name = "authorizationCode"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AuthorizationUrl:
    class Meta:
        name = "authorizationUrl"

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


@dataclass
class BearerFormat:
    class Meta:
        name = "bearerFormat"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ClientCredentials:
    class Meta:
        name = "clientCredentials"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Components2:
    class Meta:
        name = "components"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Contact2:
    class Meta:
        name = "contact"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ContentType:
    class Meta:
        name = "contentType"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Deprecated:
    class Meta:
        name = "deprecated"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class Description:
    class Meta:
        name = "description"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Discriminator2:
    class Meta:
        name = "discriminator"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
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
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Example2:
    class Meta:
        name = "example"


@dataclass
class ExclusiveMaximum:
    class Meta:
        name = "exclusiveMaximum"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class ExclusiveMinimum:
    class Meta:
        name = "exclusiveMinimum"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class Explode:
    class Meta:
        name = "explode"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ExternalDocs:
    class Meta:
        name = "externalDocs"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ExternalValue:
    class Meta:
        name = "externalValue"

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


@dataclass
class Flows:
    class Meta:
        name = "flows"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
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


@dataclass
class Implicit:
    class Meta:
        name = "implicit"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class In:
    class Meta:
        name = "in"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Info2:
    class Meta:
        name = "info"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class License2:
    class Meta:
        name = "license"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MaxItems:
    class Meta:
        name = "maxItems"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    minimum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MaxLength:
    class Meta:
        name = "maxLength"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    minimum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MaxProperties:
    class Meta:
        name = "maxProperties"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    minimum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Maximum:
    class Meta:
        name = "maximum"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MinItems:
    class Meta:
        name = "minItems"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    minimum: Optional[int] = field(
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
class MinLength:
    class Meta:
        name = "minLength"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    minimum: Optional[int] = field(
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
class MinProperties:
    class Meta:
        name = "minProperties"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    minimum: Optional[int] = field(
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
class Minimum:
    class Meta:
        name = "minimum"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MultipleOf:
    class Meta:
        name = "multipleOf"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    minimum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    exclusive_minimum: Optional[bool] = field(
        default=None,
        metadata={
            "name": "exclusiveMinimum",
            "type": "Element",
            "required": True,
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
            "required": True,
        },
    )


@dataclass
class Namespace:
    class Meta:
        name = "namespace"

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


@dataclass
class Not:
    class Meta:
        name = "not"

    description: Optional[str] = field(
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
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    one_of: List["OneOf"] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
        },
    )


@dataclass
class Nullable:
    class Meta:
        name = "nullable"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class OpenIdConnectUrl:
    class Meta:
        name = "openIdConnectUrl"

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


@dataclass
class OperationId:
    class Meta:
        name = "operationId"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OperationRef:
    class Meta:
        name = "operationRef"

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


@dataclass
class Password:
    class Meta:
        name = "password"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Paths2:
    class Meta:
        name = "paths"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Pattern:
    class Meta:
        name = "pattern"

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


@dataclass
class Prefix:
    class Meta:
        name = "prefix"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PropertyName:
    class Meta:
        name = "propertyName"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ReadOnly:
    class Meta:
        name = "readOnly"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class RefreshUrl:
    class Meta:
        name = "refreshUrl"

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


@dataclass
class Server2:
    class Meta:
        name = "server"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Style:
    class Meta:
        name = "style"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Summary:
    class Meta:
        name = "summary"

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
        name = "termsOfService"

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


@dataclass
class Title:
    class Meta:
        name = "title"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TokenUrl:
    class Meta:
        name = "tokenUrl"

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
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class UniqueItems:
    class Meta:
        name = "uniqueItems"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class Url:
    class Meta:
        name = "url"

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
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"


@dataclass
class Version:
    class Meta:
        name = "version"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Wrapped:
    class Meta:
        name = "wrapped"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class WriteOnly:
    class Meta:
        name = "writeOnly"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class Xml2:
    class Meta:
        name = "xml"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ExampleXorexamples:
    class Meta:
        name = "ExampleXORExamples"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SecurityRequirement:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Content:
    class Meta:
        name = "content"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )
    min_properties: Optional[int] = field(
        default=None,
        metadata={
            "name": "minProperties",
            "type": "Element",
        },
    )
    max_properties: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxProperties",
            "type": "Element",
        },
    )


@dataclass
class Encoding2:
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
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Headers:
    class Meta:
        name = "headers"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
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


@dataclass
class Mapping:
    class Meta:
        name = "mapping"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Scheme:
    class Meta:
        name = "scheme"

    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    enum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )


@dataclass
class Scopes:
    class Meta:
        name = "scopes"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Variables:
    class Meta:
        name = "variables"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Properties:
    class Meta:
        name = "properties"

    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    multiple_of: Optional[MultipleOf] = field(
        default=None,
        metadata={
            "name": "multipleOf",
            "type": "Element",
        },
    )
    maximum: Optional[Maximum] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exclusive_maximum: Optional[ExclusiveMaximum] = field(
        default=None,
        metadata={
            "name": "exclusiveMaximum",
            "type": "Element",
        },
    )
    minimum: Optional[Minimum] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exclusive_minimum: Optional[ExclusiveMinimum] = field(
        default=None,
        metadata={
            "name": "exclusiveMinimum",
            "type": "Element",
        },
    )
    max_length: Optional[MaxLength] = field(
        default=None,
        metadata={
            "name": "maxLength",
            "type": "Element",
        },
    )
    min_length: Optional[MinLength] = field(
        default=None,
        metadata={
            "name": "minLength",
            "type": "Element",
        },
    )
    pattern: Optional[Pattern] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    max_items: Optional[MaxItems] = field(
        default=None,
        metadata={
            "name": "maxItems",
            "type": "Element",
        },
    )
    min_items: Optional[MinItems] = field(
        default=None,
        metadata={
            "name": "minItems",
            "type": "Element",
        },
    )
    unique_items: Optional[UniqueItems] = field(
        default=None,
        metadata={
            "name": "uniqueItems",
            "type": "Element",
        },
    )
    max_properties: Optional[MaxProperties] = field(
        default=None,
        metadata={
            "name": "maxProperties",
            "type": "Element",
        },
    )
    min_properties: Optional[MinProperties] = field(
        default=None,
        metadata={
            "name": "minProperties",
            "type": "Element",
        },
    )
    required: Optional["Required"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    enum: Optional["EnumType"] = field(
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
    not_value: Optional["Not"] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    all_of: Optional["AllOf"] = field(
        default=None,
        metadata={
            "name": "allOf",
            "type": "Element",
        },
    )
    one_of: Optional["OneOf"] = field(
        default=None,
        metadata={
            "name": "oneOf",
            "type": "Element",
        },
    )
    any_of: Optional["AnyOf"] = field(
        default=None,
        metadata={
            "name": "anyOf",
            "type": "Element",
        },
    )
    items: Optional["Items"] = field(
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
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    in_value: Optional[In] = field(
        default=None,
        metadata={
            "name": "in",
            "type": "Element",
        },
    )
    tags: Optional["Tags"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ref: Optional[Ref1] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
        },
    )
    summary: Optional[Summary] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scheme: Optional["Scheme"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bearer_format: Optional[BearerFormat] = field(
        default=None,
        metadata={
            "name": "bearerFormat",
            "type": "Element",
        },
    )
    open_id_connect_url: Optional[OpenIdConnectUrl] = field(
        default=None,
        metadata={
            "name": "openIdConnectUrl",
            "type": "Element",
        },
    )
    flows: Optional[Flows] = field(
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
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    format: Optional[Format] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    default: Optional["Default"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    nullable: Optional[Nullable] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    discriminator: Optional[Discriminator2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    read_only: Optional[ReadOnly] = field(
        default=None,
        metadata={
            "name": "readOnly",
            "type": "Element",
        },
    )
    write_only: Optional[WriteOnly] = field(
        default=None,
        metadata={
            "name": "writeOnly",
            "type": "Element",
        },
    )
    allow_empty_value: Optional[AllowEmptyValue] = field(
        default=None,
        metadata={
            "name": "allowEmptyValue",
            "type": "Element",
        },
    )
    style: Optional[Style] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    explode: Optional[Explode] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    allow_reserved: Optional[AllowReserved] = field(
        default=None,
        metadata={
            "name": "allowReserved",
            "type": "Element",
        },
    )
    schema: Optional["Schema2"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    content: Optional[Content] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    example: Optional[Example2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    openapi: Optional["Openapi"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    info: Optional[Info2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    external_docs: Optional[ExternalDocs] = field(
        default=None,
        metadata={
            "name": "externalDocs",
            "type": "Element",
        },
    )
    operation_id: Optional[OperationId] = field(
        default=None,
        metadata={
            "name": "operationId",
            "type": "Element",
        },
    )
    operation_ref: Optional[OperationRef] = field(
        default=None,
        metadata={
            "name": "operationRef",
            "type": "Element",
        },
    )
    parameters: Optional["Parameters"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    request_body: Optional["RequestBody2"] = field(
        default=None,
        metadata={
            "name": "requestBody",
            "type": "Element",
        },
    )
    schemas: Optional["Schemas"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    responses: Optional["Responses2"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    request_bodies: Optional["RequestBodies"] = field(
        default=None,
        metadata={
            "name": "requestBodies",
            "type": "Element",
        },
    )
    content_type: Optional[ContentType] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
        },
    )
    headers: Optional[Headers] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    security_schemes: Optional["SecuritySchemes"] = field(
        default=None,
        metadata={
            "name": "securitySchemes",
            "type": "Element",
        },
    )
    links: Optional["Links"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    callbacks: Optional["Callbacks"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    deprecated: Optional[Deprecated] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[Xml2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    examples: Optional["Examples"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    security: Optional["Security"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    servers: Optional["Servers"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    paths: Optional[Paths2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    components: Optional[Components2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    server: Optional[Server2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    terms_of_service: Optional[TermsOfService] = field(
        default=None,
        metadata={
            "name": "termsOfService",
            "type": "Element",
        },
    )
    contact: Optional[Contact2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    license: Optional[License2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    namespace: Optional[Namespace] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    prefix: Optional[Prefix] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    attribute: Optional[Attribute] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    wrapped: Optional[Wrapped] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    authorization_url: Optional[AuthorizationUrl] = field(
        default=None,
        metadata={
            "name": "authorizationUrl",
            "type": "Element",
        },
    )
    token_url: Optional[TokenUrl] = field(
        default=None,
        metadata={
            "name": "tokenUrl",
            "type": "Element",
        },
    )
    refresh_url: Optional[RefreshUrl] = field(
        default=None,
        metadata={
            "name": "refreshUrl",
            "type": "Element",
        },
    )
    scopes: Optional[Scopes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    implicit: Optional[Implicit] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    password: Optional[Password] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    client_credentials: Optional[ClientCredentials] = field(
        default=None,
        metadata={
            "name": "clientCredentials",
            "type": "Element",
        },
    )
    authorization_code: Optional[AuthorizationCode] = field(
        default=None,
        metadata={
            "name": "authorizationCode",
            "type": "Element",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    external_value: Optional[ExternalValue] = field(
        default=None,
        metadata={
            "name": "externalValue",
            "type": "Element",
        },
    )
    encoding: Optional[Encoding2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variables: Optional[Variables] = field(
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
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "propertyName",
            "type": "Element",
        },
    )
    mapping: Optional[Mapping] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Discriminator1:
    class Meta:
        name = "Discriminator"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Encoding1:
    class Meta:
        name = "Encoding"

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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OneOf:
    class Meta:
        name = "oneOf"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    required: List[str] = field(
        default_factory=list,
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
    all_of: List["AllOf"] = field(
        default_factory=list,
        metadata={
            "name": "allOf",
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    items: Optional["Items"] = field(
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
class ParameterLocation:
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class SchemaXorcontent:
    class Meta:
        name = "SchemaXORContent"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
            "required": True,
        },
    )
    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class SecurityScheme:
    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Type15D2Xx:
    class Meta:
        name = r"^[1-5](?:\d{2}|XX)$"

    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class AZAZ09:
    class Meta:
        name = r"^[a-zA-Z0-9\.\-_]+$"

    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Default:
    class Meta:
        name = "default"

    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
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
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
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


@dataclass
class RequestBody2:
    class Meta:
        name = "requestBody"

    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
        },
    )


@dataclass
class Schema2:
    class Meta:
        name = "schema"

    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
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
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
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
    items: Optional[Items] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EnumType:
    class Meta:
        name = "enum"

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
            "required": True,
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


@dataclass
class PatternProperties:
    class Meta:
        name = "patternProperties"

    value_1_5_d_2_xx: Optional[Type15D2Xx] = field(
        default=None,
        metadata={
            "name": "^[1-5](?:\\d{2}|XX)$",
            "type": "Element",
        },
    )
    get_put_post_delete_options_head_patch_trace: Optional[
        GetPutPostDeleteOptionsHeadPatchTrace
    ] = field(
        default=None,
        metadata={
            "name": "^(get|put|post|delete|options|head|patch|trace)$",
            "type": "Element",
        },
    )
    circumflex_accent_reverse_solidus_solidus: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "^\\/",
            "type": "Element",
        },
    )
    x: Optional[X] = field(
        default=None,
        metadata={
            "name": "^x-",
            "type": "Element",
        },
    )
    a_z_a_z0_9: Optional[AZAZ09] = field(
        default=None,
        metadata={
            "name": "^[a-zA-Z0-9\\.\\-_]+$",
            "type": "Element",
        },
    )
    ref: Optional[Ref2] = field(
        default=None,
        metadata={
            "name": "^\\$ref$",
            "type": "Element",
        },
    )


@dataclass
class Required:
    class Meta:
        name = "required"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    items: Optional[Items] = field(
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
    default: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    enum: List[bool] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Security:
    class Meta:
        name = "security"

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
            "required": True,
        },
    )


@dataclass
class Servers:
    class Meta:
        name = "servers"

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
            "required": True,
        },
    )


@dataclass
class Tags:
    class Meta:
        name = "tags"

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
            "required": True,
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
class ApikeySecurityScheme:
    class Meta:
        name = "APIKeySecurityScheme"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AuthorizationCodeOauthFlow:
    class Meta:
        name = "AuthorizationCodeOAuthFlow"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Callback:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
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
class ClientCredentialsFlow:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Components1:
    class Meta:
        name = "Components"

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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Contact1:
    class Meta:
        name = "Contact"

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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Example1:
    class Meta:
        name = "Example"

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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ExternalDocumentation:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class HttpsecurityScheme:
    class Meta:
        name = "HTTPSecurityScheme"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )
    one_of: List[OneOf] = field(
        default_factory=list,
        metadata={
            "name": "oneOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Header:
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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )
    all_of: List[AllOf] = field(
        default_factory=list,
        metadata={
            "name": "allOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ImplicitOauthFlow:
    class Meta:
        name = "ImplicitOAuthFlow"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Info1:
    class Meta:
        name = "Info"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class License1:
    class Meta:
        name = "License"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Link:
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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MediaType:
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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )
    all_of: List[AllOf] = field(
        default_factory=list,
        metadata={
            "name": "allOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Oauth2SecurityScheme:
    class Meta:
        name = "OAuth2SecurityScheme"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OauthFlows:
    class Meta:
        name = "OAuthFlows"

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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OpenIdConnectSecurityScheme:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Operation:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Parameter:
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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
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
    all_of: List[AllOf] = field(
        default_factory=list,
        metadata={
            "name": "allOf",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class PasswordOauthFlow:
    class Meta:
        name = "PasswordOAuthFlow"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PathItem:
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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Paths1:
    class Meta:
        name = "Paths"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Reference:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RequestBody1:
    class Meta:
        name = "RequestBody"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Response:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Responses1:
    class Meta:
        name = "Responses"

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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    min_properties: Optional[int] = field(
        default=None,
        metadata={
            "name": "minProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Schema1:
    class Meta:
        name = "Schema"

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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ServerVariable:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Server1:
    class Meta:
        name = "Server"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Tag:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    properties: Optional[Properties] = field(
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
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Xml1:
    class Meta:
        name = "XML"

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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Callbacks:
    class Meta:
        name = "callbacks"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
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


@dataclass
class Examples:
    class Meta:
        name = "examples"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
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
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
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


@dataclass
class Parameters:
    class Meta:
        name = "parameters"

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
    unique_items: Optional[bool] = field(
        default=None,
        metadata={
            "name": "uniqueItems",
            "type": "Element",
        },
    )
    additional_properties: Optional[AdditionalProperties] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
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


@dataclass
class RequestBodies:
    class Meta:
        name = "requestBodies"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class Responses2:
    class Meta:
        name = "responses"

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
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "$ref",
            "type": "Element",
        },
    )


@dataclass
class Schemas:
    class Meta:
        name = "schemas"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class SecuritySchemes:
    class Meta:
        name = "securitySchemes"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class Definitions:
    class Meta:
        name = "definitions"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        },
    )
    info: Optional[Info1] = field(
        default=None,
        metadata={
            "name": "Info",
            "type": "Element",
            "required": True,
        },
    )
    contact: Optional[Contact1] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        },
    )
    license: Optional[License1] = field(
        default=None,
        metadata={
            "name": "License",
            "type": "Element",
            "required": True,
        },
    )
    server: Optional[Server1] = field(
        default=None,
        metadata={
            "name": "Server",
            "type": "Element",
            "required": True,
        },
    )
    server_variable: Optional[ServerVariable] = field(
        default=None,
        metadata={
            "name": "ServerVariable",
            "type": "Element",
            "required": True,
        },
    )
    components: Optional[Components1] = field(
        default=None,
        metadata={
            "name": "Components",
            "type": "Element",
            "required": True,
        },
    )
    schema: Optional[Schema1] = field(
        default=None,
        metadata={
            "name": "Schema",
            "type": "Element",
            "required": True,
        },
    )
    discriminator: Optional[Discriminator1] = field(
        default=None,
        metadata={
            "name": "Discriminator",
            "type": "Element",
            "required": True,
        },
    )
    xml: Optional[Xml1] = field(
        default=None,
        metadata={
            "name": "XML",
            "type": "Element",
            "required": True,
        },
    )
    response: Optional[Response] = field(
        default=None,
        metadata={
            "name": "Response",
            "type": "Element",
            "required": True,
        },
    )
    media_type: Optional[MediaType] = field(
        default=None,
        metadata={
            "name": "MediaType",
            "type": "Element",
            "required": True,
        },
    )
    example: Optional[Example1] = field(
        default=None,
        metadata={
            "name": "Example",
            "type": "Element",
            "required": True,
        },
    )
    header: Optional[Header] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "required": True,
        },
    )
    paths: Optional[Paths1] = field(
        default=None,
        metadata={
            "name": "Paths",
            "type": "Element",
            "required": True,
        },
    )
    path_item: Optional[PathItem] = field(
        default=None,
        metadata={
            "name": "PathItem",
            "type": "Element",
            "required": True,
        },
    )
    operation: Optional[Operation] = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Element",
            "required": True,
        },
    )
    responses: Optional[Responses1] = field(
        default=None,
        metadata={
            "name": "Responses",
            "type": "Element",
            "required": True,
        },
    )
    security_requirement: Optional[SecurityRequirement] = field(
        default=None,
        metadata={
            "name": "SecurityRequirement",
            "type": "Element",
            "required": True,
        },
    )
    tag: Optional[Tag] = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Element",
            "required": True,
        },
    )
    external_documentation: Optional[ExternalDocumentation] = field(
        default=None,
        metadata={
            "name": "ExternalDocumentation",
            "type": "Element",
            "required": True,
        },
    )
    example_xorexamples: Optional[ExampleXorexamples] = field(
        default=None,
        metadata={
            "name": "ExampleXORExamples",
            "type": "Element",
            "required": True,
        },
    )
    schema_xorcontent: Optional[SchemaXorcontent] = field(
        default=None,
        metadata={
            "name": "SchemaXORContent",
            "type": "Element",
            "required": True,
        },
    )
    parameter: Optional[Parameter] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "required": True,
        },
    )
    parameter_location: Optional[ParameterLocation] = field(
        default=None,
        metadata={
            "name": "ParameterLocation",
            "type": "Element",
            "required": True,
        },
    )
    request_body: Optional[RequestBody1] = field(
        default=None,
        metadata={
            "name": "RequestBody",
            "type": "Element",
            "required": True,
        },
    )
    security_scheme: Optional[SecurityScheme] = field(
        default=None,
        metadata={
            "name": "SecurityScheme",
            "type": "Element",
            "required": True,
        },
    )
    apikey_security_scheme: Optional[ApikeySecurityScheme] = field(
        default=None,
        metadata={
            "name": "APIKeySecurityScheme",
            "type": "Element",
            "required": True,
        },
    )
    httpsecurity_scheme: Optional[HttpsecurityScheme] = field(
        default=None,
        metadata={
            "name": "HTTPSecurityScheme",
            "type": "Element",
            "required": True,
        },
    )
    oauth2_security_scheme: Optional[Oauth2SecurityScheme] = field(
        default=None,
        metadata={
            "name": "OAuth2SecurityScheme",
            "type": "Element",
            "required": True,
        },
    )
    open_id_connect_security_scheme: Optional[OpenIdConnectSecurityScheme] = field(
        default=None,
        metadata={
            "name": "OpenIdConnectSecurityScheme",
            "type": "Element",
            "required": True,
        },
    )
    oauth_flows: Optional[OauthFlows] = field(
        default=None,
        metadata={
            "name": "OAuthFlows",
            "type": "Element",
            "required": True,
        },
    )
    implicit_oauth_flow: Optional[ImplicitOauthFlow] = field(
        default=None,
        metadata={
            "name": "ImplicitOAuthFlow",
            "type": "Element",
            "required": True,
        },
    )
    password_oauth_flow: Optional[PasswordOauthFlow] = field(
        default=None,
        metadata={
            "name": "PasswordOAuthFlow",
            "type": "Element",
            "required": True,
        },
    )
    client_credentials_flow: Optional[ClientCredentialsFlow] = field(
        default=None,
        metadata={
            "name": "ClientCredentialsFlow",
            "type": "Element",
            "required": True,
        },
    )
    authorization_code_oauth_flow: Optional[AuthorizationCodeOauthFlow] = field(
        default=None,
        metadata={
            "name": "AuthorizationCodeOAuthFlow",
            "type": "Element",
            "required": True,
        },
    )
    link: Optional[Link] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
            "required": True,
        },
    )
    callback: Optional[Callback] = field(
        default=None,
        metadata={
            "name": "Callback",
            "type": "Element",
            "required": True,
        },
    )
    encoding: Optional[Encoding1] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Openapi:
    class Meta:
        name = "openapi"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "$schema",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
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
    required: List[str] = field(
        default_factory=list,
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
    pattern_properties: Optional[PatternProperties] = field(
        default=None,
        metadata={
            "name": "patternProperties",
            "type": "Element",
        },
    )
    additional_properties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "additionalProperties",
            "type": "Element",
        },
    )
    definitions: Optional[Definitions] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
