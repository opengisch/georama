from importlib import import_module

import pytest
from faker import Faker
from faker.utils.loading import find_available_providers
from shapely import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)

from georama.core.common.faker.gis import Dataset

META_PROVIDERS_MODULES = [
    "georama.core.common.faker",
]

PROVIDERS = find_available_providers(
    [import_module(path) for path in META_PROVIDERS_MODULES]
)


class TestGeomFaker:
    @pytest.mark.parametrize(
        "locale,expected_epsg_code",
        [
            ("de_CH", 2056),
            ("en_US", 4269),
            ("en_GB", 2056),  # we have not defined that locale, fallback is de_CH
        ],
    )
    def test_locale_epsg_matching(self, locale, expected_epsg_code):
        fake = Faker(locale=locale, providers=PROVIDERS)
        assert expected_epsg_code == fake.epsg()

    @pytest.mark.parametrize(
        "locale",
        [
            "de_CH",
            "en_US",
        ],
    )
    def test_point_generation(self, locale):
        fake = Faker(locale=locale, providers=PROVIDERS)
        geom = fake.point()
        assert isinstance(geom, Point)
        assert geom.is_valid
        assert geom.within(fake.bbox())

    @pytest.mark.parametrize(
        "locale",
        [
            "de_CH",
            "en_US",
        ],
    )
    def test_linestring_generation(self, locale):
        fake = Faker(locale=locale, providers=PROVIDERS)
        geom = fake.linestring()
        assert isinstance(geom, LineString)
        assert geom.is_valid
        assert geom.within(fake.bbox())

    @pytest.mark.parametrize(
        "locale",
        [
            "de_CH",
            "en_US",
        ],
    )
    def test_polygon_generation(self, locale):
        fake = Faker(locale=locale, providers=PROVIDERS)
        geom = fake.polygon()
        assert isinstance(geom, Polygon)
        assert geom.is_valid
        assert geom.within(fake.bbox())

    @pytest.mark.parametrize(
        "locale",
        [
            "de_CH",
            "en_US",
        ],
    )
    def test_multipoint_generation(self, locale):
        fake = Faker(locale=locale, providers=PROVIDERS)
        geom = fake.multipoint()
        assert isinstance(geom, MultiPoint)
        assert geom.is_valid
        assert geom.within(fake.bbox())

    @pytest.mark.parametrize(
        "locale",
        [
            "de_CH",
            "en_US",
        ],
    )
    def test_multilinestring_generation(self, locale):
        fake = Faker(locale=locale, providers=PROVIDERS)
        geom = fake.multilinestring()
        assert isinstance(geom, MultiLineString)
        assert geom.is_valid
        assert geom.within(fake.bbox())

    @pytest.mark.parametrize(
        "locale",
        [
            "de_CH",
            "en_US",
        ],
    )
    def test_multipolygon_generation(self, locale):
        fake = Faker(locale=locale, providers=PROVIDERS)
        geom = fake.multipolygon()
        assert isinstance(geom, MultiPolygon)
        assert geom.is_valid
        assert geom.within(fake.bbox())

    @pytest.mark.parametrize(
        "locale",
        [
            "de_CH",
            "en_US",
        ],
    )
    def test_vector_dataset_generation(self, locale):
        fake = Faker(locale=locale, providers=PROVIDERS)
        min_records = 1
        max_records = 5
        ds: Dataset = fake.vector_dataset(
            "dummy", min_records=min_records, max_records=max_records
        )
        assert ds.amount <= max_records
        assert ds.amount >= min_records
