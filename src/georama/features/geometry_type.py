from georama.core.exceptions.base import GeoramaBaseError

# Maps the WKB type names (Qgis.WkbType) QSL delivers in `geometry_type_wkb` to the
# GeoJSON (RFC 7946) geometry type. `None` marks types which have no GeoJSON
# equivalent (no geometry, curves, surfaces). They can't be published.
GEOJSON_GEOMETRY_TYPES: dict[str, str | None] = {
    "Unknown": None,
    "NoGeometry": None,
    "UNSET": None,
    "Point": "Point",
    "PointZ": "Point",
    "PointM": "Point",
    "PointZM": "Point",
    "Point25D": "Point",
    "LineString": "LineString",
    "LineStringZ": "LineString",
    "LineStringM": "LineString",
    "LineStringZM": "LineString",
    "LineString25D": "LineString",
    "Polygon": "Polygon",
    "PolygonZ": "Polygon",
    "PolygonM": "Polygon",
    "PolygonZM": "Polygon",
    "Polygon25D": "Polygon",
    "Triangle": "Polygon",
    "TriangleZ": "Polygon",
    "TriangleM": "Polygon",
    "TriangleZM": "Polygon",
    "MultiPoint": "MultiPoint",
    "MultiPointZ": "MultiPoint",
    "MultiPointM": "MultiPoint",
    "MultiPointZM": "MultiPoint",
    "MultiPoint25D": "MultiPoint",
    "MultiLineString": "MultiLineString",
    "MultiLineStringZ": "MultiLineString",
    "MultiLineStringM": "MultiLineString",
    "MultiLineStringZM": "MultiLineString",
    "MultiLineString25D": "MultiLineString",
    "MultiPolygon": "MultiPolygon",
    "MultiPolygonZ": "MultiPolygon",
    "MultiPolygonM": "MultiPolygon",
    "MultiPolygonZM": "MultiPolygon",
    "MultiPolygon25D": "MultiPolygon",
    "GeometryCollection": "GeometryCollection",
    "GeometryCollectionZ": "GeometryCollection",
    "GeometryCollectionM": "GeometryCollection",
    "GeometryCollectionZM": "GeometryCollection",
    "CircularString": None,
    "CircularStringZ": None,
    "CircularStringM": None,
    "CircularStringZM": None,
    "CompoundCurve": None,
    "CompoundCurveZ": None,
    "CompoundCurveM": None,
    "CompoundCurveZM": None,
    "NurbsCurve": None,
    "NurbsCurveZ": None,
    "NurbsCurveM": None,
    "NurbsCurveZM": None,
    "CurvePolygon": None,
    "CurvePolygonZ": None,
    "CurvePolygonM": None,
    "CurvePolygonZM": None,
    "MultiCurve": None,
    "MultiCurveZ": None,
    "MultiCurveM": None,
    "MultiCurveZM": None,
    "MultiSurface": None,
    "MultiSurfaceZ": None,
    "MultiSurfaceM": None,
    "MultiSurfaceZM": None,
    "PolyhedralSurface": None,
    "PolyhedralSurfaceZ": None,
    "PolyhedralSurfaceM": None,
    "PolyhedralSurfaceZM": None,
    "TIN": None,
    "TINZ": None,
    "TINM": None,
    "TINZM": None,
}


class UnsupportedGeometryTypeError(GeoramaBaseError):
    def __init__(self, geometry_type_wkb: str):
        super().__init__(
            f"The geometry type '{geometry_type_wkb}' of the datasource has no GeoJSON equivalent."
        )


def geojson_geometry_type(geometry_type_wkb: str) -> str:
    """Maps the WKB geometry type name delivered by QSL to its GeoJSON geometry type.

    Args:
        geometry_type_wkb: The name of the QGIS WKB type, eg. `MultiPolygonZ`.

    Returns:
        The GeoJSON geometry type, eg. `MultiPolygon`.

    Raises:
        UnsupportedGeometryTypeError: If the type has no GeoJSON equivalent or is unknown.
    """
    geometry_type = GEOJSON_GEOMETRY_TYPES.get(geometry_type_wkb)
    if geometry_type is None:
        raise UnsupportedGeometryTypeError(geometry_type_wkb)
    return geometry_type
