import logging
from typing import List, Tuple, Type

from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from qgis_server_light.interface.qgis import Config, Custom, Raster, Vector
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.data_integration.admin import (
    QgisProject,
    QgisProjectFileStructure,
    QgisProjectGroup,
)
from georama.data_integration.data_integration_config import (
    Config as DataintgrationConfig,
)
from georama.data_integration.models import (
    CustomDataSet,
    Field,
    Mandant,
    Project,
    RasterDataSet,
    VectorDataSet,
)

log = logging.getLogger(__name__)


class RegisterQgisProject(View):
    @staticmethod
    def get_dataset_by_id(
        identifier: str,
        model_class: Type[VectorDataSet] | Type[RasterDataSet] | Type[CustomDataSet],
    ) -> VectorDataSet | RasterDataSet | CustomDataSet | None:
        dataset_qs = model_class.objects.filter(qgis_layer_id=identifier)
        if dataset_qs.exists():
            return dataset_qs.get()
        else:
            return None

    @staticmethod
    def find_config_dataset_by_id(
        datasets: List[Vector] | List[Raster] | List[Custom], id: str
    ) -> Vector | Raster | Custom | None:
        for dataset in datasets:
            if dataset.id == id:
                return dataset
        return None

    @staticmethod
    def load_project_config(
        mandant_name: str, project_name: str
    ) -> Tuple[QgisProject, Config] | Tuple[None, None] | Tuple[QgisProject, None]:
        config = DataintgrationConfig()
        qpfs = QgisProjectFileStructure(config.path)
        qpfs.create_groups(config.qgis_project_extensions)
        group = qpfs.find_group_by_name(mandant_name)
        if not isinstance(group, QgisProjectGroup):
            return None, None
        project = group.find_project_by_name(project_name)
        if not isinstance(project, QgisProject):
            return None, None
        if not project.has_config:
            return project, None
        parser_config = ParserConfig(
            fail_on_unknown_properties=False, fail_on_unknown_attributes=False
        )
        parser = JsonParser(parser_config)
        project_config = parser.parse(project.config_path, Config)
        return project, project_config

    def integrate_project(
        self, project: QgisProject, project_config: Config, mandant_name: str
    ):
        mandant_qs = Mandant.objects.filter(name=mandant_name)
        if not mandant_qs.exists():
            mandant_db = Mandant(name=mandant_name)
            mandant_db.save()
        else:
            # we can do so, because name is unique in DB
            mandant_db = mandant_qs.get()
        project_qs = Project.objects.filter(name=project.name, mandant=mandant_db)
        if not project_qs.exists():
            logging.debug("Project does not exists, we first create a new DB object.")
            project_db = Project(
                mandant=mandant_db,
                name=project.name,
                hash=project.hash,
                title=project_config.project.name,
            )

        else:
            logging.debug("Project exists, we proceed with the DB object.")
            project_db = project_qs.get()
            if project_db.hash == project.hash:
                logging.debug(
                    "HASH of config and in DB was the same. No further work necessary."
                )
                return redirect("admin:data_integration_project_changelist")
            else:
                project_db.mandant = mandant_db
                project_db.name = project.name
                project_db.hash = project.hash
                project_db.title = project_config.project.name
        project_db.save()
        logging.debug("Handling of vector datasets")
        for layer in project_config.datasets.vector:
            dataset = self.get_dataset_by_id(layer.id, VectorDataSet)
            if dataset is None:
                logging.debug(
                    f" New dataset will be added {layer.name} (qgis-layer-id: {layer.id}) "
                )
                dataset = VectorDataSet()
            else:
                logging.debug(
                    f" Dataset was found and will be updated {layer.name} (qgis-layer-id: {layer.id})"
                )
            dataset.project = project_db
            dataset.name = layer.name
            dataset.title = layer.title
            dataset.bbox = layer.bbox.to_string()
            dataset.bbox_wgs84 = layer.bbox_wgs84.to_string()
            dataset.path = layer.path
            dataset.styles = DictEncoder().encode(layer.styles)
            dataset.driver = layer.driver
            dataset.source = DictEncoder().encode(layer.source)
            dataset.qgis_layer_id = layer.id
            dataset.crs = DictEncoder().encode(layer.crs)
            dataset.minimum_scale = layer.minimum_scale
            dataset.maximum_scale = layer.maximum_scale
            dataset.geometry_type_simple = layer.geometry_type_simple
            dataset.geometry_type_wkb = layer.geometry_type_wkb
            dataset.save()
            logging.debug(
                f" ✓ Dataset {layer.name} (qgis-layer-id: {layer.id}) was written to DB successfully."
            )
            logging.debug(f" Handling of related fields.")
            for field in layer.fields:

                field_qs = Field.objects.filter(
                    name=field.name,
                    type=field.type,
                    type_wfs=field.type_wfs,
                    type_oapif=field.type_oapif,
                    type_oapif_format=field.type_oapif_format,
                    alias=field.alias,
                        comment=field.comment,
                    nullable=field.nullable,
                    vector_dataset=dataset,
                )
                if not field_qs.exists():
                    logging.debug(
                        f"   New Field {field.name} (type: {field.type}) will be added."
                    )
                    field = Field(
                        name=field.name,
                        type=field.type,
                        type_wfs=field.type_wfs,
                        type_oapif=field.type_oapif,
                        type_oapif_format=field.type_oapif_format,
                        alias=field.alias,
                            comment=field.comment,
                        nullable=field.nullable,
                        length=field.length,
                        precision=field.precision,
                        vector_dataset=dataset,
                    )
                else:
                    logging.debug(
                        f"   Field {field.name} (type: {field.type}) was found and will be updated."
                    )
                    field = field_qs.get()
                    field.name = field.name
                    field.type = field.type
                    field.type_wfs = field.type_wfs
                    field.type_json = field.type_json
                    field.type_json_format = field.type_json_format
                    field.alias = field.alias
                    field.comment = field.comment
                    field.nullable = field.nullable
                    field.length = field.length
                    field.precision = field.precision
                    field.vector_dataset = dataset
                field.save()
                logging.debug(
                    f"   ✓ Field {field.name} (type: {field.type}) was written to DB successfully."
                )
            logging.debug(f"   Cleaning out old fields...")
            for field_db in Field.objects.filter(vector_dataset=dataset).all():
                field_match = layer.get_field_by_name(field_db.name)
                if field_match is None:
                    logging.debug(
                        f'    Deleting field "{field.name}" of vector dataset {dataset.name} since it was '
                        "not in project config anymore"
                    )
                    field_db.delete()
            logging.debug(f"   ✓ Finished - Cleaning out old fields...")
        logging.debug(f" Cleaning out old vector datasets.")
        for dataset_db in VectorDataSet.objects.filter(project=project_db).all():
            dataset_match = self.find_config_dataset_by_id(
                project_config.datasets.vector, dataset_db.qgis_layer_id
            )
            if dataset_match is None:
                logging.debug(
                    f"    Deleting dataset {dataset_db.name} since it was not in project config anymore"
                )
                dataset_db.delete()
        logging.debug(f" ✓ Finished - Cleaning out old vector datasets.")
        logging.debug("✓ Finished - Handling of raster datasets")
        logging.debug("Handling of raster datasets")
        for layer in project_config.datasets.raster:
            dataset = self.get_dataset_by_id(layer.id, RasterDataSet)
            if dataset is None:
                logging.debug(
                    f" New dataset will be added {layer.name} (qgis-layer-id: {layer.id}) "
                )
                dataset = RasterDataSet()
            else:
                logging.debug(
                    f" Dataset was found and will be updated {layer.name} (qgis-layer-id: {layer.id})"
                )
            dataset.project = project_db
            dataset.name = layer.name
            dataset.title = layer.title
            dataset.bbox = layer.bbox.to_string()
            dataset.bbox_wgs84 = layer.bbox_wgs84.to_string()
            dataset.path = layer.path
            dataset.styles = DictEncoder().encode(layer.styles)
            dataset.driver = layer.driver
            dataset.source = DictEncoder().encode(layer.source)
            dataset.qgis_layer_id = layer.id
            dataset.crs = DictEncoder().encode(layer.crs)
            dataset.minimum_scale = layer.minimum_scale
            dataset.maximum_scale = layer.maximum_scale
            dataset.save()
            logging.debug(
                f" ✓ Dataset {layer.name} (qgis-layer-id: {layer.id}) was written to DB successfully."
            )
        logging.debug(f" Cleaning out old rester datasets.")
        for dataset_db in RasterDataSet.objects.filter(project=project_db).all():
            dataset_match = self.find_config_dataset_by_id(
                project_config.datasets.raster, dataset_db.qgis_layer_id
            )
            if dataset_match is None:
                logging.debug(
                    f"  Deleting dataset {dataset_db.name} since it was not in project config anymore"
                )
                dataset_db.delete()
        logging.debug(f" ✓ Finished - Cleaning out old raster datasets.")
        logging.debug("✓ Finished - Handling of raster datasets")
        logging.debug("Handling of custom datasets")
        for layer in project_config.datasets.custom:
            dataset = self.get_dataset_by_id(layer.id, CustomDataSet)
            if dataset is None:
                logging.debug(
                    f" New dataset will be added {layer.name} (qgis-layer-id: {layer.id}) "
                )
                dataset = CustomDataSet()
            else:
                logging.debug(
                    f" Dataset was found and will be updated {layer.name} (qgis-layer-id: {layer.id})"
                )
            dataset.project = project_db
            dataset.name = layer.name
            dataset.title = layer.title
            dataset.bbox = layer.bbox.to_string()
            dataset.bbox_wgs84 = layer.bbox_wgs84.to_string()
            dataset.path = layer.path
            dataset.styles = DictEncoder().encode(layer.styles)
            dataset.driver = layer.driver
            dataset.source = DictEncoder().encode(layer.source)
            dataset.qgis_layer_id = layer.id
            dataset.crs = DictEncoder().encode(layer.crs)
            dataset.minimum_scale = layer.minimum_scale
            dataset.maximum_scale = layer.maximum_scale
            dataset.save()
        logging.debug(f" Cleaning out old custom datasets.")
        for dataset_db in CustomDataSet.objects.filter(project=project_db).all():
            dataset_match = self.find_config_dataset_by_id(
                project_config.datasets.custom, dataset_db.qgis_layer_id
            )
            if dataset_match is None:
                logging.debug(
                    f"  Deleting dataset {dataset_db.name} since it was not in project config anymore"
                )
                dataset_db.delete()
        logging.debug(f" ✓ Finished - Cleaning out old custom datasets.")

        logging.debug("✓ Finished - Handling of custom datasets")

    @transaction.atomic
    def get(self, request: HttpRequest, mandant_name: str, project_name: str, **kwargs):
        project, project_config = self.load_project_config(mandant_name, project_name)
        if not project_config or not project:
            redirect("admin:data_integration_project_changelist")
        self.integrate_project(project, project_config, mandant_name)
        return redirect("admin:data_integration_project_changelist")
