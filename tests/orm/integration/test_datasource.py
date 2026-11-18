import pytest
from qgis_server_light.interface.exporter.extract import Field as QslField

from georama.integration.factories import FieldFactory, VectorFactory


class TestVectorPrimaryKey:
    """The primary key of a vector is taken from the field definitions QSL exported. Only
    one field is expected to be the primary key.
    """

    @pytest.mark.django_db
    def test_primary_key_field_name(self, project_global_organisation):
        vector = VectorFactory.create(project=project_global_organisation, fields=[])
        owner_id = FieldFactory.create(datasource=vector, name="owner_id")
        owner_id.set_definition_from_qsl(QslField(name="owner_id", type="int4"))
        owner_id.save()
        parcel_id = FieldFactory.create(datasource=vector, name="parcel_id")
        parcel_id.set_definition_from_qsl(
            QslField(name="parcel_id", type="int4", is_primary_key=True, is_generated=True)
        )
        parcel_id.save()
        assert vector.primary_key_field_name == "parcel_id"

    @pytest.mark.django_db
    def test_no_primary_key_without_definitions(self, project_global_organisation):
        # fields of exports before the definition existed tell nothing about the key
        vector = VectorFactory.create(project=project_global_organisation, fields=[])
        FieldFactory.create(datasource=vector, name="parcel_id", definition={})
        assert vector.primary_key_field_name is None


class TestGeometrylessVector:
    """A table without geometry is exported without CRS and bbox, the vector tells so."""

    @pytest.mark.django_db
    def test_crs_and_bbox_are_none(self, project_global_organisation):
        vector = VectorFactory.create(
            project=project_global_organisation,
            fields=[],
            is_spatial=False,
            crs=None,
            bbox=None,
            bbox_wgs84=None,
            geometry_type_simple=None,
            geometry_type_wkb=None,
            # the factory picks the styles by geometry type
            styles=[],
        )
        assert vector.crs_to_qsl is None
        assert vector.bbox_to_list is None
        assert vector.bbox_2d_string is None
        # the list of the manager shows it as table
        assert vector.icon == "fa fa-table"
