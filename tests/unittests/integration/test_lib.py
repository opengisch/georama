from django.conf import settings

from georama.integration.lib.qgis_project_file_structure import QgisProject, QgisProjectCollection


class TestQgisProjectFileStructure:
    def test_qgis_project_collection_init(self):
        assert QgisProjectCollection("test").organisation == "test"

    def test_qgis_project_collection_glob_pattern(self):
        assert QgisProjectCollection("test").glob_pattern == "*.qg[sz]"

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
        assert p.root_path == settings.DATA_INTEGRATION_ROOT

    def test_qgis_project_assembles_integration_root_correctly(self, orga_a_project_file):
        test_path = settings.DATA_INTEGRATION_ROOT / orga_a_project_file.parent.name
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

    def test_qgis_project_has_expected_config_format(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert p.config_format == "json"

    def test_qgis_project_assembles_expected_config_path(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert p.config_path.suffix == "." + p.config_format

    def test_qgis_project_provides_correct_config_path_from_root(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert (
            str(p.config_path_from_root)
            == str(orga_a_project_file).replace(str(orga_a_project_file.parent.parent) + "/", "")
            + "."
            + p.config_format
        )

    def test_qgis_project_provides_correct_config_path_from_orga(self, orga_a_project_file):
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert (
            str(p.config_path_from_orga)
            == str(orga_a_project_file).replace(str(orga_a_project_file.parent) + "/", "")
            + "."
            + p.config_format
        )

    def test_qgis_project_has_no_config_as_expected(self, orga_a_project_random_file):
        orga_a_project_file = orga_a_project_random_file.with_suffix("")
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert not p.has_config

    def test_qgis_project_hash_is_none_on_nonexisting_config(self, orga_a_project_random_file):
        orga_a_project_file = orga_a_project_random_file.with_suffix("")
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert p.hash is None

    def test_qgis_project_has_config_as_expected(self, orga_b_project_config_file):
        orga_a_project_file = orga_b_project_config_file.with_suffix("")
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert p.has_config

    def test_qgis_project_delivers_hash_on_existing_config(self, orga_b_project_config_file):
        orga_a_project_file = orga_b_project_config_file.with_suffix("")
        p = QgisProject(orga_a_project_file, orga_a_project_file.parent.name)
        assert isinstance(p.hash, str)
