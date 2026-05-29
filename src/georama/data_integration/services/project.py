import logging
import math

from qgis_server_light.interface.exporter.extract import Config as QslConfig
from qgis_server_light.interface.exporter.extract import Custom, Raster, Vector
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.data_integration.lib.data_integration_config import (
    Config as DataIntegrationConfig,
)
from georama.data_integration.lib.qgis_project_file_structure import (
    Config,
    QgisProject,
    QgisProjectFileStructure,
)
from georama.data_integration.models import (
    CustomDataSet,
    Field,
    Mandant,
    Project,
    RasterDataSet,
    VectorDataSet,
)


class FSService:
    def __init__(self):
        """
        Implements handling of file system related stuff. Like reading in
        the structure of folders and QGIS Project files.
        """
        self.config = DataIntegrationConfig()
        self.qpfs = QgisProjectFileStructure(self.config.path)
        self.qpfs.create_groups(self.config.qgis_project_extensions)

    def count(self) -> int:
        return sum(len(group.projects) for group in self.qpfs.groups)

    def count_out_dated(self):
        """
        Counts file system projects which are integrated into Georama DB already
        and where the JSON config file on the disk has a different hash then the
        hash wich was stored in the database when the project was integrated.

        Returns:
            The count of items matching the described criteria.
        """

        count = 0
        integrated_projects = DBService().get_list()
        for integrated_project in integrated_projects:
            found_group = self.qpfs.find_group_by_name(integrated_project.mandant.name)
            found_project = found_group.find_project_by_name(integrated_project.name)
            if found_project.hash != integrated_project.hash:
                count += 1
        return count

    def load_project_config(self, project: QgisProject) -> QslConfig | None:
        """
        Reads in the config file from disk (QGIS Project JSON).

        Args:
            project: The project we want to read the config for.

        Returns:
            The parsed and deserialized config or None if project has no config file.
        """
        parser_config = ParserConfig(
            fail_on_unknown_properties=False, fail_on_unknown_attributes=False
        )
        parser = JsonParser(parser_config)
        if project.has_config:
            try:
                project_config = parser.parse(project.config_path, QslConfig)
                return project_config
            except Exception as e:
                logging.info(project.name)
                logging.error(e)
        return None

    def find_config_dataset_by_id(
        self, datasets: list[Vector] | list[Raster] | list[Custom], id: str
    ) -> Vector | Raster | Custom | None:
        """
        Finds a dataset by id in the list of passed datasets.

        Args:
            datasets: Either a list Vector, Raster or Custom datasets.
            id: The id value which should be looked up

        Returns:
            The found dataset or None
        """
        for dataset in datasets:
            if dataset.id == id:
                return dataset
        return None

    def get(self, group_name: str, project_name: str) -> QgisProject:
        """
        This gets a project by group and name from the disk, it also adds config
        and db instance if existing.

        Args:
            group_name: The name
            project_name:

        Returns:

        """
        found_group = self.qpfs.find_group_by_name(group_name)
        found_project = found_group.find_project_by_name(project_name)
        found_project.database_representation = DBService().get_project_by_group_and_name(
            group_name, project_name
        )
        found_project.config = self.load_project_config(found_project)
        return found_project

    def get_list(self) -> list[QgisProject]:
        integrated_projects = DBService().get_list()

        for integrated_project in integrated_projects:
            found_group = self.qpfs.find_group_by_name(integrated_project.mandant.name)
            found_project = found_group.find_project_by_name(integrated_project.name)
            found_project.database_representation = integrated_project
        for group in self.qpfs.groups:
            for project in group.projects:
                project.config = self.load_project_config(project)

        return sum((group.projects for group in self.qpfs.groups), [])

    def get_list_page(self, offset: int | None = None, count: int | None = None):
        return self.get_list()

    def amount_of_pages(self, offset=100) -> int:
        return math.ceil(self.count() / offset)

    def pages_list(self, offset=100):
        page_numbers = list(range(1, self.amount_of_pages(offset) + 1))
        pages = []
        for page_number in page_numbers:
            pages.append([page_number, (page_number - 1) * offset])
        return pages


class DBService:
    def get_list(self) -> list[Project]:
        return list(Project.objects.all())

    def get_project_by_group_and_name(self, group_name=None, project_name=None):
        query = Project.objects.filter(mandant__name=group_name, name=project_name)
        if query.exists():
            return query.get()
        return None

    @staticmethod
    def get_dataset_by_id(
        identifier: str,
        model_class: type[VectorDataSet] | type[RasterDataSet] | type[CustomDataSet],
    ) -> VectorDataSet | RasterDataSet | CustomDataSet | None:
        dataset_qs = model_class.objects.filter(qgis_layer_id=identifier)
        if dataset_qs.exists():
            return dataset_qs.get()
        else:
            return None

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
                version=project_config.project.version,
                title=project_config.project.name,
            )

        else:
            logging.debug("Project exists, we proceed with the DB object.")
            project_db = project_qs.get()
            if project_db.hash == project.hash:
                logging.debug(
                    "HASH of config and in DB was the same. No further work necessary."
                )
                return None
            else:
                project_db.mandant = mandant_db
                project_db.name = project.name
                project_db.hash = project.hash
                project_db.version = project_config.project.version
                project_db.title = project_config.project.name
        project_db.save()
        fss_project = FSService()
        logging.debug("Handling of vector datasets")
        for layer in project_config.datasets.vector:
            if layer.is_spatial:
                dataset = self.get_dataset_by_id(layer.id, VectorDataSet)
                if dataset is None:
                    logging.debug(
                        f" New dataset will be added {layer.name} (qgis-layer-id: {layer.id}) "
                    )
                    dataset = VectorDataSet()
                else:
                    logging.debug(
                        f" Dataset was found and will be updated {layer.name}"
                        f" (qgis-layer-id: {layer.id})"
                    )
                dataset.project = project_db
                dataset.name = layer.name
                dataset.title = layer.title
                dataset.bbox = layer.bbox.to_string()
                dataset.bbox_wgs84 = layer.bbox_wgs84.to_string()
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
                    f" ✓ Dataset {layer.name} (qgis-layer-id: {layer.id})"
                    f" was written to DB successfully."
                )
                logging.debug(" Handling of related fields.")
                for qsl_field in layer.fields:
                    field_qs = Field.objects.filter(
                        name=qsl_field.name,
                        type=qsl_field.type,
                        is_primary_key=qsl_field.is_primary_key,
                        type_wfs=qsl_field.type_wfs,
                        type_oapif=qsl_field.type_oapif,
                        type_oapif_format=qsl_field.type_oapif_format,
                        alias=qsl_field.alias,
                        comment=qsl_field.comment,
                        nullable=qsl_field.nullable,
                        length=qsl_field.length,
                        precision=qsl_field.precision,
                        vector_dataset=dataset,
                    )
                    if not field_qs.exists():
                        logging.debug(
                            f"   New Field {qsl_field.name} "
                            f"(type: {qsl_field.type}) will be added."
                        )
                        field = Field(
                            name=qsl_field.name,
                            type=qsl_field.type,
                            is_primary_key=qsl_field.is_primary_key,
                            type_wfs=qsl_field.type_wfs,
                            type_oapif=qsl_field.type_oapif,
                            type_oapif_format=qsl_field.type_oapif_format,
                            alias=qsl_field.alias,
                            comment=qsl_field.comment,
                            nullable=qsl_field.nullable,
                            length=qsl_field.length,
                            precision=qsl_field.precision,
                            vector_dataset=dataset,
                        )
                    else:
                        logging.debug(
                            f"   Field {qsl_field.name} (type: {qsl_field.type})"
                            f" was found and will be updated."
                        )
                        field: Field = field_qs.get()
                        field.name = qsl_field.name
                        field.type = qsl_field.type
                        field.is_primary_key = qsl_field.is_primary_key
                        field.type_wfs = qsl_field.type_wfs
                        field.type_oapif = qsl_field.type_oapif
                        field.type_oapif_format = qsl_field.type_oapif_format
                        field.alias = qsl_field.alias
                        field.comment = qsl_field.comment
                        field.nullable = qsl_field.nullable
                        field.length = qsl_field.length
                        field.precision = qsl_field.precision
                        field.vector_dataset = dataset
                    field.save()
                    logging.debug(
                        f"   ✓ Field {field.name} (type: {field.type})"
                        f" was written to DB successfully."
                    )
                logging.debug("   Cleaning out old fields...")
                for field_db in Field.objects.filter(vector_dataset=dataset).all():
                    field_match = layer.get_field_by_name(field_db.name)
                    if field_match is None:
                        logging.debug(
                            f'    Deleting field "{field.name}" of vector '
                            f"dataset {dataset.name}"
                            f" since it was"
                            " not in project config anymore"
                        )
                        field_db.delete()
                logging.debug("   ✓ Finished - Cleaning out old fields...")
        logging.debug(" Cleaning out old vector datasets.")
        for dataset_db in VectorDataSet.objects.filter(project=project_db).all():
            dataset_match = fss_project.find_config_dataset_by_id(
                project_config.datasets.vector, dataset_db.qgis_layer_id
            )
            if dataset_match is None:
                logging.debug(
                    f"    Deleting dataset {dataset_db.name} since it was not"
                    f" in project config anymore"
                )
                dataset_db.delete()
        logging.debug(" ✓ Finished - Cleaning out old vector datasets.")
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
                    f" Dataset was found and will be updated {layer.name}"
                    f" (qgis-layer-id: {layer.id})"
                )
            dataset.project = project_db
            dataset.name = layer.name
            dataset.title = layer.title
            dataset.bbox = layer.bbox.to_string()
            dataset.bbox_wgs84 = layer.bbox_wgs84.to_string()
            dataset.styles = DictEncoder().encode(layer.styles)
            dataset.driver = layer.driver
            dataset.source = DictEncoder().encode(layer.source)
            dataset.qgis_layer_id = layer.id
            dataset.crs = DictEncoder().encode(layer.crs)
            dataset.minimum_scale = layer.minimum_scale
            dataset.maximum_scale = layer.maximum_scale
            dataset.save()
            logging.debug(
                f" ✓ Dataset {layer.name} (qgis-layer-id: {layer.id})"
                f" was written to DB successfully."
            )
        logging.debug(" Cleaning out old rester datasets.")
        for dataset_db in RasterDataSet.objects.filter(project=project_db).all():
            dataset_match = FSService().find_config_dataset_by_id(
                project_config.datasets.raster, dataset_db.qgis_layer_id
            )
            if dataset_match is None:
                logging.debug(
                    f"  Deleting dataset {dataset_db.name} since it was not "
                    f" in project config anymore"
                )
                dataset_db.delete()
        logging.debug(" ✓ Finished - Cleaning out old raster datasets.")
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
                    f" Dataset was found and will be updated {layer.name}"
                    f" (qgis-layer-id: {layer.id})"
                )
            dataset.project = project_db
            dataset.name = layer.name
            dataset.title = layer.title
            dataset.bbox = layer.bbox.to_string()
            dataset.bbox_wgs84 = layer.bbox_wgs84.to_string()
            dataset.styles = DictEncoder().encode(layer.styles)
            dataset.driver = layer.driver
            dataset.source = DictEncoder().encode(layer.source)
            dataset.qgis_layer_id = layer.id
            dataset.crs = DictEncoder().encode(layer.crs)
            dataset.minimum_scale = layer.minimum_scale
            dataset.maximum_scale = layer.maximum_scale
            dataset.save()
        logging.debug(" Cleaning out old custom datasets.")
        for dataset_db in CustomDataSet.objects.filter(project=project_db).all():
            dataset_match = FSService().find_config_dataset_by_id(
                project_config.datasets.custom, dataset_db.qgis_layer_id
            )
            if dataset_match is None:
                logging.debug(
                    f"  Deleting dataset {dataset_db.name} since it was not"
                    f" in project config anymore"
                )
                dataset_db.delete()
        logging.debug(" ✓ Finished - Cleaning out old custom datasets.")
        logging.debug("✓ Finished - Handling of custom datasets")

        return None

    def count_db_projects(self) -> int:
        count = Project.objects.count()
        return count
