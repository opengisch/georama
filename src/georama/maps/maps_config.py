from xml.etree.ElementTree import QName

from django.conf import settings

import georama.maps.interfaces.ogc.wms_1_3_0.capabilities as wms130_capabilities
from georama.maps.interfaces.ogc import wfs_2_0_0


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

    def wms_1_3_0_service_config(self, url: str) -> wms130_capabilities.Service:
        service_config = wms130_capabilities.Service(
            name=wms130_capabilities.ServiceName.WMS,
            title=wms130_capabilities.Title(value="QGIS Server light WMS"),
            abstract=wms130_capabilities.Abstract(value="This is the new approach."),
            keyword_list=wms130_capabilities.KeywordList(
                keyword=[
                    wms130_capabilities.Keyword(value="fast", vocabulary="ISO"),
                    wms130_capabilities.Keyword(
                        value="infoMapAccessService", vocabulary="ISO"
                    ),
                ]
            ),
            contact_information=wms130_capabilities.ContactInformation(
                contact_person_primary=wms130_capabilities.ContactPersonPrimary(
                    contact_person=wms130_capabilities.ContactPerson(value="Clemens Rudert"),
                    contact_organization=wms130_capabilities.ContactOrganization(
                        value="OPENGIS.ch"
                    ),
                ),
                contact_position=None,
                contact_address=wms130_capabilities.ContactAddress(
                    address=wms130_capabilities.Address(value="Via Geinas 2"),
                    city=wms130_capabilities.City(value="Laax"),
                    state_or_province=wms130_capabilities.StateOrProvince(
                        value="Canton Graubünden"
                    ),
                    post_code=wms130_capabilities.PostCode(value="7031"),
                    country=wms130_capabilities.Country(value="Switzerland"),
                ),
                contact_electronic_mail_address=wms130_capabilities.ContactElectronicMailAddress(
                    value="sales@opengis.ch"
                ),
            ),
            online_resource=wms130_capabilities.OnlineResource(href=url),
            fees=wms130_capabilities.Fees(value="its for free"),
            access_constraints=wms130_capabilities.AccessConstraints(value="None"),
        )
        return service_config

    def wms_1_3_0_capability_config(self, url: str) -> wms130_capabilities.Capability:
        capability_config = wms130_capabilities.Capability(
            request=wms130_capabilities.Request(
                get_capabilities=wms130_capabilities.GetCapabilities(
                    format=[
                        wms130_capabilities.Format(value="text/xml"),
                        wms130_capabilities.Format(value="application/json"),
                    ],
                    dcptype=[
                        wms130_capabilities.Dcptype(
                            http=wms130_capabilities.Http(
                                get=wms130_capabilities.Get(
                                    online_resource=wms130_capabilities.OnlineResource(
                                        href=url
                                    )
                                )
                            )
                        )
                    ],
                ),
                get_map=wms130_capabilities.GetMap(
                    format=[wms130_capabilities.Format(value=self.default_format)],
                    dcptype=[
                        wms130_capabilities.Dcptype(
                            http=wms130_capabilities.Http(
                                get=wms130_capabilities.Get(
                                    online_resource=wms130_capabilities.OnlineResource(
                                        href=url
                                    )
                                )
                            )
                        )
                    ],
                ),
            ),
            exception=wms130_capabilities.Exception(
                format=[wms130_capabilities.Format(value="text/xml")]
            ),
            layer=wms130_capabilities.Layer(
                queryable=0,
                opaque=0,
                no_subsets=0,
                cascaded=0,
                name=wms130_capabilities.Name(value="qgis_server_light"),
                title=wms130_capabilities.Title(value="QGIS Server light"),
                abstract=wms130_capabilities.Abstract(
                    value="The lightning fast and scalable access to your raster data."
                ),
                keyword_list=wms130_capabilities.KeywordList(
                    keyword=[
                        wms130_capabilities.Keyword(value="fast", vocabulary="ISO"),
                        wms130_capabilities.Keyword(
                            value="infoMapAccessService", vocabulary="ISO"
                        ),
                    ]
                ),
                crs=[
                    wms130_capabilities.Crs(value="EPSG:2056"),
                    wms130_capabilities.Crs(value="CRS:84"),
                ],
                ex_geographic_bounding_box=wms130_capabilities.ExGeographicBoundingBox(
                    west_bound_longitude=180.0,
                    east_bound_longitude=-180,
                    south_bound_latitude=-90.0,
                    north_bound_latitude=90.0,
                ),
                bounding_box=[
                    wms130_capabilities.BoundingBox(
                        crs="EPSG:2056",
                        minx=1.0,
                        miny=1.0,
                        maxx=1.0,
                        maxy=1.0,
                    )
                ],
                style=[
                    wms130_capabilities.Style(
                        name=wms130_capabilities.Name(value="default"),
                        title=wms130_capabilities.Title(value="default"),
                    )
                ],
            ),
        )
        return capability_config

    def wfs_2_0_0_capabilities_config(self, url: str) -> wfs_2_0_0.WfsCapabilities:
        version = "2.0.0"
        wfs_capabilities = wfs_2_0_0.WfsCapabilities(
            feature_type_list=wfs_2_0_0.FeatureTypeList(feature_type=[]),
            filter_capabilities=wfs_2_0_0.FilterCapabilities(
                conformance=wfs_2_0_0.ConformanceType(
                    constraint=[
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsQuery",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsAdHocQuery",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsFunctions",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsResourceId",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsMinStandardFilter",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsStandardFilter",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsMinSpatialFilter",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsSpatialFilter",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                            name="ImplementsMinTemporalFilter",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                            name="ImplementsTemporalFilter",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                            name="ImplementsVersionNav",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsSorting",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                            name="ImplementsExtendedOperators",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                            name="ImplementsMinimumXPath",
                        ),
                        wfs_2_0_0.DomainType(
                            default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                            name="ImplementsSchemaElementFunc",
                        ),
                    ]
                ),
                id_capabilities=wfs_2_0_0.IdCapabilitiesType(
                    resource_identifier=[
                        wfs_2_0_0.ResourceIdentifierType(
                            name=QName(text_or_uri="fes:ResourceId"),
                        )
                    ]
                ),
                scalar_capabilities=wfs_2_0_0.ScalarCapabilitiesType(
                    comparison_operators=wfs_2_0_0.ComparisonOperatorsType(
                        comparison_operator=[
                            wfs_2_0_0.ComparisonOperatorType(
                                name="PropertyIsEqualTo",
                            ),
                            wfs_2_0_0.ComparisonOperatorType(
                                name="PropertyIsNotEqualTo",
                            ),
                            wfs_2_0_0.ComparisonOperatorType(
                                name="PropertyIsLessThan",
                            ),
                            wfs_2_0_0.ComparisonOperatorType(
                                name="PropertyIsGreaterThan",
                            ),
                            wfs_2_0_0.ComparisonOperatorType(
                                name="PropertyIsLessThanOrEqualTo",
                            ),
                            wfs_2_0_0.ComparisonOperatorType(
                                name="PropertyIsGreaterThanOrEqualTo",
                            ),
                            wfs_2_0_0.ComparisonOperatorType(
                                name="PropertyIsLike",
                            ),
                            wfs_2_0_0.ComparisonOperatorType(
                                name="PropertyIsBetween",
                            ),
                        ]
                    )
                ),
                spatial_capabilities=wfs_2_0_0.SpatialCapabilitiesType(
                    geometry_operands=wfs_2_0_0.GeometryOperandsType(
                        geometry_operand=[
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:Point"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:MultiPoint"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:LineString"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:MultiLineString"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:Curve"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:MultiCurve"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:Polygon"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:MultiPolygon"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:Surface"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:MultiSurface"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:Box"),
                            ),
                            wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                name=QName(text_or_uri="gml:Envelope"),
                            ),
                        ]
                    ),
                    spatial_operators=wfs_2_0_0.SpatialOperatorsType(
                        spatial_operator=[
                            wfs_2_0_0.SpatialOperatorType(
                                geometry_operands=wfs_2_0_0.GeometryOperandsType(
                                    geometry_operand=[
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Equals"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Disjoint"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Touches"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Within"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Overlaps"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Crosses"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Intersects"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Contains"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="DWithin"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="Beyond"),
                                        ),
                                        wfs_2_0_0.GeometryOperandsTypeGeometryOperand(
                                            name=QName(text_or_uri="BBOX"),
                                        ),
                                    ]
                                )
                            )
                        ]
                    ),
                ),
                temporal_capabilities=wfs_2_0_0.TemporalCapabilitiesType(
                    temporal_operands=wfs_2_0_0.TemporalOperandsType(
                        temporal_operand=[
                            wfs_2_0_0.TemporalOperandsTypeTemporalOperand(
                                name=QName(text_or_uri="gml:TimePeriod"),
                            ),
                            wfs_2_0_0.TemporalOperandsTypeTemporalOperand(
                                name=QName(text_or_uri="gml:TimeInstant"),
                            ),
                        ]
                    ),
                    temporal_operators=wfs_2_0_0.TemporalOperatorsType(
                        temporal_operator=[
                            wfs_2_0_0.TemporalOperatorType(
                                temporal_operands=wfs_2_0_0.TemporalOperandsType(
                                    temporal_operand=[
                                        wfs_2_0_0.TemporalOperandsTypeTemporalOperand(
                                            name=QName(text_or_uri="During"),
                                        )
                                    ]
                                )
                            )
                        ]
                    ),
                ),
            ),
            operations_metadata=wfs_2_0_0.OperationsMetadata(
                constraint=[
                    wfs_2_0_0.DomainType(
                        name="ImplementsBasicWFS",
                        default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsTransactionalWFS",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsLockingWFS",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="KVPEncoding", default_value=wfs_2_0_0.DefaultValue(value="FALSE")
                    ),
                    wfs_2_0_0.DomainType(
                        name="XMLEncoding", default_value=wfs_2_0_0.DefaultValue(value="TRUE")
                    ),
                    wfs_2_0_0.DomainType(
                        name="SOAPEncoding",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsInheritance",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsRemoteResolve",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsResultPaging",
                        default_value=wfs_2_0_0.DefaultValue(value="TRUE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsStandardJoins",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsSpatialJoins",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsTemporalJoins",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ImplementsFeatureVersioning",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="ManageStoredQueries",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="PagingIsTransactionSafe",
                        default_value=wfs_2_0_0.DefaultValue(value="FALSE"),
                    ),
                    wfs_2_0_0.DomainType(
                        name="QueryExpressions",
                        choice=wfs_2_0_0.AllowedValues(
                            value_or_range=[
                                wfs_2_0_0.Value1(value="wfs:Query"),
                                wfs_2_0_0.Value1(value="wfs:StoredQuery"),
                            ]
                        ),
                    ),
                ],
                operation=[
                    wfs_2_0_0.Operation(
                        name="GetCapabilities",
                        dcp=[
                            wfs_2_0_0.Dcp(
                                http=wfs_2_0_0.Http(
                                    get_or_post=[
                                        wfs_2_0_0.Get(href=url),
                                        wfs_2_0_0.Post(href=url),
                                    ]
                                )
                            )
                        ],
                        parameter=[
                            wfs_2_0_0.DomainType(
                                name="AcceptVersions",
                                choice=wfs_2_0_0.AllowedValues(
                                    value_or_range=[wfs_2_0_0.Value1(value=version)]
                                ),
                            ),
                            wfs_2_0_0.DomainType(
                                name="AcceptFormats",
                                choice=wfs_2_0_0.AllowedValues(
                                    value_or_range=[wfs_2_0_0.Value1(value="text/xml")]
                                ),
                            ),
                            wfs_2_0_0.DomainType(
                                name="Sections",
                                choice=wfs_2_0_0.AllowedValues(
                                    value_or_range=[
                                        wfs_2_0_0.Value1(value="ServiceIdentification"),
                                        wfs_2_0_0.Value1(value="ServiceProvider"),
                                        wfs_2_0_0.Value1(value="OperationsMetadata"),
                                        wfs_2_0_0.Value1(value="FeatureTypeList"),
                                        wfs_2_0_0.Value1(value="Filter_Capabilities"),
                                    ]
                                ),
                            ),
                        ],
                    ),
                    wfs_2_0_0.Operation(
                        name="DescribeFeatureType",
                        dcp=[
                            wfs_2_0_0.Dcp(
                                http=wfs_2_0_0.Http(
                                    get_or_post=[
                                        wfs_2_0_0.Get(href=url),
                                        wfs_2_0_0.Post(href=url),
                                    ]
                                )
                            )
                        ],
                        parameter=[
                            wfs_2_0_0.DomainType(
                                name="outputFormat",
                                choice=wfs_2_0_0.AllowedValues(
                                    value_or_range=[
                                        wfs_2_0_0.Value1(
                                            value="application/gml+xml; version=3.2"
                                        ),
                                        wfs_2_0_0.Value1(value="text/xml; subtype=gml/3.2.1"),
                                        wfs_2_0_0.Value1(value="text/json"),
                                    ]
                                ),
                            )
                        ],
                    ),
                    wfs_2_0_0.Operation(
                        name="GetFeature",
                        dcp=[
                            wfs_2_0_0.Dcp(
                                http=wfs_2_0_0.Http(
                                    get_or_post=[
                                        wfs_2_0_0.Get(href=url),
                                        wfs_2_0_0.Post(href=url),
                                    ]
                                )
                            )
                        ],
                        parameter=[
                            wfs_2_0_0.DomainType(
                                name="outputFormat",
                                choice=wfs_2_0_0.AllowedValues(
                                    value_or_range=[
                                        wfs_2_0_0.Value1(
                                            value="application/gml+xml; version=3.2"
                                        ),
                                        wfs_2_0_0.Value1(value="text/xml; subtype=gml/3.2.1"),
                                        wfs_2_0_0.Value1(value="text/json"),
                                    ]
                                ),
                            )
                        ],
                    ),
                    wfs_2_0_0.Operation(
                        name="GetPropertyValue",
                        dcp=[
                            wfs_2_0_0.Dcp(
                                http=wfs_2_0_0.Http(
                                    get_or_post=[
                                        wfs_2_0_0.Get(href=url),
                                        wfs_2_0_0.Post(href=url),
                                    ]
                                )
                            )
                        ],
                        parameter=[
                            wfs_2_0_0.DomainType(
                                name="outputFormat",
                                choice=wfs_2_0_0.AllowedValues(
                                    value_or_range=[
                                        wfs_2_0_0.Value1(
                                            value="application/gml+xml; version=3.2"
                                        ),
                                        wfs_2_0_0.Value1(value="text/xml; subtype=gml/3.2.1"),
                                        wfs_2_0_0.Value1(value="text/json"),
                                    ]
                                ),
                            )
                        ],
                    ),
                ],
                parameter=[
                    wfs_2_0_0.DomainType(
                        name="version",
                        choice=wfs_2_0_0.AllowedValues(
                            value_or_range=[wfs_2_0_0.Value1(value=version)]
                        ),
                    )
                ],
            ),
            service_identification=wfs_2_0_0.ServiceIdentification(
                title=[
                    wfs_2_0_0.Title1(
                        value="QGIS Server light WFS",
                    )
                ],
                abstract=[wfs_2_0_0.Abstract1(value="This is the new approach.")],
                keywords=[
                    wfs_2_0_0.Keywords(
                        keyword=[
                            wfs_2_0_0.LanguageStringType(value="fast", lang="en"),
                            wfs_2_0_0.LanguageStringType(value="scalable", lang="en"),
                        ]
                    )
                ],
                service_type=wfs_2_0_0.CodeType(value="WFS", code_space="OGC"),
                service_type_version=[version],
                fees=wfs_2_0_0.Fees(value="None"),
                access_constraints=[wfs_2_0_0.AccessConstraints(value="None")],
            ),
            service_provider=wfs_2_0_0.ServiceProvider(
                provider_name="OPENGIS.ch",
                provider_site=wfs_2_0_0.OnlineResourceType(href="https://opengis.ch"),
                service_contact=wfs_2_0_0.ResponsiblePartySubsetType(
                    contact_info=wfs_2_0_0.ContactInfo(
                        address=wfs_2_0_0.AddressType(
                            administrative_area="Canton Graubünden",
                            city="Laax",
                            country="Switzerland",
                            delivery_point=["OPENGIS.ch GmbH", "Via Geinas 2"],
                            electronic_mail_address=["sales@opengis.ch"],
                            postal_code="7031",
                        ),
                        hours_of_service="09:00 - 16:00",
                        online_resource=wfs_2_0_0.OnlineResourceType(
                            href="https://opengis.ch"
                        ),
                    ),
                    individual_name=wfs_2_0_0.IndividualName(
                        value="Rudert, Clemens",
                    ),
                    position_name=wfs_2_0_0.PositionName(
                        value="DEV",
                    ),
                ),
            ),
            version=version,
        )
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
                                                                    "value": "Dufourstrasse 40/50, Postfach",  # noqa: E501
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
