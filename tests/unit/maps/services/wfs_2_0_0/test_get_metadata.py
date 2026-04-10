import json
import logging
from decimal import Decimal
from unittest.mock import Mock, patch

from lxml import etree
from qgis_server_light.interface.common import BBox

from georama.data_integration.models import VectorDataSet
from georama.maps.interfaces.iso.tc211.gmd.dataclasses import (
    CharacterStringPropertyType,
    CiCitationPropertyType,
    CiOnlineResource,
    CiOnlineResourcePropertyType,
    DecimalPropertyType,
    DecimalType,
    ExExtentPropertyType,
    ExGeographicBoundingBox,
    MdDataIdentification,
    MdDigitalTransferOptionsPropertyType,
    MdIdentificationPropertyType,
    MdMetadata,
    MdReferenceSystem,
    MdReferenceSystemPropertyType,
    RsIdentifier,
    RsIdentifierPropertyType,
)
from georama.maps.services.wfs_2_0_0.get_metadata import PublishedAsWmsAdmin


def get_lcs(obj):
    return obj.localised_character_string.value


class TestWfsGetMetadata:
    def test_allowed_formats(self, wfs_get_metadata):
        expected = ["TEXT/XML", "APPLICATION/JSON"]
        assert wfs_get_metadata.allowed_formats == expected

    def test_obtain_accessible_layers(self, wfs_get_metadata, caplog):
        # No read permission
        layer_vector_no_read = Mock(
            has_read_permission=Mock(return_value=False),
            queryable=True,
            vector_dataset=Mock(spec=VectorDataSet),
        )
        # Read permission, but no VectorDataSet
        layer_read_query_but_no_vec = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=True,
        )
        # Accessible vector layer
        layer_vector_foo = Mock(
            has_read_permission=Mock(return_value=True),
            queryable=True,
            vector_dataset=Mock(spec=VectorDataSet),
        )

        with patch("georama.maps.models.PublishedAsWms.objects.get") as mock_get:
            mock_get.return_value = layer_vector_foo
            layers = wfs_get_metadata.obtain_accessible_layers(layer_names=["foo"])
            assert layers == [layer_vector_foo]

            mock_get.return_value = layer_vector_no_read
            layers = wfs_get_metadata.obtain_accessible_layers(layer_names=["no_read"])
            assert layers == []

            mock_get.return_value = layer_read_query_but_no_vec
            layers = wfs_get_metadata.obtain_accessible_layers(layer_names=["no_vector"])
            assert layers == []

            with caplog.at_level(logging.DEBUG):
                assert [r.msg for r in caplog.records] == [
                    "linked dataset has to be VectorDataSet for WFS 2.0.0, all others are ignored!",
                ]

    def test_create_layer_distributioninfo_info(self, wfs_get_metadata):
        layer_name = "TestPointLayer_1234_5678"
        wms_link_png = "http://localhost:4242/maps?SERVICE=WMS&REQUEST=GETMAP&..."
        wfs_link_gml3 = "http://localhost:4242/maps?SERVICE=WFS&REQUEST=GetFeature&..."

        dist_info = wfs_get_metadata.create_layer_distributioninfo_info(
            layer_name=layer_name,
            wms_link_png=wms_link_png,
            wfs_link_gml3=wfs_link_gml3,
        )
        assert isinstance(dist_info, list)
        assert len(dist_info) == 2

        rptype_wms_png, rptype_wfs_gml3 = dist_info
        assert isinstance(rptype_wms_png, CiOnlineResourcePropertyType)
        assert isinstance(rptype_wfs_gml3, CiOnlineResourcePropertyType)

        res_png = rptype_wms_png.ci_online_resource
        res_gml = rptype_wfs_gml3.ci_online_resource

        assert isinstance(res_png, CiOnlineResource)
        assert isinstance(res_gml, CiOnlineResource)

        assert res_png.linkage.url.value == wms_link_png
        assert get_lcs(res_png.protocol) == "WWW:DOWNLOAD-1.0-http-get-map"

        assert get_lcs(res_png.name) == layer_name
        assert get_lcs(res_png.description) == "PNG Format"

        assert res_gml.linkage.url.value == wfs_link_gml3
        assert get_lcs(res_gml.protocol) == "WWW:DOWNLOAD-1.0-http--download"

        assert get_lcs(res_gml.name) == layer_name
        assert get_lcs(res_gml.description) == "GML3 Format"

    def test_create_layer_reference_system_info(self, wfs_get_metadata, mock_layer):
        refsys_info = wfs_get_metadata.create_layer_reference_system_info(layer=mock_layer)
        assert isinstance(refsys_info, MdReferenceSystemPropertyType)

        md_refsys = refsys_info.md_reference_system
        assert isinstance(md_refsys, MdReferenceSystem)

        refsys_id = md_refsys.reference_system_identifier
        assert isinstance(refsys_id, RsIdentifierPropertyType)

        rs_id = refsys_id.rs_identifier
        assert isinstance(rs_id, RsIdentifier)

        assert get_lcs(rs_id.code) == mock_layer.bound_dataset.crs_to_qsl.auth_id
        assert get_lcs(rs_id.code_space) == "http://www.epsg-registry.org"
        assert get_lcs(rs_id.version) == "6.14"

    def test_create_layer_identification_info(self, wfs_get_metadata, mock_layer):
        lang = "en-US"
        layer_id_info = wfs_get_metadata.create_layer_identification_info(
            layer=mock_layer,
            language=lang,
        )
        assert isinstance(layer_id_info, MdIdentificationPropertyType)

        md_data_id = layer_id_info.md_data_identification
        assert isinstance(md_data_id, MdDataIdentification)
        assert md_data_id.id == mock_layer.name

        citation = md_data_id.citation
        assert isinstance(citation, CiCitationPropertyType)
        assert get_lcs(citation.ci_citation.title) == mock_layer.title

        abstract = md_data_id.abstract
        assert isinstance(abstract, CharacterStringPropertyType)
        assert get_lcs(abstract) == mock_layer.description

        languages = md_data_id.language
        assert isinstance(languages, list)
        language = languages[0]
        assert isinstance(language, CharacterStringPropertyType)
        assert get_lcs(language) == lang

        extents = md_data_id.extent
        assert isinstance(extents, list)
        extent = extents[0]
        assert isinstance(extent, ExExtentPropertyType)

        bbox = extent.ex_extent.geographic_element[0].ex_geographic_bounding_box
        assert isinstance(bbox, ExGeographicBoundingBox)

        layer_bbox = BBox.from_string(mock_layer.bound_dataset.bbox_wgs84)
        expected_bbox = ExGeographicBoundingBox(
            west_bound_longitude=DecimalPropertyType(
                decimal=DecimalType(value=Decimal(layer_bbox.x_min))
            ),
            east_bound_longitude=DecimalPropertyType(
                decimal=DecimalType(value=Decimal(layer_bbox.x_max))
            ),
            south_bound_latitude=DecimalPropertyType(
                decimal=DecimalType(value=Decimal(layer_bbox.y_min))
            ),
            north_bound_latitude=DecimalPropertyType(
                decimal=DecimalType(value=Decimal(layer_bbox.y_max))
            ),
        )
        assert bbox == expected_bbox

    def test_create_file_identification_info(self, wfs_get_metadata):
        layer_name = "TestPointLayer_1234_5678"
        file_id_info = wfs_get_metadata.create_file_identification_info(
            layer_name=layer_name,
        )

        assert isinstance(file_id_info, CharacterStringPropertyType)
        assert get_lcs(file_id_info) == layer_name

    def test_get_metadata(self, wfs_get_metadata, mock_layer):
        lang = "en-US"
        wms_params = PublishedAsWmsAdmin.create_wms_url_params(mock_layer)
        wms_link_png = f"{wfs_get_metadata.url}{wms_params}"

        fmt = "APPLICATION/GML+XML; VERSION=3.2"
        wfs_params = PublishedAsWmsAdmin.create_wfs_url_params(mock_layer, output_format=fmt)
        wfs_link_gml3 = f"{wfs_get_metadata.url}{wfs_params}"

        obtain_layers_method = (
            "georama.maps.services.wfs_2_0_0.get_metadata."
            "WfsGetMetadata.obtain_accessible_layers"
        )
        with patch(obtain_layers_method) as mock_get:
            mock_get.return_value = [mock_layer]

            metadata = wfs_get_metadata.get_metadata(
                layer_name=mock_layer.name,
                language=lang,
            )

        assert isinstance(metadata, MdMetadata)
        file_id = metadata.file_identifier
        assert file_id == wfs_get_metadata.create_file_identification_info(mock_layer.name)

        id_infos = metadata.identification_info
        assert isinstance(id_infos, list)

        id_info = id_infos[0]
        assert isinstance(id_info, MdIdentificationPropertyType)
        assert id_info == wfs_get_metadata.create_layer_identification_info(mock_layer, lang)

        refsys_infos = metadata.reference_system_info
        assert isinstance(refsys_infos, list)

        refsys_info = refsys_infos[0]
        assert isinstance(refsys_info, MdReferenceSystemPropertyType)
        assert refsys_info == wfs_get_metadata.create_layer_reference_system_info(mock_layer)

        transfer_opts = metadata.distribution_info.md_distribution.transfer_options
        assert isinstance(transfer_opts, list)

        opts = transfer_opts[0]
        assert isinstance(opts, MdDigitalTransferOptionsPropertyType)
        assert (
            opts.md_digital_transfer_options.on_line
            == wfs_get_metadata.create_layer_distributioninfo_info(
                mock_layer.name, wms_link_png, wfs_link_gml3
            )
        )

    def test_render_xml(self, wfs_get_metadata, mock_layer):
        lang = "en-US"

        obtain_layers_method = (
            "georama.maps.services.wfs_2_0_0.get_metadata."
            "WfsGetMetadata.obtain_accessible_layers"
        )
        with patch(obtain_layers_method) as mock_get:
            mock_get.return_value = [mock_layer]
            rendered = wfs_get_metadata.render_xml(
                wfs_get_metadata.get_metadata(mock_layer.name, lang)
            )

        root = etree.fromstring(rendered.encode("utf-8"))
        assert root.tag == "{http://www.isotc211.org/2005/gmd}MD_Metadata"

    def test_render_json(self, wfs_get_metadata, mock_layer):
        lang = "en-US"

        obtain_layers_method = (
            "georama.maps.services.wfs_2_0_0.get_metadata."
            "WfsGetMetadata.obtain_accessible_layers"
        )
        with patch(obtain_layers_method) as mock_get:
            mock_get.return_value = [mock_layer]
            rendered = wfs_get_metadata.render_json(
                wfs_get_metadata.get_metadata(mock_layer.name, lang)
            )

        metadata = json.loads(rendered)
        file_id = metadata["fileIdentifier"]["LocalisedCharacterString"]["value"]
        assert file_id == mock_layer.name

        assert sorted(metadata.keys()) == [
            "applicationSchemaInfo",
            "characterSet",
            "contact",
            "contentInfo",
            "dataQualityInfo",
            "dataSetURI",
            "dateStamp",
            "describes",
            "distributionInfo",
            "featureAttribute",
            "featureType",
            "fileIdentifier",
            "hierarchyLevel",
            "hierarchyLevelName",
            "id",
            "identificationInfo",
            "language",
            "locale",
            "metadataConstraints",
            "metadataExtensionInfo",
            "metadataMaintenance",
            "metadataStandardName",
            "metadataStandardVersion",
            "parentIdentifier",
            "portrayalCatalogueInfo",
            "propertyType",
            "referenceSystemInfo",
            "series",
            "spatialRepresentationInfo",
            "uuid",
        ]

    def test_render(self, wfs_get_metadata):
        render_xml = Mock(return_value=("content"))
        render_json = Mock(return_value=("content"))

        wfs_get_metadata.render_xml = render_xml
        wfs_get_metadata.render_json = render_json

        expectations = [
            (
                "TEXT/XML",
                render_xml,
            ),
            (
                "APPLICATION/JSON",
                render_json,
            ),
        ]

        capabilities = Mock()
        for format, render_method in expectations:
            render_xml.reset_mock()
            render_json.reset_mock()

            result = wfs_get_metadata.render(format, capabilities)
            render_method.assert_called_with(capabilities)
            assert result == "content"

        failure_response = wfs_get_metadata.render("UNKNOWN", capabilities)
        assert failure_response is None
