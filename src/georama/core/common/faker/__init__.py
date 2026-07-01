import random

from faker.providers import BaseProvider
from pyproj import CRS
from shapely.geometry import LineString, Point, Polygon

localized = True


def get_epsg_bounds(epsg_code: int) -> tuple:
    """
    Retrieve the bounding box (minx, miny, maxx, maxy) for an EPSG code.
    Works with both geographic (degrees) and projected (meters) CRS.

    Returns:
        tuple: (west, south, east, north) in the CRS units
    """
    try:
        crs = CRS.from_epsg(epsg_code)
        if crs.area_of_use is not None:
            bounds = crs.area_of_use.bounds
            return bounds  # (west/minx, south/miny, east/maxx, north/maxy)

        # Fallback for C.R.S without area_of_use
        if crs.is_geographic:
            return (-180, -90, 180, 90)
        else:
            # For projected, try to infer reasonable bounds
            return (0, 0, 1000000, 1000000)
    except Exception:
        return (-180, -90, 180, 90)


class Provider(BaseProvider):
    """
    Faker provider for generating random valid geometries as WKB.

    Supports all Faker locale variants with intelligent EPSG selection:
    - Uses local projected EPSG codes where available (e.g., EPSG:2056 for Switzerland)
    - Falls back to geographic CRS for other regions

    Usage:
        from faker import Faker

        # Swiss German → uses EPSG:2056 (LV95, projected)
        fake = Faker('de_CH')
        fake.add_provider(GeometryProvider)

        point = fake.wkb_point()
        print(f"EPSG: {fake.epsg_code()}")  # Output: EPSG: 2056
        print(f"Bounds: {fake.geometry_bounds()}")  # In meters: (2683000, 1247000, ...)
    """

    epsg_code: int = 4326

    def __init__(self, generator):
        super().__init__(generator)

        self.bounds = get_epsg_bounds(self.epsg_code)
        self.west, self.south, self.east, self.north = self.bounds

    def _random_coordinate(self) -> tuple:
        """Generate a random coordinate within the EPSG bounds."""
        x = random.uniform(self.west, self.east)
        y = random.uniform(self.south, self.north)
        return (x, y)

    def _random_coordinates(self, count: int) -> list:
        """Generate multiple random coordinates."""
        return [self._random_coordinate() for _ in range(count)]

    def _is_valid_polygon(self, polygon: Polygon) -> bool:
        """Check if polygon is valid."""
        return polygon.is_valid and polygon.exterior.is_ring

    def _generate_valid_polygon(
        self, min_points: int = 4, max_points: int = 20, max_attempts: int = 50
    ) -> Polygon | None:
        """Generate a valid polygon without self-intersections."""
        for _ in range(max_attempts):
            num_points = random.randint(min_points, max_points)
            coords = self._random_coordinates(num_points)

            try:
                polygon = Polygon(coords)

                if not self._is_valid_polygon(polygon):
                    polygon = Polygon(coords).convex_hull
                    if isinstance(polygon, Polygon) and self._is_valid_polygon(polygon):
                        return polygon
                else:
                    return polygon
            except Exception:
                continue

        # Fallback: simple rectangle
        x1, x2 = sorted([random.uniform(self.west, self.east) for _ in range(2)])
        y1, y2 = sorted([random.uniform(self.south, self.north) for _ in range(2)])
        return Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])

    def wkb_point(self) -> bytes:
        """Generate a random valid Point as WKB."""
        coord = self._random_coordinate()
        point = Point(coord)
        return point.wkb

    def wkb_linestring(self, min_points: int = 2, max_points: int = 20) -> bytes:
        """Generate a random valid LineString as WKB."""
        num_points = random.randint(max(2, min_points), max_points)
        coords = self._random_coordinates(num_points)
        line = LineString(coords)
        return line.wkb

    def wkb_polygon(self, min_points: int = 4, max_points: int = 20) -> bytes:
        """Generate a random valid Polygon as WKB."""
        polygon = self._generate_valid_polygon(min_points, max_points)
        return polygon.wkb

    def wkb_multipoint(self, num_points: int = 5) -> bytes:
        """Generate a random valid MultiPoint as WKB."""
        from shapely.geometry import MultiPoint

        coords = self._random_coordinates(num_points)
        return MultiPoint(coords).wkb

    def wkb_multilinestring(self, num_lines: int = 3, points_per_line: int = 5) -> bytes:
        """Generate a random valid MultiLineString as WKB."""
        from shapely.geometry import MultiLineString

        lines = [
            LineString(self._random_coordinates(max(2, points_per_line))) for _ in range(num_lines)
        ]
        return MultiLineString(lines).wkb

    def wkb_multipolygon(self, num_polygons: int = 3) -> bytes:
        """Generate a random valid MultiPolygon as WKB."""
        from shapely.geometry import MultiPolygon

        polygons = [self._generate_valid_polygon() for _ in range(num_polygons)]
        return MultiPolygon(polygons).wkb

    def geometry_bounds(self) -> tuple:
        """Return the (west, south, east, north) bounds."""
        return self.bounds

    def is_projected(self) -> bool:
        """Check if using a projected CRS."""
        try:
            crs = CRS.from_epsg(self.epsg_code)
            return crs.is_projected
        except Exception:
            return False
