from datetime import datetime
from pathlib import Path

from django.conf import settings

from georama.integration.lib.qgis_project_file_structure import QgisProject, QgisProjectCollection


class TestQgisProjectFileStructure:
    def test_qgis_project_collection_init(self):
        assert QgisProjectCollection("test").organisation == "test"

    def test_qgis_project_collection_glob_pattern(self):
        assert QgisProjectCollection("test").glob_pattern() == "*.qg[sz]"

    def test_qgis_project_collection_glob_pattern_filtered(self):
        assert QgisProjectCollection("test").glob_pattern("hello") == "*hello*.qg[sz]"

    def test_qgis_project_collection_return_empty_list_on_empty_folder(self, organisation_a_folder):
        pl = QgisProjectCollection(organisation_a_folder.name).projects()
        assert len(pl) == 0

    def test_qgis_project_collection_return_list_when_project_file(self, orga_a_project_file):
        pl = QgisProjectCollection(orga_a_project_file.parent.name).projects()
        assert len(pl) == 1
        assert pl[0].organisation == orga_a_project_file.parent.name

    def test_qgis_project_collection_filtered_by_orga(
        self, orga_a_project_file, orga_b_project_file
    ):
        pl = QgisProjectCollection(orga_a_project_file.parent.name).projects()
        assert len(pl) == 1
        assert pl[0].organisation == orga_a_project_file.parent.name

    def test_qgis_project_collection_finds_qgs_and_qgz(
        self, orga_a_project_file, orga_b_project_file
    ):
        pl = QgisProjectCollection(orga_a_project_file.parent.name).projects()
        assert len(pl) == 1
        pl = QgisProjectCollection(orga_b_project_file.parent.name).projects()
        assert len(pl) == 1

    def test_qgis_project_collection_filters_as_expected(
        self, orga_a_project_file, orga_b_project_file
    ):
        pc = QgisProjectCollection(orga_a_project_file.parent.name)
        pl = pc.projects_filtered({orga_a_project_file.relative_to(orga_a_project_file.parent)})
        assert len(pl) == 0
        pl = pc.projects_filtered({orga_b_project_file.relative_to(orga_b_project_file.parent)})
        assert len(pl) == 1

    def test_qgis_project_has_correct_root_path(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert p.root_path == Path(settings.DATA_INTEGRATION_ROOT)

    def test_qgis_project_assembles_integration_root_correctly(self, orga_a_project_file):
        test_path = Path(settings.DATA_INTEGRATION_ROOT) / orga_a_project_file.parent.name
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert p.integration_root == test_path

    def test_qgis_project_assembles_project_path_correctly(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert p.project_path == orga_a_project_file
        assert p.project_path.exists()

    def test_qgis_project_provides_correct_path_from_root(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert str(p.path_from_root) == str(orga_a_project_file).replace(
            str(orga_a_project_file.parent.parent) + "/", ""
        )

    def test_qgis_project_provides_correct_path_from_orga(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert str(p.path_from_orga) == str(orga_a_project_file).replace(
            str(orga_a_project_file.parent) + "/", ""
        )

    def test_qgis_project_has_modification_date_of_file_on_disk(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        # the date comes from the project file itself, there is no sidecar file anymore
        assert p.modification_date == datetime.fromtimestamp(orga_a_project_file.stat().st_mtime)

    def test_qgis_project_has_no_modification_date_when_file_is_missing(
        self, organisation_a_folder
    ):
        p = QgisProject(Path("missing.qgs"), organisation_a_folder.name)
        # a project file which is gone has no date, the badge shows it as stale then
        assert p.modification_date is None
