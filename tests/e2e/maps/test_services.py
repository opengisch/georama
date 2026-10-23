import pytest
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.models.xsd import Schema

from georama.maps.interfaces.ogc.wfs_2_0_0 import (
    FeatureTypeList,
    OperationsMetadata,
    ServiceIdentification,
    ServiceProvider,
    WfsCapabilities,
)
from georama.maps.interfaces.ogc.wms_1_3_0.capabilities import Capability, Service, WmsCapabilities
from georama.maps.interfaces.opengis.gml_3_2_1 import MdMetadata
from georama.maps.maps_config import Config
from georama.maps.services.wfs_2_0_0 import WfsOperation


class TestOgcService:
    """We test the correct extraction and responses of OGC WXS offered by georama,
    currently we don't test:
        - rendering
        - feature extraction
        - legends
    """

    @pytest.mark.django_db
    def test_capabilities_wms(self, client, global_wms_layer_public_queryable):
        response = client.get("/maps/ows/?SERVICE=WMS&REQUEST=GETCAPABILITIES&VERSION=1.3.0")
        capabilities: WmsCapabilities = XmlParser().from_bytes(response.content, WmsCapabilities)

        assert isinstance(capabilities.capability, Capability)
        assert isinstance(capabilities.service, Service)
        assert capabilities.capability.layer is not None
        assert len(capabilities.capability.layer.layer) == 1
        assert (
            capabilities.capability.layer.layer[0].name.value
            == global_wms_layer_public_queryable.identifier
        )
        assert (
            capabilities.capability.layer.layer[0].title.value
            == global_wms_layer_public_queryable.metadata.title
        )
        assert (
            capabilities.capability.layer.layer[0].abstract.value
            == global_wms_layer_public_queryable.metadata.description
        )
        styles = global_wms_layer_public_queryable.datasource.styles_to_qsl
        assert [s.name.value for s in capabilities.capability.layer.layer[0].style] == [
            style.name for style in styles
        ]
        assert capabilities.capability.layer.layer[0].queryable == 1

    @pytest.mark.django_db
    def test_capabilities_wfs(self, client, global_wms_layer_public_queryable):
        type_name = WfsOperation.encode_layer_name(global_wms_layer_public_queryable.identifier)
        response = client.get("/maps/ows/?SERVICE=WFS&REQUEST=GETCAPABILITIES&VERSION=2.0.0")
        capabilities: WfsCapabilities = XmlParser().from_bytes(response.content, WfsCapabilities)

        assert isinstance(capabilities.service_identification, ServiceIdentification)
        assert isinstance(capabilities.service_provider, ServiceProvider)
        assert isinstance(capabilities.operations_metadata, OperationsMetadata)
        assert isinstance(capabilities.feature_type_list, FeatureTypeList)
        assert (
            capabilities.feature_type_list.feature_type[0].name
            == f"{WfsOperation.own_namespace}:{type_name}"
        )
        assert (
            capabilities.feature_type_list.feature_type[0].title[0].value
            == global_wms_layer_public_queryable.metadata.title
        )
        assert (
            capabilities.feature_type_list.feature_type[0]
            .default_crs_or_other_crs_or_no_crs[0]
            .value
            == global_wms_layer_public_queryable.datasource.crs_to_qsl.ogc_uri
        )
        assert [
            crs.value
            for crs in capabilities.feature_type_list.feature_type[
                0
            ].default_crs_or_other_crs_or_no_crs[1:]
        ] == [
            crs.ogc_uri
            for crs in Config().other_crs("maps")
            if crs.ogc_uri != global_wms_layer_public_queryable.datasource.crs_to_qsl.ogc_uri
        ]
        assert (
            capabilities.feature_type_list.feature_type[0].output_formats.format[0]
            == "application/gml+xml; version=3.2"
        )
        assert (
            capabilities.feature_type_list.feature_type[0].output_formats.format[1]
            == "text/xml; subtype=gml/3.2.1"
        )
        assert (
            capabilities.feature_type_list.feature_type[0].metadata_url[0].href
            == f"http://testserver/maps/ows/?request=GetMetadata&layer={type_name}"
        )

    @pytest.mark.django_db
    def test_metadata_wfs(self, client, global_wms_layer_public_queryable):
        response = client.get(
            f"/maps/ows/?REQUEST=GetMetadata&layer={global_wms_layer_public_queryable.identifier}"
        )
        metadata: MdMetadata = XmlParser().from_bytes(response.content, MdMetadata)
        assert (
            metadata.file_identifier.localised_character_string.value
            == global_wms_layer_public_queryable.identifier
        )
        assert len(metadata.distribution_info.md_distribution.transfer_options) == 1
        assert (
            len(
                metadata.distribution_info.md_distribution.transfer_options[
                    0
                ].md_digital_transfer_options.on_line
            )
            == 2
        )
        assert (
            metadata.distribution_info.md_distribution.transfer_options[0]
            .md_digital_transfer_options.on_line[0]
            .ci_online_resource.description.localised_character_string.value
            == "PNG Format"
        )
        assert (
            metadata.distribution_info.md_distribution.transfer_options[0]
            .md_digital_transfer_options.on_line[1]
            .ci_online_resource.description.localised_character_string.value
            == "GML3 Format"
        )

    @pytest.mark.django_db
    def test_describe_feature_type(self, client, global_wms_layer_public_queryable):
        type_name = WfsOperation.encode_layer_name(global_wms_layer_public_queryable.identifier)
        response = client.get(
            f"/maps/ows/?SERVICE=WFS&VERSION=2.0.0&REQUEST=DescribeFeatureType&TYPENAME={WfsOperation.own_namespace}:{type_name}"
        )
        schema: Schema = XmlParser().from_bytes(response.content, Schema)
        assert schema.elements[0].name == type_name
        assert schema.elements[0].type == f"{WfsOperation.own_namespace}:{type_name}Type"
        assert schema.complex_types[0].name == f"{type_name}Type"
        assert ["geometry"] + [
            f.name for f in global_wms_layer_public_queryable.datasource.vector.fields.all()
        ] == [e.name for e in schema.complex_types[0].complex_content.extension.sequence.elements]
