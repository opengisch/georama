import pytest

from georama.features.geometry_type import UnsupportedGeometryTypeError, geojson_geometry_type


class TestGeojsonGeometryType:
    @pytest.mark.parametrize(
        "geometry_type_wkb, expected",
        [
            ("Point", "Point"),
            ("PointZM", "Point"),
            ("Point25D", "Point"),
            ("LineStringM", "LineString"),
            ("TriangleZ", "Polygon"),
            ("MultiPolygon", "MultiPolygon"),
            ("MultiPolygonZ", "MultiPolygon"),
            ("GeometryCollectionZ", "GeometryCollection"),
        ],
    )
    def test_maps_to_geojson_type(self, geometry_type_wkb, expected):
        assert geojson_geometry_type(geometry_type_wkb) == expected

    @pytest.mark.parametrize(
        "geometry_type_wkb",
        [
            "Unknown",
            "NoGeometry",
            "UNSET",
            "CircularString",
            "CompoundCurveZ",
            "NurbsCurveZM",
            "CurvePolygon",
            "MultiCurveM",
            "MultiSurfaceZ",
            "PolyhedralSurface",
            "TINZ",
            "",
            "Polyline",
            "point",
        ],
    )
    def test_type_without_geojson_equivalent_raises(self, geometry_type_wkb):
        with pytest.raises(UnsupportedGeometryTypeError, match=f"'{geometry_type_wkb}'"):
            geojson_geometry_type(geometry_type_wkb)
