

def config_openapi() -> dict:
    return {
        "components": {
            "parameters": {
                "bbox": {
                    "description": "Only features that have a geometry that intersects the bounding box are selected.The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth).",
                    "explode": False,
                    "in": "query",
                    "name": "bbox",
                    "required": False,
                    "schema": {
                        "items": {
                            "type": "number"
                        },
                        "maxItems": 6,
                        "minItems": 4,
                        "type": "array"
                    },
                    "style": "form"
                },
                "bbox-crs": {
                    "description": "Indicates the coordinate reference system for the given bbox coordinates.",
                    "explode": False,
                    "in": "query",
                    "name": "bbox-crs",
                    "required": False,
                    "schema": {
                        "format": "uri",
                        "type": "string"
                    },
                    "style": "form"
                },
                "bbox-crs-epsg": {
                    "description": "Indicates the EPSG for the given bbox coordinates.",
                    "explode": False,
                    "in": "query",
                    "name": "bbox-crs",
                    "required": False,
                    "schema": {
                        "default": 4326,
                        "type": "integer"
                    },
                    "style": "form"
                },
                "crs": {
                    "description": "Indicates the coordinate reference system for the results.",
                    "explode": False,
                    "in": "query",
                    "name": "crs",
                    "required": False,
                    "schema": {
                        "format": "uri",
                        "type": "string"
                    },
                    "style": "form"
                },
                "f": {
                    "description": "The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON.",
                    "explode": False,
                    "in": "query",
                    "name": "f",
                    "required": False,
                    "schema": {
                        "default": "json",
                        "enum": [
                            "json",
                            "html",
                            "jsonld"
                        ],
                        "type": "string"
                    },
                    "style": "form"
                },
                "lang": {
                    "description": "The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. \"fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7\"), simple (e.g. \"de\") or locale-like (e.g. \"de-CH\" or \"fr_BE\") fashion.",
                    "in": "query",
                    "name": "lang",
                    "required": False,
                    "schema": {
                        "default": "en-US",
                        "enum": [
                            "en-US",
                            "fr-CA"
                        ],
                        "type": "string"
                    }
                },
                "offset": {
                    "description": "The optional offset parameter indicates the index within the result set from which the server shall begin presenting results in the response document.  The first element has an index of 0 (default).",
                    "explode": False,
                    "in": "query",
                    "name": "offset",
                    "required": False,
                    "schema": {
                        "default": 0,
                        "minimum": 0,
                        "type": "integer"
                    },
                    "style": "form"
                },
                "resourceId": {
                    "description": "Configuration resource identifier",
                    "in": "path",
                    "name": "resourceId",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                },
                "skipGeometry": {
                    "description": "This option can be used to skip response geometries for each feature.",
                    "explode": False,
                    "in": "query",
                    "name": "skipGeometry",
                    "required": False,
                    "schema": {
                        "default": False,
                        "type": "boolean"
                    },
                    "style": "form"
                },
                "vendorSpecificParameters": {
                    "description": "Additional \"free-form\" parameters that are not explicitly defined",
                    "in": "query",
                    "name": "vendorSpecificParameters",
                    "schema": {
                        "additionalProperties": True,
                        "type": "object"
                    },
                    "style": "form"
                }
            },
            "responses": {
                "200": {
                    "description": "successful operation"
                },
                "204": {
                    "description": "no content"
                },
                "Queryables": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/queryables"
                            }
                        }
                    },
                    "description": "successful queryables operation"
                },
                "Tiles": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/tiles"
                            }
                        }
                    },
                    "description": "Retrieves the tiles description for this collection"
                },
                "default": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "https://schemas.opengis.net/ogcapi/processes/part1/1.0/openapi/schemas/exception.yaml"
                            }
                        }
                    },
                    "description": "Unexpected error"
                }
            },
            "schemas": {
                "queryable": {
                    "properties": {
                        "description": {
                            "description": "a human-readable narrative describing the queryable",
                            "type": "string"
                        },
                        "language": {
                            "default": [
                                "en"
                            ],
                            "description": "the language used for the title and description",
                            "type": "string"
                        },
                        "queryable": {
                            "description": "the token that may be used in a CQL predicate",
                            "type": "string"
                        },
                        "title": {
                            "description": "a human readable title for the queryable",
                            "type": "string"
                        },
                        "type": {
                            "description": "the data type of the queryable",
                            "type": "string"
                        },
                        "type-ref": {
                            "description": "a reference to the formal definition of the type",
                            "format": "url",
                            "type": "string"
                        }
                    },
                    "required": [
                        "queryable",
                        "type"
                    ],
                    "type": "object"
                },
                "queryables": {
                    "properties": {
                        "queryables": {
                            "items": {
                                "$ref": "#/components/schemas/queryable"
                            },
                            "type": "array"
                        }
                    },
                    "required": [
                        "queryables"
                    ],
                    "type": "object"
                },
                "tilematrixsetlink": {
                    "properties": {
                        "tileMatrixSet": {
                            "type": "string"
                        },
                        "tileMatrixSetURI": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "tileMatrixSet"
                    ],
                    "type": "object"
                },
                "tiles": {
                    "properties": {
                        "links": {
                            "items": {
                                "$ref": "https://schemas.opengis.net/ogcapi/tiles/part1/1.0/openapi/ogcapi-tiles-1.yaml#/components/schemas/link"
                            },
                            "type": "array"
                        },
                        "tileMatrixSetLinks": {
                            "items": {
                                "$ref": "#/components/schemas/tilematrixsetlink"
                            },
                            "type": "array"
                        }
                    },
                    "required": [
                        "tileMatrixSetLinks",
                        "links"
                    ],
                    "type": "object"
                }
            }
        },
        "info": {
            "contact": {
                "email": "you@example.org",
                "name": "Organization Name",
                "url": "https://pygeoapi.io"
            },
            "description": "pygeoapi provides an API to geospatial data",
            "license": {
                "name": "CC-BY 4.0 license",
                "url": "https://creativecommons.org/licenses/by/4.0/"
            },
            "termsOfService": "None",
            "title": "pygeoapi default instance",
            "version": "3.0.2",
            "x-keywords": [
                "geospatial",
                "data",
                "api"
            ]
        },
        "openapi": "3.0.2",
        "paths": {
            "/openapi": {
                "get": {
                    "description": "This document",
                    "operationId": "getOpenapi",
                    "parameters": [
                        {
                            "$ref": "#/components/parameters/f"
                        },
                        {
                            "$ref": "#/components/parameters/lang"
                        },
                        {
                            "description": "UI to render the OpenAPI document",
                            "explode": False,
                            "in": "query",
                            "name": "ui",
                            "required": False,
                            "schema": {
                                "default": "swagger",
                                "enum": [
                                    "swagger",
                                    "redoc"
                                ],
                                "type": "string"
                            },
                            "style": "form"
                        }
                    ],
                    "responses": {
                        "200": {
                            "$ref": "#/components/responses/200"
                        },
                        "400": {
                            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/InvalidParameter"
                        },
                        "default": {
                            "$ref": "#/components/responses/default"
                        }
                    },
                    "summary": "This document",
                    "tags": [
                        "server"
                    ]
                }
            },
            "/collections": {
                "get": {
                    "description": "Feature Collections",
                    "operationId": "getCollections",
                    "parameters": [
                        {
                            "$ref": "#/components/parameters/f"
                        }, {
                            "$ref": "#/components/parameters/lang"
                        }
                    ],
                    "responses": {
                        "200": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/Collections"
                        },
                        "400": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/InvalidParameter"
                        },
                        "500": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/ServerError"
                        }
                    },
                    "summary": "Feature Collections",
                    "tags": [
                        "server"
                    ]
                }
            },
            "/conformance": {
                "get": {
                    "description": "API conformance definition",
                    "operationId": "getConformanceDeclaration",
                    "parameters": [
                        {
                            "$ref": "#/components/parameters/f"
                        }, {
                            "$ref": "#/components/parameters/lang"
                        }
                    ],
                    "responses": {
                        "200": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/ConformanceDeclaration"
                        },
                        "400": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/InvalidParameter"
                        },
                        "500": {
                            "$ref": "http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml#/components/responses/ServerError"
                        }
                    },
                    "summary": "API conformance definition",
                    "tags": [
                        "server"
                    ]
                }
            }
        },
        "servers": [
            {
                "description": "pygeoapi provides an API to geospatial data",
                "url": "OVERWRITTEN ON RUNTIME"
            }
        ],
        "tags": [
            {
                "description": "pygeoapi provides an API to geospatial data",
                "externalDocs": {
                    "description": "information",
                    "url": "http://example.org"
                },
                "name": "server"
            },
            {
                "description": "Kantonsgrenzen",
                "name": "kantonsgrenzen"
            }
        ]
    }