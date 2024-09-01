import json

from django.http import HttpRequest

from georama.rasteroctopus.interfaces.ogc.wms_1_3_0.capabilities import ServiceName
from georama.rasteroctopus.interfaces.ogc.wms_1_3_0.capabilities.xlink import TypeType


class Config:

    @property
    def redis_url(self):
        return "redis://localhost:1234"

    @property
    def default_dpi(self) -> int:
        return 96

    @property
    def default_format(self) -> str:
        return "image/png"

    def service_config(self, url: str) -> str:
        service_config = {
            "Name": ServiceName.WMS.value,
            "Title": {
                "value": "QGIS Server light"
            },
            "Abstract": {
                "value": "this is the new approach"
            },
            "KeywordList": {
                "Keyword": [{
                    "value": "fast",
                    "vocabulary": "ISO"
                }, {
                    "value": "infoMapAccessService",
                    "vocabulary": "ISO"
                }]
            },
            "ContactInformation": {
                "ContactPersonPrimary": {
                    "ContactPerson": {
                        "value": "Clemens Rudert"
                    },
                    "ContactOrganization": {
                        "value": "OPENGIS.ch"
                    }
                },
                "ContactPosition": {},
                "ContactAddress": {
                    "Address": {
                        "value": "Via Geinas 2"
                    },
                    "City": {
                        "value": "Laax"
                    },
                    "StateOrProvince": {
                        "value": "Canton Graubünden"
                    },
                    "PostCode": {
                        "value": "7031"
                    },
                    "Country": {
                        "value": "Switzerland"
                    }
                },
                "ContactElectronicMailAddress": {
                    "value": "sales@opengis.ch"
                },

            },
            "OnlineResource": {
                "type": TypeType.SIMPLE.value,
                "href": url
            },
            "Fees": {
                "value": "its for free"
            },
            "AccessConstraints": {
                "value": "None"
            }

        }
        return json.dumps(service_config)

    def capability_config(self, url: str) -> str:
        capability_config = {
            "Request": {
                "GetCapabilities": {
                    "Format": [{
                        "value": "text/xml"
                    }, {
                        "value": "application/json"
                    }],
                    "DCPType": [{
                        "HTTP": {
                            "Get": {
                                "OnlineResource": {
                                    "type": TypeType.SIMPLE.value,
                                    "href": url
                                }
                            }
                        }
                    }]
                },
                "GetMap": {
                    "Format": [{
                        "value": self.default_format
                    }],
                    "DCPType": [{
                        "HTTP": {
                            "Get": {
                                "OnlineResource": {
                                    "type": TypeType.SIMPLE.value,
                                    "href": url
                                }
                            }
                        }
                    }]
                }
            },
            "Exception": {
                "Format": [{
                    "value": "text/xml"
                }]
            },
            "Layer": {
                "queryable": False,
                "cascaded": 0,
                "Name": "qgis_server_light",
                "Title": {
                    "value": "QGIS Server light"
                },
                "Abstract": {
                    "value": "The lightning fast access to your raster data"
                },
                "KeywordList": {
                    "Keyword": [{
                        "value": "fast",
                        "vocabulary": "ISO"
                    }, {
                        "value": "infoMapAccessService",
                        "vocabulary": "ISO"
                    }]
                },
                "CRS": [{
                    "value": "EPSG:2056"
                }, {
                    "value": "CRS:84"
                }],
                "EX_GeographicBoundingBox": {
                    "westBoundLongitude": 180.0,
                    "eastBoundLongitude": -180.0,
                    "southBoundLatitude": -90.0,
                    "northBoundLatitude": 90.0
                },
                "BoundingBox": [{
                    "CRS": "EPSG:2056",
                    "minx": 1.0,
                    "miny": 1.0,
                    "maxx": 1.0,
                    "maxy": 1.0
                }],
                "Style": [{
                    "Title": {
                        "value": "Default"
                    },
                    "Name": {
                        "value": "default"
                    }
                }]
            }

        }
        return json.dumps(capability_config)
