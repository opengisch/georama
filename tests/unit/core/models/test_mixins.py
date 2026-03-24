from georama.core.models.mixins import GeoramaPermissionMixin


class TestGeoramaPermissionMixin:
    def test_assemble_perm(self):
        assert GeoramaPermissionMixin.assemble_perm("a", "b") == "a.b"

    def test_perm(self):
        assert GeoramaPermissionMixin.perm("add") == "core.add_georamapermissionmixin"

    def test_add(self):
        assert GeoramaPermissionMixin.perm_add() == "core.add_georamapermissionmixin"

    def test_change(self):
        assert GeoramaPermissionMixin.perm_change() == "core.change_georamapermissionmixin"

    def test_delete(self):
        assert GeoramaPermissionMixin.perm_delete() == "core.delete_georamapermissionmixin"

    def test_view(self):
        assert GeoramaPermissionMixin.perm_view() == "core.view_georamapermissionmixin"
