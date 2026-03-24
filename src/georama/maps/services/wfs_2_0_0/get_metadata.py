import logging
from decimal import Decimal

from qgis_server_light.interface.common import BBox
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from georama.data_integration.models import VectorDataSet
from georama.maps.admin import PublishedAsWmsAdmin
from georama.maps.interfaces.iso.tc211.gmd.dataclasses import (
    CharacterStringPropertyType,
    CiCitation,
    CiCitationPropertyType,
    CiOnlineResource,
    CiOnlineResourcePropertyType,
    DecimalPropertyType,
    DecimalType,
    ExExtent,
    ExExtentPropertyType,
    ExGeographicBoundingBox,
    ExGeographicExtentPropertyType,
    LocalisedCharacterString,
    MdDataIdentification,
    MdIdentificationPropertyType,
    MdMetadata,
    MdReferenceSystem,
    MdReferenceSystemPropertyType,
    RsIdentifier,
    RsIdentifierPropertyType,
    Url,
    UrlPropertyType,
)
from georama.maps.maps_config import Config
from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WfsGetMetadata(OgcOperation):
    @property
    def allowed_formats(self) -> list[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]

    def obtain_accessible_layers(
        self, layer_names: list[str] | None = None
    ) -> list[PublishedAsWms]:
        accessible_layers = []
        published_as = PublishedAsWms.objects.get(name=layer_names[0])
        if published_as.has_read_permission(self.user, self.appname):
            if isinstance(published_as.vector_dataset, VectorDataSet):
                accessible_layers.append(published_as)
            else:
                logging.debug(
                    "linked dataset has to be VectorDataSet for"
                    " WFS 2.0.0, all others are ignored!"
                )
        return accessible_layers

    def create_layer_distributioninfo_info(
        self, layer_name: str, wms_link_png: str, wfs_link_gml3: str
    ) -> list[CiOnlineResourcePropertyType]:
        return [
            CiOnlineResourcePropertyType(
                ci_online_resource=CiOnlineResource(
                    linkage=UrlPropertyType(url=Url(value=wms_link_png)),
                    protocol=CharacterStringPropertyType(
                        localised_character_string=LocalisedCharacterString(
                            value="WWW:DOWNLOAD-1.0-http-get-map"
                        )
                    ),
                    name=CharacterStringPropertyType(
                        localised_character_string=LocalisedCharacterString(value=layer_name)
                    ),
                    description=CharacterStringPropertyType(
                        localised_character_string=LocalisedCharacterString(value="PNG Format")
                    ),
                )
            ),
            CiOnlineResourcePropertyType(
                ci_online_resource=CiOnlineResource(
                    linkage=UrlPropertyType(url=Url(value=wfs_link_gml3)),
                    protocol=CharacterStringPropertyType(
                        localised_character_string=LocalisedCharacterString(
                            value="WWW:DOWNLOAD-1.0-http--download"
                        )
                    ),
                    name=CharacterStringPropertyType(
                        localised_character_string=LocalisedCharacterString(value=layer_name)
                    ),
                    description=CharacterStringPropertyType(
                        localised_character_string=LocalisedCharacterString(
                            value="GML3 Format"
                        )
                    ),
                )
            ),
        ]

    def create_layer_reference_system_info(
        self, layer: PublishedAsWms
    ) -> MdReferenceSystemPropertyType:
        return MdReferenceSystemPropertyType(
            md_reference_system=MdReferenceSystem(
                reference_system_identifier=RsIdentifierPropertyType(
                    rs_identifier=RsIdentifier(
                        code=CharacterStringPropertyType(
                            localised_character_string=LocalisedCharacterString(
                                value=layer.bound_dataset.crs_to_qsl.auth_id
                            )
                        ),
                        code_space=CharacterStringPropertyType(
                            localised_character_string=LocalisedCharacterString(
                                value="http://www.epsg-registry.org"
                            )
                        ),
                        version=CharacterStringPropertyType(
                            localised_character_string=LocalisedCharacterString(value="6.14")
                        ),
                    )
                )
            )
        )

    def create_layer_identification_info(
        self, layer: PublishedAsWms, language: str
    ) -> MdIdentificationPropertyType:
        layer_bbox = BBox.from_string(layer.bound_dataset.bbox_wgs84)
        return MdIdentificationPropertyType(
            md_data_identification=MdDataIdentification(
                id=layer.name,
                citation=CiCitationPropertyType(
                    ci_citation=CiCitation(
                        title=CharacterStringPropertyType(
                            localised_character_string=LocalisedCharacterString(
                                value=layer.title
                            )
                        )
                    )
                ),
                abstract=CharacterStringPropertyType(
                    localised_character_string=LocalisedCharacterString(
                        value=layer.description
                    )
                ),
                language=[
                    CharacterStringPropertyType(
                        localised_character_string=LocalisedCharacterString(value=language)
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

    def create_file_identification_info(self, layer_name: str) -> CharacterStringPropertyType:
        return CharacterStringPropertyType(
            localised_character_string=LocalisedCharacterString(value=layer_name)
        )

    def get_metadata(self, layer_name: str, language: str) -> MdMetadata:
        """
        Attibutes:
            layer_name: name of WMS/WFS Layer
            language: in the form `en-US`
            layer_geometry_type: `complex`|`composite`|`curve`|`point`|`solid`|`surface`
        """
        found_layer = self.obtain_accessible_layers([layer_name])[0]
        wms_link_png = f"{self.url}{PublishedAsWmsAdmin.create_wms_url_params(found_layer)}"
        wfs_link_gml3 = (
            f"{self.url}"
            f"{PublishedAsWmsAdmin.create_wfs_url_params(found_layer, output_format='APPLICATION/GML+XML; VERSION=3.2')}"  # noqa: E501
        )
        BBox.from_string(found_layer.bound_dataset.bbox_wgs84)
        # TODO: Make that catched from configuration as we do for WMS already!
        config = Config().wfs_get_metadata_config(self.url)
        decoder = DictDecoder()
        metadata = decoder.decode(config, MdMetadata)
        metadata.file_identifier = self.create_file_identification_info(found_layer.name)
        metadata.identification_info = [
            self.create_layer_identification_info(found_layer, language)
        ]
        metadata.reference_system_info = [self.create_layer_reference_system_info(found_layer)]
        metadata.distribution_info.md_distribution.transfer_options[
            0
        ].md_digital_transfer_options.on_line = self.create_layer_distributioninfo_info(
            found_layer.name, wms_link_png, wfs_link_gml3
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
