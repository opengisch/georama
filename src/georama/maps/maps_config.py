from django.conf import settings

from georama.maps.interfaces.ogc.wms_1_3_0.capabilities import ServiceName
from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.xlink import TypeType


class Config:
    @property
    def redis_url(self):
        return settings.QSL_REDIS_URL

    @property
    def default_dpi(self) -> int:
        return 96

    @property
    def default_format(self) -> str:
        return "image/png"

    @property
    def job_timeout(self) -> float:
        """
        Timeout in milliseconds
        """
        return settings.JOB_TIMEOUT

    def wms_1_3_0_service_config(self, url: str) -> dict:
        service_config = {
            "Name": ServiceName.WMS.value,
            "Title": {"value": "QGIS Server light"},
            "Abstract": {"value": "this is the new approach"},
            "KeywordList": {
                "Keyword": [
                    {"value": "fast", "vocabulary": "ISO"},
                    {"value": "infoMapAccessService", "vocabulary": "ISO"},
                ]
            },
            "ContactInformation": {
                "ContactPersonPrimary": {
                    "ContactPerson": {"value": "Clemens Rudert"},
                    "ContactOrganization": {"value": "OPENGIS.ch"},
                },
                "ContactPosition": {},
                "ContactAddress": {
                    "Address": {"value": "Via Geinas 2"},
                    "City": {"value": "Laax"},
                    "StateOrProvince": {"value": "Canton Graubünden"},
                    "PostCode": {"value": "7031"},
                    "Country": {"value": "Switzerland"},
                },
                "ContactElectronicMailAddress": {"value": "sales@opengis.ch"},
            },
            "OnlineResource": {"type": TypeType.SIMPLE.value, "href": url},
            "Fees": {"value": "its for free"},
            "AccessConstraints": {"value": "None"},
        }
        return service_config

    def wms_1_3_0_capability_config(self, url: str) -> dict:
        capability_config = {
            "Request": {
                "GetCapabilities": {
                    "Format": [{"value": "text/xml"}, {"value": "application/json"}],
                    "DCPType": [
                        {
                            "HTTP": {
                                "Get": {
                                    "OnlineResource": {
                                        "type": TypeType.SIMPLE.value,
                                        "href": url,
                                    }
                                }
                            }
                        }
                    ],
                },
                "GetMap": {
                    "Format": [{"value": self.default_format}],
                    "DCPType": [
                        {
                            "HTTP": {
                                "Get": {
                                    "OnlineResource": {
                                        "type": TypeType.SIMPLE.value,
                                        "href": url,
                                    }
                                }
                            }
                        }
                    ],
                },
            },
            "Exception": {"Format": [{"value": "text/xml"}]},
            "Layer": {
                "queryable": 0,
                "opaque": 0,
                "noSubsets": 0,
                "cascaded": 0,
                "Name": "qgis_server_light",
                "Title": {"value": "QGIS Server light"},
                "Abstract": {"value": "The lightning fast access to your raster data"},
                "KeywordList": {
                    "Keyword": [
                        {"value": "fast", "vocabulary": "ISO"},
                        {"value": "infoMapAccessService", "vocabulary": "ISO"},
                    ]
                },
                "CRS": [{"value": "EPSG:2056"}, {"value": "CRS:84"}],
                "EX_GeographicBoundingBox": {
                    "westBoundLongitude": 180.0,
                    "eastBoundLongitude": -180.0,
                    "southBoundLatitude": -90.0,
                    "northBoundLatitude": 90.0,
                },
                "BoundingBox": [
                    {"CRS": "EPSG:2056", "minx": 1.0, "miny": 1.0, "maxx": 1.0, "maxy": 1.0}
                ],
                "Style": [{"Title": {"value": "Default"}, "Name": {"value": "default"}}],
            },
        }
        return capability_config

    def wfs_2_0_0_capabilities_config(self, url: str) -> dict:
        version = "2.0.0"
        wfs_capabilities = {
            "FeatureTypeList": {"FeatureType": []},
            "Filter_Capabilities": {
                "Conformance": {
                    "Constraint": [
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsQuery",
                        },
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsAdHocQuery",
                        },
                        {
                            "DefaultValue": {"value": "FALSE"},
                            "name": "ImplementsFunctions",
                        },
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsResourceId",
                        },
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsMinStandardFilter",
                        },
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsStandardFilter",
                        },
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsMinSpatialFilter",
                        },
                        {
                            "DefaultValue": {"value": "FALSE"},
                            "name": "ImplementsSpatialFilter",
                        },
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsMinTemporalFilter",
                        },
                        {
                            "DefaultValue": {"value": "FALSE"},
                            "name": "ImplementsTemporalFilter",
                        },
                        {
                            "DefaultValue": {"value": "FALSE"},
                            "name": "ImplementsVersionNav",
                        },
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsSorting",
                        },
                        {
                            "DefaultValue": {"value": "FALSE"},
                            "name": "ImplementsExtendedOperators",
                        },
                        {
                            "DefaultValue": {"value": "TRUE"},
                            "name": "ImplementsMinimumXPath",
                        },
                        {
                            "DefaultValue": {"value": "FALSE"},
                            "name": "ImplementsSchemaElementFunc",
                        },
                    ]
                },
                "Id_Capabilities": {"ResourceIdentifier": [{"name": "fes:ResourceId"}]},
                "Scalar_Capabilities": {
                    "ComparisonOperators": {
                        "ComparisonOperator": [
                            {"name": "PropertyIsEqualTo"},
                            {"name": "PropertyIsNotEqualTo"},
                            {"name": "PropertyIsLessThan"},
                            {"name": "PropertyIsGreaterThan"},
                            {"name": "PropertyIsLessThanOrEqualTo"},
                            {"name": "PropertyIsGreaterThanOrEqualTo"},
                            {"name": "PropertyIsLike"},
                            {"name": "PropertyIsBetween"},
                        ]
                    }
                },
                "Spatial_Capabilities": {
                    "GeometryOperands": {
                        "GeometryOperand": [
                            {"name": "gml:Point"},
                            {"name": "gml:MultiPoint"},
                            {"name": "gml:LineString"},
                            {"name": "gml:MultiLineString"},
                            {"name": "gml:Curve"},
                            {"name": "gml:MultiCurve"},
                            {"name": "gml:Polygon"},
                            {"name": "gml:MultiPolygon"},
                            {"name": "gml:Surface"},
                            {"name": "gml:MultiSurface"},
                            {"name": "gml:Box"},
                            {"name": "gml:Envelope"},
                        ]
                    },
                    "SpatialOperators": {
                        "SpatialOperator": [
                            {
                                "GeometryOperands": {
                                    "GeometryOperand": [
                                        {"name": "Equals"},
                                        {"name": "Disjoint"},
                                        {"name": "Touches"},
                                        {"name": "Within"},
                                        {"name": "Overlaps"},
                                        {"name": "Crosses"},
                                        {"name": "Intersects"},
                                        {"name": "Contains"},
                                        {"name": "DWithin"},
                                        {"name": "Beyond"},
                                        {"name": "BBOX"},
                                    ]
                                }
                            }
                        ]
                    },
                },
                "Temporal_Capabilities": {
                    "TemporalOperands": {
                        "TemporalOperand": [
                            {"name": "gml:TimePeriod"},
                            {"name": "gml:TimeInstant"},
                        ]
                    },
                    "TemporalOperators": {"TemporalOperator": [{"name": "During"}]},
                },
            },
            "OperationsMetadata": {
                "Constraint": [
                    {
                        "DefaultValue": {"value": "TRUE"},
                        "name": "ImplementsBasicWFS",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ImplementsTransactionalWFS",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ImplementsLockingWFS",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "KVPEncoding",
                    },
                    {
                        "DefaultValue": {"value": "TRUE"},
                        "name": "XMLEncoding",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "SOAPEncoding",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ImplementsInheritance",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ImplementsRemoteResolve",
                    },
                    {
                        "DefaultValue": {"value": "TRUE"},
                        "name": "ImplementsResultPaging",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ImplementsStandardJoins",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ImplementsSpatialJoins",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ImplementsTemporalJoins",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ImplementsFeatureVersioning",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "ManageStoredQueries",
                    },
                    {
                        "DefaultValue": {"value": "FALSE"},
                        "name": "PagingIsTransactionSafe",
                    },
                    {
                        "AllowedValues": {
                            "Value": [
                                {"value": "wfs:Query"},
                                {"value": "wfs:StoredQuery"},
                            ],
                        },
                        "name": "QueryExpressions",
                    },
                ],
                "Operation": [
                    {
                        "DCP": [
                            {
                                "HTTP": {
                                    "Get": [
                                        {
                                            "href": url,
                                            "type": "simple",
                                        }
                                    ],
                                    "Post": [
                                        {
                                            "href": url,
                                            "type": "simple",
                                        }
                                    ],
                                }
                            }
                        ],
                        "Parameter": [
                            {
                                "AllowedValues": {
                                    "Value": [{"value": version}],
                                },
                                "name": "AcceptVersions",
                            },
                            {
                                "AllowedValues": {
                                    "Value": [{"value": "text/xml"}],
                                },
                                "name": "AcceptFormats",
                            },
                            {
                                "AllowedValues": {
                                    "Value": [
                                        {"value": "ServiceIdentification"},
                                        {"value": "ServiceProvider"},
                                        {"value": "OperationsMetadata"},
                                        {"value": "FeatureTypeList"},
                                        {"value": "Filter_Capabilities"},
                                    ],
                                },
                                "name": "Sections",
                            },
                        ],
                        "name": "GetCapabilities",
                    },
                    {
                        "DCP": [
                            {
                                "HTTP": {
                                    "Get": [
                                        {
                                            "href": url,
                                            "type": "simple",
                                        }
                                    ],
                                    "Post": [
                                        {
                                            "href": url,
                                            "type": "simple",
                                        }
                                    ],
                                }
                            }
                        ],
                        "Parameter": [
                            {
                                "AllowedValues": {
                                    "Value": [
                                        {"value": "application/gml+xml; " "version=3.2"},
                                        {"value": "text/xml; " "subtype=gml/3.2.1"},
                                        {"value": "text/xml; " "subtype=gml/3.1.1"},
                                        {"value": "text/xml; " "subtype=gml/2.1.2"},
                                    ],
                                },
                                "name": "outputFormat",
                            }
                        ],
                        "name": "DescribeFeatureType",
                    },
                    {
                        "DCP": [
                            {
                                "HTTP": {
                                    "Get": [
                                        {
                                            "href": url,
                                            "type": "simple",
                                        }
                                    ],
                                    "Post": [
                                        {
                                            "href": url,
                                            "type": "simple",
                                        }
                                    ],
                                }
                            }
                        ],
                        "Parameter": [
                            {
                                "AllowedValues": {
                                    "Value": [
                                        {"value": "application/gml+xml; " "version=3.2"},
                                        {"value": "text/xml; " "subtype=gml/3.2.1"},
                                        {"value": "text/xml; " "subtype=gml/3.1.1"},
                                        {"value": "text/xml; " "subtype=gml/2.1.2"},
                                    ],
                                },
                                "name": "outputFormat",
                            }
                        ],
                        "name": "GetFeature",
                    },
                    {
                        "DCP": [
                            {
                                "HTTP": {
                                    "Get": [
                                        {
                                            "href": url,
                                            "type": "simple",
                                        }
                                    ],
                                    "Post": [
                                        {
                                            "href": url,
                                            "type": "simple",
                                        }
                                    ],
                                }
                            }
                        ],
                        "Parameter": [
                            {
                                "AllowedValues": {
                                    "Value": [
                                        {"value": "application/gml+xml; " "version=3.2"},
                                        {"value": "text/xml; " "subtype=gml/3.2.1"},
                                        {"value": "text/xml; " "subtype=gml/3.1.1"},
                                        {"value": "text/xml; " "subtype=gml/2.1.2"},
                                    ],
                                },
                                "name": "outputFormat",
                            }
                        ],
                        "name": "GetPropertyValue",
                    },
                ],
                "Parameter": [
                    {
                        "AllowedValues": {"Value": [{"value": version}]},
                        "name": "version",
                    }
                ],
            },
            "ServiceIdentification": {
                "AccessConstraints": [{"value": "None"}],
                "Fees": {"value": "None"},
                "ServiceType": {"codeSpace": "OGC", "value": "WFS"},
                "ServiceTypeVersion": [version],
                "Title": [{"value": "Georama WFS"}],
            },
            "ServiceProvider": {
                "ProviderName": "OPENGIS.ch",
                "ProviderSite": {
                    "href": "https://opengis.ch",
                    "type": "simple",
                },
                "ServiceContact": {
                    "ContactInfo": {
                        "Address": {
                            "AdministrativeArea": "Canton Graubünden",
                            "City": "Laax",
                            "Country": "Switzerland",
                            "DeliveryPoint": ["OPENGIS.ch GmbH", "Via Geinas 2"],
                            "ElectronicMailAddress": ["sales@opengis.ch"],
                            "PostalCode": "7031",
                        },
                        "HoursOfService": "09:00 - 16:00",
                        "OnlineResource": {
                            "href": "https://opengis.ch",
                            "type": "simple",
                        },
                    },
                    "IndividualName": {"value": "Rudert, Clemens"},
                    "PositionName": {"value": "DEV"},
                },
            },
            "version": version,
        }
        return wfs_capabilities

    def wfs_get_metadata_config(self, url: str) -> dict:
        metadata = {
            "language": {"LocalisedCharacterString": {"value": "en-US"}},
            "hierarchyLevel": [
                {
                    "MD_ScopeCode": {
                        "value": "dataset",
                        "codeList": "http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_ScopeCode",
                        "codeListValue": "dataset",
                        "codeSpace": "ISOTC211/19115",
                    }
                }
            ],
            "contact": [
                {
                    "CI_ResponsibleParty": {
                        "id": "contact",
                        "individualName": {
                            "LocalisedCharacterString": {
                                "value": "Fachstelle für Geoinformation"
                            }
                        },
                        "organisationName": {
                            "LocalisedCharacterString": {
                                "value": "Grundbuch- und Vermessungsamt"
                            }
                        },
                        "contactInfo": {
                            "CI_Contact": {
                                "phone": {
                                    "CI_Telephone": {
                                        "voice": [
                                            {
                                                "LocalisedCharacterString": {
                                                    "value": "+41612679953"
                                                }
                                            }
                                        ],
                                    },
                                    "type": "simple",
                                },
                                "address": {
                                    "CI_Address": {
                                        "deliveryPoint": [
                                            {
                                                "LocalisedCharacterString": {
                                                    "value": "Dufourstrasse 40/50, Postfach",
                                                }
                                            }
                                        ],
                                        "city": {
                                            "LocalisedCharacterString": {"value": "Basel"}
                                        },
                                        "administrativeArea": {
                                            "LocalisedCharacterString": {
                                                "value": "Basel-Stadt"
                                            }
                                        },
                                        "postalCode": {
                                            "LocalisedCharacterString": {"value": "4001"}
                                        },
                                        "country": {
                                            "LocalisedCharacterString": {"value": "Schweiz"}
                                        },
                                        "electronicMailAddress": [
                                            {
                                                "LocalisedCharacterString": {
                                                    "value": "geo@bs.ch"
                                                }
                                            }
                                        ],
                                    },
                                    "type": "simple",
                                },
                                "onlineResource": {
                                    "CI_OnlineResource": {
                                        "linkage": {"URL": {"value": "https://wms.geo.bs.ch"}}
                                    },
                                    "type": "simple",
                                },
                            },
                            "type": "simple",
                        },
                        "role": {
                            "CI_RoleCode": {
                                "value": "pointOfContact",
                                "codeList": "http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
                                "codeListValue": "pointOfContact",
                                "codeSpace": "ISOTC211/19115",
                            }
                        },
                    },
                    "type": "simple",
                }
            ],
            "dateStamp": {"nilReason": "missing"},
            "metadataStandardName": {
                "LocalisedCharacterString": {
                    "value": "ISO 19115:2003 - Geographic information - Metadata"
                }
            },
            "metadataStandardVersion": {
                "LocalisedCharacterString": {
                    "value": "ISO 19115:2003",
                }
            },
            "distributionInfo": {
                "MD_Distribution": {
                    "distributor": [
                        {
                            "MD_Distributor": {
                                "distributorContact": {
                                    "CI_ResponsibleParty": {
                                        "id": "contact",
                                        "individualName": {
                                            "LocalisedCharacterString": {
                                                "value": "Fachstelle für Geoinformation"
                                            }
                                        },
                                        "organisationName": {
                                            "LocalisedCharacterString": {
                                                "value": "Grundbuch- und Vermessungsamt"
                                            }
                                        },
                                        "contactInfo": {
                                            "CI_Contact": {
                                                "phone": {
                                                    "CI_Telephone": {
                                                        "voice": [
                                                            {
                                                                "LocalisedCharacterString": {
                                                                    "value": "+41612679953",
                                                                }
                                                            }
                                                        ],
                                                        "facsimile": [],
                                                    },
                                                    "type": "simple",
                                                },
                                                "address": {
                                                    "CI_Address": {
                                                        "deliveryPoint": [
                                                            {
                                                                "LocalisedCharacterString": {
                                                                    "value": "Dufourstrasse 40/50, Postfach",
                                                                }
                                                            }
                                                        ],
                                                        "city": {
                                                            "LocalisedCharacterString": {
                                                                "value": "Basel",
                                                            },
                                                        },
                                                        "administrativeArea": {
                                                            "LocalisedCharacterString": {
                                                                "value": "Basel-Stadt",
                                                            }
                                                        },
                                                        "postalCode": {
                                                            "LocalisedCharacterString": {
                                                                "value": "4001",
                                                            },
                                                        },
                                                        "country": {
                                                            "LocalisedCharacterString": {
                                                                "value": "Schweiz",
                                                            },
                                                        },
                                                        "electronicMailAddress": [
                                                            {
                                                                "LocalisedCharacterString": {
                                                                    "value": "geo@bs.ch",
                                                                },
                                                            }
                                                        ],
                                                    },
                                                    "type": "simple",
                                                },
                                                "onlineResource": {
                                                    "CI_OnlineResource": {
                                                        "linkage": {
                                                            "URL": {
                                                                "value": "https://wms.geo.bs.ch"
                                                            },
                                                        },
                                                    },
                                                    "type": "simple",
                                                },
                                            },
                                            "type": "simple",
                                        },
                                        "role": {
                                            "CI_RoleCode": {
                                                "value": "pointOfContact",
                                                "codeList": "http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
                                                "codeListValue": "pointOfContact",
                                                "codeSpace": "ISOTC211/19115",
                                            },
                                        },
                                    },
                                    "type": "simple",
                                },
                            },
                            "type": "simple",
                        }
                    ],
                    "transferOptions": [
                        {
                            "MD_DigitalTransferOptions": {
                                "unitsOfDistribution": {
                                    "LocalisedCharacterString": {
                                        "value": "KB",
                                    },
                                },
                            },
                            "type": "simple",
                        }
                    ],
                },
                "type": "simple",
            },
        }
        return metadata
