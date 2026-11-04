import random

import factory
from faker import Faker

from georama.features.models import FeatureLayer
from georama.features.models.metadata import Metadata
from georama.integration.factories import VectorFactory

fake = Faker()

# Feature layers are served via OAPIF which supports GeoJSON compatible types only.
GEOMETRY_TYPES = [
    # geometry_type_simple, geometry_type_wkb
    ("Point", "Point"),
    ("Line", "LineString"),
    ("Polygon", "Polygon"),
    ("Point", "MultiPoint"),
    ("Line", "MultiLineString"),
    ("Polygon", "MultiPolygon"),
]


class MetadataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Metadata

    title = factory.Faker("word")
    description = factory.LazyAttribute(
        lambda obj: random.choice([fake.text(max_nb_chars=random.randint(20, 1000)), ""])
    )


class FeatureLayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FeatureLayer

    public = factory.Iterator([True, False])
    metadata = factory.SubFactory(MetadataFactory)
    datasource = factory.SubFactory(
        VectorFactory,
        geometry_type_simple=factory.Sequence(lambda n: GEOMETRY_TYPES[n % len(GEOMETRY_TYPES)][0]),
        geometry_type_wkb=factory.Sequence(lambda n: GEOMETRY_TYPES[n % len(GEOMETRY_TYPES)][1]),
    )
