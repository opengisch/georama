import logging
from decimal import Decimal
from typing import List

from qgis_server_light.interface.qgis import BBox
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from georama.data_integration.models import VectorDataSet
from georama.maps.admin import PublishedAsWmsAdmin
from georama.maps.interfaces.iso.tc211.gmd.dataclasses import (
    CharacterStringPropertyType,
    CiAddress,
    CiAddressPropertyType,
    CiCitation,
    CiCitationPropertyType,
    CiContact,
    CiContactPropertyType,
    CiOnlineResource,
    CiOnlineResourcePropertyType,
    CiResponsibleParty,
    CiResponsiblePartyPropertyType,
    CiRoleCode,
    CiRoleCodePropertyType,
    CiTelephone,
    CiTelephonePropertyType,
    DatePropertyType,
    DecimalPropertyType,
    DecimalType,
    ExExtent,
    ExExtentPropertyType,
    ExGeographicBoundingBox,
    ExGeographicExtentPropertyType,
    LocalisedCharacterString,
    MdDataIdentification,
    MdDigitalTransferOptions,
    MdDigitalTransferOptionsPropertyType,
    MdDistribution,
    MdDistributionPropertyType,
    MdDistributor,
    MdDistributorPropertyType,
    MdGeometricObjects,
    MdGeometricObjectsPropertyType,
    MdGeometricObjectTypeCode,
    MdGeometricObjectTypeCodePropertyType,
    MdIdentificationPropertyType,
    MdMetadata,
    MdReferenceSystem,
    MdReferenceSystemPropertyType,
    MdScopeCode,
    MdScopeCodePropertyType,
    MdSpatialRepresentationPropertyType,
    MdTopologyLevelCode,
    MdTopologyLevelCodePropertyType,
    MdVectorSpatialRepresentation,
    RsIdentifier,
    RsIdentifierPropertyType,
    Url,
    UrlPropertyType,
)
from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WfsGetMetadata(OgcOperation):
    @property
    def allowed_formats(self) -> List[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]

    def obtain_accessible_layers(
        self, layer_names: List[str] | None = None
    ) -> List[PublishedAsWms]:
        accessible_layers = []
        published_as = PublishedAsWms.objects.get(name=layer_names[0])
        if published_as.has_read_permission(self.user, self.appname):
            if isinstance(published_as.vector_dataset, VectorDataSet):
                accessible_layers.append(published_as)
            else:
                logging.debug(
                    "linked dataset has to be VectorDataSet for WFS 2.0.0, all others are ignored!"
                )
        return accessible_layers

    def get_metadata(self, layer_name: str, language: str) -> MdMetadata:
        """
        Attibutes:
            layer_name: name of WMS/WFS Layer
            language: in the form `en-US`
            layer_geometry_type: `complex`|`composite`|`curve`|`point`|`solid`|`surface`
        """
        found_layer = self.obtain_accessible_layers([layer_name])[0]
        wms_link_png = f"{self.url}{PublishedAsWmsAdmin.create_url_params(found_layer)}"
        wfs_link_gml2 = ""
        wfs_link_gml3 = ""
        layer_geometry_type = ""
        layer_bbox = BBox.from_string(found_layer.bound_dataset.bbox_wgs84)
        # TODO: Make that catched from configuration as we do for WMS already!
        metadata = MdMetadata(
            file_identifier=CharacterStringPropertyType(
                localised_character_string=LocalisedCharacterString(value=layer_name)
            ),
            language=CharacterStringPropertyType(
                localised_character_string=LocalisedCharacterString(value=language)
            ),
            hierarchy_level=[
                MdScopeCodePropertyType(
                    MdScopeCode(
                        value="dataset",
                        code_space="ISOTC211/19115",
                        code_list="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_ScopeCode",
                        code_list_value="dataset",
                    )
                )
            ],
            contact=[
                CiResponsiblePartyPropertyType(
                    ci_responsible_party=CiResponsibleParty(
                        id="contact",
                        individual_name=CharacterStringPropertyType(
                            localised_character_string=LocalisedCharacterString(
                                value="Fachstelle für Geoinformation"
                            )
                        ),
                        organisation_name=CharacterStringPropertyType(
                            localised_character_string=LocalisedCharacterString(
                                value="Grundbuch- und Vermessungsamt"
                            )
                        ),
                        contact_info=CiContactPropertyType(
                            ci_contact=CiContact(
                                phone=CiTelephonePropertyType(
                                    ci_telephone=CiTelephone(
                                        voice=[
                                            CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="+41612679953"
                                                )
                                            )
                                        ]
                                    )
                                ),
                                address=CiAddressPropertyType(
                                    ci_address=CiAddress(
                                        delivery_point=[
                                            CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="Dufourstrasse 40/50, Postfach"
                                                )
                                            )
                                        ],
                                        city=CharacterStringPropertyType(
                                            localised_character_string=LocalisedCharacterString(
                                                value="Basel"
                                            )
                                        ),
                                        administrative_area=CharacterStringPropertyType(
                                            localised_character_string=LocalisedCharacterString(
                                                value="Basel-Stadt"
                                            )
                                        ),
                                        postal_code=CharacterStringPropertyType(
                                            localised_character_string=LocalisedCharacterString(
                                                value="4001"
                                            )
                                        ),
                                        country=CharacterStringPropertyType(
                                            localised_character_string=LocalisedCharacterString(
                                                value="Schweiz"
                                            )
                                        ),
                                        electronic_mail_address=[
                                            CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="geo@bs.ch"
                                                )
                                            )
                                        ],
                                    )
                                ),
                                online_resource=CiOnlineResourcePropertyType(
                                    ci_online_resource=CiOnlineResource(
                                        linkage=UrlPropertyType(
                                            url=Url(value="https://wms.geo.bs.ch")
                                        )
                                    )
                                ),
                            )
                        ),
                        role=CiRoleCodePropertyType(
                            ci_role_code=CiRoleCode(
                                code_space="ISOTC211/19115",
                                code_list="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
                                code_list_value="pointOfContact",
                                value="pointOfContact",
                            )
                        ),
                    )
                )
            ],
            date_stamp=DatePropertyType(nil_reason="missing"),
            metadata_standard_name=CharacterStringPropertyType(
                localised_character_string=LocalisedCharacterString(
                    value="ISO 19115:2003 - Geographic information - Metadata"
                )
            ),
            metadata_standard_version=CharacterStringPropertyType(
                localised_character_string=LocalisedCharacterString(value="ISO 19115:2003")
            ),
            spatial_representation_info=[
                MdSpatialRepresentationPropertyType(
                    md_vector_spatial_representation=MdVectorSpatialRepresentation(
                        topology_level=MdTopologyLevelCodePropertyType(
                            md_topology_level_code=MdTopologyLevelCode(
                                code_space="ISOTC211/19115",
                                code_list="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_TopologyLevelCode",
                                code_list_value="geometryOnly",
                                value="geometryOnly",
                            )
                        ),
                        geometric_objects=[
                            MdGeometricObjectsPropertyType(
                                md_geometric_objects=MdGeometricObjects(
                                    geometric_object_type=MdGeometricObjectTypeCodePropertyType(
                                        md_geometric_object_type_code=MdGeometricObjectTypeCode(
                                            code_space="ISOTC211/19115",
                                            code_list="https://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_GeometricObjectTypeCode",
                                            code_list_value=layer_geometry_type,
                                            value=layer_geometry_type,
                                        )
                                    )
                                )
                            )
                        ],
                    )
                )
            ],
            reference_system_info=[
                MdReferenceSystemPropertyType(
                    md_reference_system=MdReferenceSystem(
                        reference_system_identifier=RsIdentifierPropertyType(
                            rs_identifier=RsIdentifier(
                                code=CharacterStringPropertyType(
                                    localised_character_string=LocalisedCharacterString(
                                        value=found_layer.bound_dataset.crs_to_qsl.auth_id
                                    )
                                ),
                                code_space=CharacterStringPropertyType(
                                    localised_character_string=LocalisedCharacterString(
                                        value="http://www.epsg-registry.org"
                                    )
                                ),
                                version=CharacterStringPropertyType(
                                    localised_character_string=LocalisedCharacterString(
                                        value="6.14"
                                    )
                                ),
                            )
                        )
                    )
                )
            ],
            identification_info=[
                MdIdentificationPropertyType(
                    md_data_identification=MdDataIdentification(
                        id=layer_name,
                        citation=CiCitationPropertyType(
                            ci_citation=CiCitation(
                                title=CharacterStringPropertyType(
                                    localised_character_string=LocalisedCharacterString(
                                        value=found_layer.title
                                    )
                                )
                            )
                        ),
                        abstract=CharacterStringPropertyType(
                            localised_character_string=LocalisedCharacterString(
                                value=found_layer.description
                            )
                        ),
                        language=[
                            CharacterStringPropertyType(
                                localised_character_string=LocalisedCharacterString(
                                    value=language
                                )
                            )
                        ],
                        extent=[
                            ExExtentPropertyType(
                                ex_extent=ExExtent(
                                    geographic_element=[
                                        ExGeographicExtentPropertyType(
                                            ex_geographic_bounding_box=ExGeographicBoundingBox(
                                                west_bound_longitude=DecimalPropertyType(
                                                    decimal=DecimalType(
                                                        value=Decimal(layer_bbox.x_min)
                                                    )
                                                ),
                                                east_bound_longitude=DecimalPropertyType(
                                                    decimal=DecimalType(
                                                        value=Decimal(layer_bbox.x_max)
                                                    )
                                                ),
                                                south_bound_latitude=DecimalPropertyType(
                                                    decimal=DecimalType(
                                                        value=Decimal(layer_bbox.y_min)
                                                    )
                                                ),
                                                north_bound_latitude=DecimalPropertyType(
                                                    decimal=DecimalType(
                                                        value=Decimal(layer_bbox.y_max)
                                                    )
                                                ),
                                            )
                                        )
                                    ]
                                )
                            )
                        ],
                    )
                )
            ],
            distribution_info=MdDistributionPropertyType(
                md_distribution=MdDistribution(
                    distributor=[
                        MdDistributorPropertyType(
                            md_distributor=MdDistributor(
                                distributor_contact=CiResponsiblePartyPropertyType(
                                    CiResponsibleParty(
                                        id="contact",
                                        individual_name=CharacterStringPropertyType(
                                            localised_character_string=LocalisedCharacterString(
                                                value="Fachstelle für Geoinformation"
                                            )
                                        ),
                                        organisation_name=CharacterStringPropertyType(
                                            localised_character_string=LocalisedCharacterString(
                                                value="Grundbuch- und Vermessungsamt"
                                            )
                                        ),
                                        contact_info=CiContactPropertyType(
                                            ci_contact=CiContact(
                                                phone=CiTelephonePropertyType(
                                                    ci_telephone=CiTelephone(
                                                        voice=[
                                                            CharacterStringPropertyType(
                                                                localised_character_string=LocalisedCharacterString(
                                                                    value="+41612679953"
                                                                )
                                                            )
                                                        ]
                                                    )
                                                ),
                                                address=CiAddressPropertyType(
                                                    ci_address=CiAddress(
                                                        delivery_point=[
                                                            CharacterStringPropertyType(
                                                                localised_character_string=LocalisedCharacterString(
                                                                    value="Dufourstrasse 40/50, Postfach"
                                                                )
                                                            )
                                                        ],
                                                        city=CharacterStringPropertyType(
                                                            localised_character_string=LocalisedCharacterString(
                                                                value="Basel"
                                                            )
                                                        ),
                                                        administrative_area=CharacterStringPropertyType(
                                                            localised_character_string=LocalisedCharacterString(
                                                                value="Basel-Stadt"
                                                            )
                                                        ),
                                                        postal_code=CharacterStringPropertyType(
                                                            localised_character_string=LocalisedCharacterString(
                                                                value="4001"
                                                            )
                                                        ),
                                                        country=CharacterStringPropertyType(
                                                            localised_character_string=LocalisedCharacterString(
                                                                value="Schweiz"
                                                            )
                                                        ),
                                                        electronic_mail_address=[
                                                            CharacterStringPropertyType(
                                                                localised_character_string=LocalisedCharacterString(
                                                                    value="geo@bs.ch"
                                                                )
                                                            )
                                                        ],
                                                    )
                                                ),
                                                online_resource=CiOnlineResourcePropertyType(
                                                    ci_online_resource=CiOnlineResource(
                                                        linkage=UrlPropertyType(
                                                            url=Url(
                                                                value="https://wms.geo.bs.ch"
                                                            )
                                                        )
                                                    )
                                                ),
                                            )
                                        ),
                                        role=CiRoleCodePropertyType(
                                            ci_role_code=CiRoleCode(
                                                code_space="ISOTC211/19115",
                                                code_list="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_RoleCode",
                                                code_list_value="pointOfContact",
                                                value="pointOfContact",
                                            )
                                        ),
                                    )
                                )
                            )
                        )
                    ],
                    transfer_options=[
                        MdDigitalTransferOptionsPropertyType(
                            md_digital_transfer_options=MdDigitalTransferOptions(
                                units_of_distribution=CharacterStringPropertyType(
                                    localised_character_string=LocalisedCharacterString(
                                        value="KB"
                                    )
                                ),
                                on_line=[
                                    CiOnlineResourcePropertyType(
                                        ci_online_resource=CiOnlineResource(
                                            linkage=UrlPropertyType(
                                                url=Url(value=wms_link_png)
                                            ),
                                            protocol=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="WWW:DOWNLOAD-1.0-http-get-map"
                                                )
                                            ),
                                            name=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value=layer_name
                                                )
                                            ),
                                            description=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="PNG Format"
                                                )
                                            ),
                                        )
                                    ),
                                    CiOnlineResourcePropertyType(
                                        ci_online_resource=CiOnlineResource(
                                            linkage=UrlPropertyType(
                                                url=Url(value=wfs_link_gml2)
                                            ),
                                            protocol=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="WWW:DOWNLOAD-1.0-http--download"
                                                )
                                            ),
                                            name=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value=layer_name
                                                )
                                            ),
                                            description=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="GML2 Format"
                                                )
                                            ),
                                        )
                                    ),
                                    CiOnlineResourcePropertyType(
                                        ci_online_resource=CiOnlineResource(
                                            linkage=UrlPropertyType(
                                                url=Url(value=wfs_link_gml3)
                                            ),
                                            protocol=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="WWW:DOWNLOAD-1.0-http--download"
                                                )
                                            ),
                                            name=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value=layer_name
                                                )
                                            ),
                                            description=CharacterStringPropertyType(
                                                localised_character_string=LocalisedCharacterString(
                                                    value="GML3 Format"
                                                )
                                            ),
                                        )
                                    ),
                                ],
                            )
                        )
                    ],
                )
            ),
        )
        return metadata

    @staticmethod
    def render_xml(metadata: MdMetadata) -> str:
        serializer = XmlSerializer(
            config=SerializerConfig(
                schema_location="gmd http://www.isotc211.org/2005/gmd/gmd.xsd"
            )
        )
        return serializer.render(
            metadata,
            ns_map={
                "gmd": "http://www.isotc211.org/2005/gmd",
                "gco": "http://www.isotc211.org/2005/gco",
                "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            },
        )

    @staticmethod
    def render_json(metadata: MdMetadata) -> str:
        serializer = JsonSerializer()
        return serializer.render(metadata)

    def render(self, requested_format: str, metadata: MdMetadata) -> str | None:
        if requested_format == "TEXT/XML":
            return self.render_xml(metadata)
        elif requested_format == "APPLICATION/JSON":
            return self.render_json(metadata)
        else:
            logging.debug("No matching Format was found.")
            return None
