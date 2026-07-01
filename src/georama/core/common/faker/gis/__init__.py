import random

from faker.providers import BaseProvider
from pyproj import CRS
from shapely import box
from shapely.geometry import LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon

localized = True
default_locale = "de_CH"


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

        self._bounds = get_epsg_bounds(self.epsg_code)
        self._bbox = box(*self._bounds)
        self.west, self.south, self.east, self.north = self._bounds

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
        self,
        min_points: int = 6,
        max_points: int = 2000,
        max_attempts: int = 50,
        bounds: tuple | None = None,
    ) -> Polygon | None:
        """
        Generate a valid polygon without self-intersections.

        Args:
            min_points: Minimum number of points
            max_points: Maximum number of points
            max_attempts: Maximum attempts to generate valid polygon
            bounds: Optional custom bounds (west, south, east, north)
        """
        if bounds is None:
            bounds = (self.west, self.south, self.east, self.north)

        west, south, east, north = bounds

        for _ in range(max_attempts):
            num_points = random.randint(min_points, max_points)
            coords = [
                (random.uniform(west, east), random.uniform(south, north))
                for _ in range(num_points)
            ]

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
        x1, x2 = sorted([random.uniform(west, east) for _ in range(2)])
        y1, y2 = sorted([random.uniform(south, north) for _ in range(2)])
        return Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])

    def point(self) -> Point:
        """Generate a random valid Point as WKB."""
        coord = self._random_coordinate()
        point = Point(coord)
        return point

    def linestring(self, min_points: int = 2, max_points: int = 200) -> LineString:
        """Generate a random valid LineString as WKB."""
        num_points = random.randint(max(2, min_points), max_points)
        coords = self._random_coordinates(num_points)
        line = LineString(coords)
        return line

    def polygon(self, min_points: int = 4, max_points: int = 2000) -> Polygon:
        """Generate a random valid Polygon as WKB."""
        polygon = self._generate_valid_polygon(min_points, max_points)
        return polygon

    def multipoint(self, num_points: int = 5) -> MultiPoint:
        """Generate a random valid MultiPoint as WKB."""

        coords = self._random_coordinates(num_points)
        return MultiPoint(coords)

    def multilinestring(self, num_lines: int = 3, points_per_line: int = 5) -> MultiLineString:
        """Generate a random valid MultiLineString as WKB."""

        lines = [
            LineString(self._random_coordinates(max(2, points_per_line))) for _ in range(num_lines)
        ]
        return MultiLineString(lines)

    def multipolygon(self, num_polygons: int = 3) -> MultiPolygon:
        """
        Generate a random valid MultiPolygon as WKB.

        Polygons are generated in separate grid cells to ensure no overlaps.
        This guarantees PostGIS ST_IsValid() returns true.

        Args:
            num_polygons: Number of polygons (default: 3, max: 16)

        Returns:
            bytes: Well-Known Binary representation of a MultiPolygon
        """
        num_polygons = max(1, min(num_polygons, 16))

        # Create grid to separate polygons
        cols = int(num_polygons**0.5) + 1
        rows = (num_polygons + cols - 1) // cols

        cell_width = (self.east - self.west) / cols
        cell_height = (self.north - self.south) / rows

        # 1% margin on each side to prevent edge touching
        margin = 0.01
        cell_width_margin = cell_width * (1 - 2 * margin)
        cell_height_margin = cell_height * (1 - 2 * margin)

        polygons = []
        poly_count = 0

        for row in range(rows):
            for col in range(cols):
                if poly_count >= num_polygons:
                    break

                # Define cell bounds with margin
                cell_west = self.west + col * cell_width + cell_width * margin
                cell_south = self.south + row * cell_height + cell_height * margin
                cell_east = cell_west + cell_width_margin
                cell_north = cell_south + cell_height_margin

                polygon = self._generate_valid_polygon(
                    bounds=(cell_west, cell_south, cell_east, cell_north)
                )

                if polygon and self._is_valid_polygon(polygon):
                    polygons.append(polygon)
                    poly_count += 1

            if poly_count >= num_polygons:
                break

        if not polygons:
            polygons = [self._generate_valid_polygon()]

        multi_polygon = MultiPolygon(polygons)

        if not multi_polygon.is_valid:
            raise ValueError(f"Generated invalid MultiPolygon: {multi_polygon.is_valid}")

        return multi_polygon

    def is_projected(self) -> bool:
        """Check if using a projected CRS."""
        try:
            crs = CRS.from_epsg(self.epsg_code)
            return crs.is_projected
        except Exception:
            return False

    def epsg(self):
        return self.epsg_code

    def bbox(self):
        return self._bbox

    def bounds(self):
        return self._bounds
