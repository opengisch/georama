import os

from georama.maps.interfaces.ogc.wms_1_3_0.capabilities import ServiceName
from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.xlink import TypeType


class Config:
    @property
    def redis_url(self):
        return os.environ.get("QSL_REDIS_URL", "redis://localhost:1234")

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
        return float(os.environ.get("JOB_TIMEOUT", 1000))

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
                "queryable": False,
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
        wfs_capabilities = {
            "FeatureTypeList": {"FeatureType": []},
            "Filter_Capabilities": {
                "Conformance": {
                    "Constraint": [
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsQuery",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsAdHocQuery",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "FALSE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsFunctions",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsResourceId",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsMinStandardFilter",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsStandardFilter",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsMinSpatialFilter",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "FALSE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsSpatialFilter",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsMinTemporalFilter",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "FALSE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsTemporalFilter",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "FALSE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsVersionNav",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsSorting",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "FALSE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsExtendedOperators",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "TRUE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsMinimumXPath",
                        },
                        {
                            "AllowedValues": None,
                            "AnyValue": None,
                            "DataType": None,
                            "DefaultValue": {"value": "FALSE"},
                            "Meaning": None,
                            "Metadata": [],
                            "NoValues": None,
                            "ReferenceSystem": None,
                            "UOM": None,
                            "ValuesReference": None,
                            "name": "ImplementsSchemaElementFunc",
                        },
                    ]
                },
                "Extended_Capabilities": None,
                "Functions": None,
                "Id_Capabilities": {
                    "ResourceIdentifier": [{"Metadata": None, "name": "fes:ResourceId"}]
                },
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
                    },
                    "LogicalOperators": None,
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
                                },
                                "name": None,
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
                    "TemporalOperators": {
                        "TemporalOperator": [{"TemporalOperands": None, "name": "During"}]
                    },
                },
            },
            "OperationsMetadata": {
                "Constraint": [
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "TRUE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsBasicWFS",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsTransactionalWFS",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsLockingWFS",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "KVPEncoding",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "TRUE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "XMLEncoding",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "SOAPEncoding",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsInheritance",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsRemoteResolve",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "TRUE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsResultPaging",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsStandardJoins",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsSpatialJoins",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsTemporalJoins",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ImplementsFeatureVersioning",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "ManageStoredQueries",
                    },
                    {
                        "AllowedValues": None,
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": {"value": "FALSE"},
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "PagingIsTransactionSafe",
                    },
                    {
                        "AllowedValues": {
                            "Range": [],
                            "Value": [
                                {"any_element": "wfs:Query"},
                                {"any_element": "wfs:StoredQuery"},
                            ],
                        },
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": None,
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "QueryExpressions",
                    },
                ],
                "ExtendedCapabilities": None,
                "Operation": [
                    {
                        "Constraint": [],
                        "DCP": [
                            {
                                "HTTP": {
                                    "Get": [
                                        {
                                            "Constraint": [],
                                            "actuate": None,
                                            "arcrole": None,
                                            "href": url,
                                            "role": None,
                                            "show": None,
                                            "title": None,
                                            "type": "simple",
                                        }
                                    ],
                                    "Post": [
                                        {
                                            "Constraint": [],
                                            "actuate": None,
                                            "arcrole": None,
                                            "href": url,
                                            "role": None,
                                            "show": None,
                                            "title": None,
                                            "type": "simple",
                                        }
                                    ],
                                }
                            }
                        ],
                        "Metadata": [],
                        "Parameter": [
                            {
                                "AllowedValues": {
                                    "Range": [],
                                    "Value": [{"any_element": "2.0.0"}],
                                },
                                "AnyValue": None,
                                "DataType": None,
                                "DefaultValue": None,
                                "Meaning": None,
                                "Metadata": [],
                                "NoValues": None,
                                "ReferenceSystem": None,
                                "UOM": None,
                                "ValuesReference": None,
                                "name": "AcceptVersions",
                            },
                            {
                                "AllowedValues": {
                                    "Range": [],
                                    "Value": [{"any_element": "text/xml"}],
                                },
                                "AnyValue": None,
                                "DataType": None,
                                "DefaultValue": None,
                                "Meaning": None,
                                "Metadata": [],
                                "NoValues": None,
                                "ReferenceSystem": None,
                                "UOM": None,
                                "ValuesReference": None,
                                "name": "AcceptFormats",
                            },
                            {
                                "AllowedValues": {
                                    "Range": [],
                                    "Value": [
                                        {"any_element": "ServiceIdentification"},
                                        {"any_element": "ServiceProvider"},
                                        {"any_element": "OperationsMetadata"},
                                        {"any_element": "FeatureTypeList"},
                                        {"any_element": "Filter_Capabilities"},
                                    ],
                                },
                                "AnyValue": None,
                                "DataType": None,
                                "DefaultValue": None,
                                "Meaning": None,
                                "Metadata": [],
                                "NoValues": None,
                                "ReferenceSystem": None,
                                "UOM": None,
                                "ValuesReference": None,
                                "name": "Sections",
                            },
                        ],
                        "name": "GetCapabilities",
                    },
                    {
                        "Constraint": [],
                        "DCP": [
                            {
                                "HTTP": {
                                    "Get": [
                                        {
                                            "Constraint": [],
                                            "actuate": None,
                                            "arcrole": None,
                                            "href": url,
                                            "role": None,
                                            "show": None,
                                            "title": None,
                                            "type": "simple",
                                        }
                                    ],
                                    "Post": [
                                        {
                                            "Constraint": [],
                                            "actuate": None,
                                            "arcrole": None,
                                            "href": url,
                                            "role": None,
                                            "show": None,
                                            "title": None,
                                            "type": "simple",
                                        }
                                    ],
                                }
                            }
                        ],
                        "Metadata": [],
                        "Parameter": [
                            {
                                "AllowedValues": {
                                    "Range": [],
                                    "Value": [
                                        {"any_element": "application/gml+xml; " "version=3.2"},
                                        {"any_element": "text/xml; " "subtype=gml/3.2.1"},
                                        {"any_element": "text/xml; " "subtype=gml/3.1.1"},
                                        {"any_element": "text/xml; " "subtype=gml/2.1.2"},
                                    ],
                                },
                                "AnyValue": None,
                                "DataType": None,
                                "DefaultValue": None,
                                "Meaning": None,
                                "Metadata": [],
                                "NoValues": None,
                                "ReferenceSystem": None,
                                "UOM": None,
                                "ValuesReference": None,
                                "name": "outputFormat",
                            }
                        ],
                        "name": "DescribeFeatureType",
                    },
                    {
                        "Constraint": [],
                        "DCP": [
                            {
                                "HTTP": {
                                    "Get": [
                                        {
                                            "Constraint": [],
                                            "actuate": None,
                                            "arcrole": None,
                                            "href": url,
                                            "role": None,
                                            "show": None,
                                            "title": None,
                                            "type": "simple",
                                        }
                                    ],
                                    "Post": [
                                        {
                                            "Constraint": [],
                                            "actuate": None,
                                            "arcrole": None,
                                            "href": url,
                                            "role": None,
                                            "show": None,
                                            "title": None,
                                            "type": "simple",
                                        }
                                    ],
                                }
                            }
                        ],
                        "Metadata": [],
                        "Parameter": [
                            {
                                "AllowedValues": {
                                    "Range": [],
                                    "Value": [
                                        {"any_element": "application/gml+xml; " "version=3.2"},
                                        {"any_element": "text/xml; " "subtype=gml/3.2.1"},
                                        {"any_element": "text/xml; " "subtype=gml/3.1.1"},
                                        {"any_element": "text/xml; " "subtype=gml/2.1.2"},
                                    ],
                                },
                                "AnyValue": None,
                                "DataType": None,
                                "DefaultValue": None,
                                "Meaning": None,
                                "Metadata": [],
                                "NoValues": None,
                                "ReferenceSystem": None,
                                "UOM": None,
                                "ValuesReference": None,
                                "name": "outputFormat",
                            }
                        ],
                        "name": "GetFeature",
                    },
                    {
                        "Constraint": [],
                        "DCP": [
                            {
                                "HTTP": {
                                    "Get": [
                                        {
                                            "Constraint": [],
                                            "actuate": None,
                                            "arcrole": None,
                                            "href": url,
                                            "role": None,
                                            "show": None,
                                            "title": None,
                                            "type": "simple",
                                        }
                                    ],
                                    "Post": [
                                        {
                                            "Constraint": [],
                                            "actuate": None,
                                            "arcrole": None,
                                            "href": url,
                                            "role": None,
                                            "show": None,
                                            "title": None,
                                            "type": "simple",
                                        }
                                    ],
                                }
                            }
                        ],
                        "Metadata": [],
                        "Parameter": [
                            {
                                "AllowedValues": {
                                    "Range": [],
                                    "Value": [
                                        {"any_element": "application/gml+xml; " "version=3.2"},
                                        {"any_element": "text/xml; " "subtype=gml/3.2.1"},
                                        {"any_element": "text/xml; " "subtype=gml/3.1.1"},
                                        {"any_element": "text/xml; " "subtype=gml/2.1.2"},
                                    ],
                                },
                                "AnyValue": None,
                                "DataType": None,
                                "DefaultValue": None,
                                "Meaning": None,
                                "Metadata": [],
                                "NoValues": None,
                                "ReferenceSystem": None,
                                "UOM": None,
                                "ValuesReference": None,
                                "name": "outputFormat",
                            }
                        ],
                        "name": "GetPropertyValue",
                    },
                ],
                "Parameter": [
                    {
                        "AllowedValues": {"Range": [], "Value": [{"any_element": "2.0.0"}]},
                        "AnyValue": None,
                        "DataType": None,
                        "DefaultValue": None,
                        "Meaning": None,
                        "Metadata": [],
                        "NoValues": None,
                        "ReferenceSystem": None,
                        "UOM": None,
                        "ValuesReference": None,
                        "name": "version",
                    }
                ],
            },
            "ServiceIdentification": {
                "Abstract": [],
                "AccessConstraints": [{"value": "None"}],
                "Fees": {"value": "None"},
                "Keywords": [],
                "Profile": [],
                "ServiceType": {"codeSpace": "OGC", "value": "WFS"},
                "ServiceTypeVersion": ["2.0.0"],
                "Title": [{"lang": None, "value": "Georama WFS"}],
            },
            "ServiceProvider": {
                "ProviderName": "OPENGIS.ch",
                "ProviderSite": {
                    "actuate": None,
                    "arcrole": None,
                    "href": "https://opengis.ch",
                    "role": None,
                    "show": None,
                    "title": None,
                    "type": "simple",
                },
                "ServiceContact": {
                    "ContactInfo": {
                        "Address": {
                            "AdministrativeArea": "Canton " "Graubünden",
                            "City": "Laax",
                            "Country": "Switzerland",
                            "DeliveryPoint": ["OPENGIS.ch " "GmbH", "Via " "Geinas " "2"],
                            "ElectronicMailAddress": ["sales@opengis.ch"],
                            "PostalCode": "7031",
                        },
                        "ContactInstructions": None,
                        "HoursOfService": None,
                        "OnlineResource": None,
                        "Phone": None,
                    },
                    "IndividualName": {"value": "Rudert, Clemens"},
                    "PositionName": {"value": "DEV"},
                    "Role": None,
                },
            },
            "WSDL": None,
            "updateSequence": None,
            "version": "2.0.0",
        }
        return wfs_capabilities
