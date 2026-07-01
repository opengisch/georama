import pytest
from faker import Faker

from georama.core.common.faker import Provider as GeometryProvider


@pytest.mark.parametrize(
    "locale,expected_epsg_code",
    [
        ("de_CH", 2056),
        ("en_US", 4269),
        ("en_GB", 4326),
    ],
)
class TestGeomFaker:
    def test_general(self, locale, expected_epsg_code):
        fake = Faker(locale=locale)
        fake.add_provider(GeometryProvider)
        assert expected_epsg_code == fake.epsg_code
