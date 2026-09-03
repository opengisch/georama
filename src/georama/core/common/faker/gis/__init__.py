import random
from collections.abc import Callable
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

from faker import Faker
from faker.providers import BaseProvider
from pyproj import CRS, Transformer
from shapely import box
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)

localized = True
default_locale = "de_CH"


@dataclass
class Field:
    name: str
    type: str
    alias: str
    nullable: bool
    type_oapif: str
    is_primary_key: bool
    length: int | None
    precision: int | None
    type_oapif_format: str
    type_wfs: str
    comment: str
    field_gen: Callable[[Faker], Any]


@dataclass
class Schema:
    name: str
    geom_gen: str
    fields: list[Field]


@dataclass
class Dataset:
    create_table_sql: str
    insert_values_sql: str
    selected_fields: list[Field]
    table_name: str
    geometry_field_name: str
    amount: int
    geometry_type_wkb: str
    geometry_type_simple: str
    name: str
    epsg_id: int


def get_epsg_bounds(
    epsg_code: int,
) -> tuple[tuple[float, float, float, float], tuple[float, float, float, float]]:
    """
    Retrieve the bounding box (minx, miny, maxx, maxy) for an EPSG code.
    Works with both geographic (degrees) and projected (meters) CRS.

    Returns:
        tuple: (west, south, east, north) in the CRS units
    """
    try:
        crs = CRS.from_epsg(epsg_code)
        if crs.area_of_use is not None:
            transformer = Transformer.from_crs("EPSG:4326", epsg_code, always_xy=True)
            wgs84_bounds = crs.area_of_use.bounds
            minx, miny, maxx, maxy = wgs84_bounds
            x1, y1 = transformer.transform(minx, miny)
            x2, y2 = transformer.transform(maxx, maxy)
            new_bounds = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
            return (
                new_bounds,
                wgs84_bounds,
            )  # (west/minx, south/miny, east/maxx, north/maxy)

        # Fallback for C.R.S without area_of_use
        if crs.is_geographic:
            return (-180, -90, 180, 90), (-180, -90, 180, 90)
        else:
            # For projected, try to infer reasonable bounds
            return (0, 0, 1000000, 1000000), (-180, -90, 180, 90)
    except Exception:
        return (-180, -90, 180, 90), (-180, -90, 180, 90)


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

    schemas: list[Schema] = [
        Schema(
            "cities",
            "point",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.city(),
                ),
                Field(
                    "visited",
                    "Date",
                    "Date of visit",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "date-time",
                    "dateTime",
                    "",
                    lambda faker: faker.date(pattern="%Y-%m-%d"),
                ),
                Field(
                    "distance",
                    "DECIMAL",
                    "Distance",
                    False,
                    "number",
                    False,
                    None,
                    None,
                    "double",
                    "decimal",
                    "",
                    lambda locale: Decimal(
                        f"{random.randint(0, 99999999)}.{random.randint(0, 99):02d}"
                    ),
                ),
                Field(
                    "video",
                    "VARCHAR",
                    "Video",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.file_path(depth=3, category="video"),
                ),
            ],
        ),
        Schema(
            "rivers",
            "linestring",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda locale: f"{Faker().name()} river",
                ),
                Field(
                    "flow_rate",
                    "DECIMAL",
                    "Flow Rate",
                    False,
                    "number",
                    False,
                    None,
                    2,
                    "double",
                    "decimal",
                    "",
                    lambda locale: Decimal(
                        f"{random.randint(0, 99999999)}.{random.randint(0, 99):02d}"
                    ),
                ),
            ],
        ),
        Schema(
            "poi",
            "point",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.word(),
                ),
                Field(
                    "comment",
                    "VARCHAR",
                    "Comment",
                    False,
                    "string",
                    False,
                    500,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.text(max_nb_chars=random.randint(20, 500)),
                ),
                Field(
                    "description",
                    "VARCHAR",
                    "Description",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.text(max_nb_chars=random.randint(20, 1000)),
                ),
            ],
        ),
        Schema(
            "labels",
            "point",
            [
                Field(
                    "text",
                    "VARCHAR",
                    "Text",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.word(),
                ),
            ],
        ),
        Schema(
            "streets",
            "linestring",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.street_name(),
                ),
                Field(
                    "local_residents",
                    "bigint",
                    "Local Residents",
                    False,
                    "integer",
                    False,
                    None,
                    None,
                    "int64",
                    "long",
                    "",
                    lambda faker: faker.random_int(),
                ),
            ],
        ),
        Schema(
            "buildings",
            "polygon",
            [
                Field(
                    "levels",
                    "bigint",
                    "Local Residents",
                    False,
                    "integer",
                    False,
                    None,
                    None,
                    "int64",
                    "long",
                    "",
                    lambda faker: faker.random_int(max=150),
                ),
            ],
        ),
        Schema(
            "landcover",
            "polygon",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda locale: random.choice(["rock", "forest", "water", "desert"]),
                ),
            ],
        ),
        Schema(
            "administrative_areas",
            "multipolygon",
            [
                Field(
                    "zip",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.zipcode(),
                ),
            ],
        ),
        Schema(
            "land_parcels",
            "multipolygon",
            [
                Field(
                    "owner",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda faker: faker.name(),
                ),
            ],
        ),
        Schema(
            "protected_zones",
            "multipolygon",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda locale: random.choice(
                        ["nature", "silence", "industrie", "small buildings"]
                    ),
                ),
            ],
        ),
        Schema(
            "river_system",
            "multilinestring",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda locale: random.choice(
                        [
                            "deranged drainage pattern",
                            "dendritic drainage pattern",
                            "parallel drainage pattern",
                            "radial drainage pattern",
                            "rectangular drainage pattern",
                            "trellis drainage pattern",
                        ]
                    ),
                ),
            ],
        ),
        Schema(
            "utility_lines",
            "multilinestring",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda locale: random.choice(
                        [
                            "power line",
                            "transmission line",
                            "overhead power line",
                            "underground power cable",
                            "gas pipeline",
                            "water pipeline",
                            "water main",
                            "sewer line",
                            "stormwater pipeline",
                            "district heating pipeline",
                            "district cooling pipeline",
                            "oil pipeline",
                            "product pipeline",
                            "telecommunication line",
                            "fiber-optic cable",
                            "telephone line",
                            "cable television line",
                        ]
                    ),
                ),
            ],
        ),
        Schema(
            "sampling_locations",
            "multipoint",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda locale: random.choice(
                        [
                            "water sampling site",
                            "groundwater monitoring well",
                            "stream gauging station",
                            "river sampling station",
                            "lake sampling station",
                            "reservoir sampling station",
                            "coastal sampling station",
                            "marine sampling station",
                            "soil sampling site",
                            "sediment sampling site",
                            "air quality monitoring station",
                            "weather station",
                            "meteorological station",
                            "ecological monitoring site",
                            "biodiversity monitoring site",
                            "vegetation plot",
                            "forest inventory plot",
                            "geological sampling site",
                            "mineral sampling site",
                            "drill site",
                            "borehole",
                            "core sampling site",
                            "test pit",
                        ]
                    ),
                ),
            ],
        ),
        Schema(
            "observation_sites",
            "multipoint",
            [
                Field(
                    "name",
                    "VARCHAR",
                    "Name",
                    False,
                    "string",
                    False,
                    None,
                    None,
                    "",
                    "string",
                    "",
                    lambda locale: random.choice(
                        [
                            "observation station",
                            "monitoring station",
                            "observation point",
                            "observation tower",
                            "lookout tower",
                            "camera trap station",
                            "hydrological observation station",
                            "meteorological observation station",
                            "air quality monitoring station",
                            "seismic station",
                            "geodetic station",
                            "volcano observatory",
                            "astronomical observatory",
                        ]
                    ),
                ),
            ],
        ),
    ]

    def __init__(self, generator):
        super().__init__(generator)
        self.sub_faker = Faker()
        self._bounds, self._bounds_wgs84 = get_epsg_bounds(self.epsg_code)
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

    def linestring(self, min_points: int = 2, max_points: int = 25) -> LineString:
        """Generate a random valid LineString as WKB."""
        num_points = random.randint(max(2, min_points), max_points)
        coords = self._random_coordinates(num_points)
        line = LineString(coords)
        return line

    def polygon(self, min_points: int = 4, max_points: int = 50) -> Polygon:
        """Generate a random valid Polygon as WKB."""
        polygon = self._generate_valid_polygon(min_points, max_points)
        return polygon

    def multipoint(self, num_points: int = 5) -> MultiPoint:
        """Generate a random valid MultiPoint as WKB."""

        coords = self._random_coordinates(num_points)
        return MultiPoint(coords)

    def multilinestring(
        self, num_lines: int = 3, points_per_line: int = 5
    ) -> MultiLineString:
        """Generate a random valid MultiLineString as WKB."""

        lines = [
            LineString(self._random_coordinates(max(2, points_per_line)))
            for _ in range(num_lines)
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
            raise ValueError(
                f"Generated invalid MultiPolygon: {multi_polygon.is_valid}"
            )

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

    def bounds_wgs84(self):
        return self._bounds_wgs84

    def vector_dataset(self, db_schema: str, min_records=10, max_records=50):
        schema: Schema = random.choice(self.schemas)
        fields: list[Field] = random.sample(
            schema.fields, random.randint(1, len(schema.fields))
        )
        table_name = f"{schema.name}_{self.sub_faker.unique.word()}"
        geometry_field_name = self.geometry_column_name()
        create_sql = self._produce_create_sql(
            fields, table_name, schema.geom_gen, db_schema, geometry_field_name
        )
        amount = random.randint(min_records, max_records)
        insert_sql = self._produce_insert_sql(
            fields, table_name, db_schema, schema.geom_gen, geometry_field_name, amount
        )
        return Dataset(
            create_sql,
            insert_sql,
            fields,
            table_name,
            geometry_field_name,
            amount,
            schema.geom_gen,
            self.geom_type_simple(schema.geom_gen),
            schema.name,
            self.epsg_code,
        )

    def geom_type_simple(self, geom_gen: str):
        if geom_gen in ["point", "multipoint"]:
            return "point"
        elif geom_gen in ["linestring", "multilinestring"]:
            return "line"
        elif geom_gen in ["polygon", "multipolygon"]:
            return "polygon"
        else:
            raise LookupError(
                f"Geomtry type not available for simplifiaciton: {geom_gen}"
            )

    def vector_datasets(self, db_schema: str, amount=5, min_records=10, max_records=50):
        return [
            self.vector_dataset(
                db_schema, min_records=min_records, max_records=max_records
            )
            for _ in range(amount)
        ]

    def _produce_insert_sql(
        self,
        fields: list[Field],
        table_name: str,
        db_schema: str,
        geom_gen: str,
        geometry_field_name: str,
        amount: int,
    ):
        field_names = [field.name for field in fields] + [geometry_field_name]
        return f"""
        INSERT INTO {db_schema}.{table_name} ({", ".join(field_names)})
        VALUES
        {",\n".join(self._produce_insert_sql_values(fields, geom_gen, amount))};
        """

    def _produce_insert_sql_values(
        self, fields: list[Field], geom_gen: str, amount: int
    ):
        return [self._produce_insert_sql_value(fields, geom_gen) for _ in range(amount)]

    def _produce_insert_sql_value(self, fields: list[Field], geom_gen: str):
        field_values = []

        for field in fields:
            if field.type.upper() in ["VARCHAR", "DATE"]:
                field_values.append(f"'{field.field_gen(self.sub_faker)}'")
            elif field.type.upper() in ["BIGINT", "DECIMAL"]:
                field_values.append(f"{field.field_gen(self.sub_faker)}")
            else:
                raise LookupError(f"No matched type for {field}")
        field_values.append(
            f"ST_GeomFromWKB('\\x{getattr(self, geom_gen)().wkb.hex()}', {self.epsg_code})"
        )
        return f"({', '.join(field_values)})"

    def _produce_create_sql(
        self,
        fields: list[Field],
        table_name: str,
        geom_type: str,
        db_schema: str,
        geometry_field_name: str,
    ):
        field_parts = [
            self._produce_create_sql_pk_part(),
            self._produce_create_sql_geom_part(geom_type, geometry_field_name),
        ] + self._produce_create_sql_field_parts(fields)
        return f"""
        CREATE TABLE {db_schema}.{table_name} (
            {", ".join(field_parts)}
        );
        """

    def _produce_create_sql_pk_part(self):
        return "id uuid DEFAULT gen_random_uuid() PRIMARY KEY"

    def geometry_column_name(self):
        return random.choice(["geom", "geometry", "the_geom", "g"])

    def _produce_create_sql_geom_part(
        self, geometry_type: str, geometry_field_name: str
    ):
        return (
            f"{geometry_field_name} geometry({geometry_type.upper()},{self.epsg_code})"
        )

    def _produce_create_sql_field_parts(self, fields: list[Field]) -> list[str]:
        return [self._produce_create_sql_field_part(field) for field in fields]

    def _produce_create_sql_field_part(self, field: Field) -> str:
        if field.type.upper() == "VARCHAR":
            return self._produce_create_sql_field_part_varchar(field)
        elif field.type.upper() == "DATE":
            return self._produce_create_sql_field_part_date(field)
        elif field.type.upper() in ["BIGINT"]:
            return self._produce_create_sql_field_part_int(field)
        elif field.type.upper() == "DECIMAL":
            return self._produce_create_sql_field_part_decimal(field)
        else:
            raise LookupError(f"No matched type for {field}")

    def _produce_create_sql_field_part_varchar(self, field: Field) -> str:
        field_def = f"{field.name} {field.type.upper()}"
        if field.length:
            field_def += f"({field.length})"
        return field_def

    def _produce_create_sql_field_part_date(self, field: Field) -> str:
        return f"{field.name} {field.type.upper()}"

    def _produce_create_sql_field_part_int(self, field: Field) -> str:
        return f"{field.name} {field.type.upper()}"

    def _produce_create_sql_field_part_decimal(self, field: Field) -> str:
        field_def = f"{field.name} {field.type.upper()}"
        if field.precision:
            field_def += f"(10,{field.precision})"
        return field_def
