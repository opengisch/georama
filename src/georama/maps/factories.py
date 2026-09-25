import random

import factory
from faker import Faker

from georama.integration.factories import VectorFactory
from georama.maps.models import WmsLayer
from georama.maps.models.metadata import Metadata

fake = Faker()


class MetadataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Metadata

    title = factory.Faker("word")
    description = factory.LazyAttribute(
        lambda obj: random.choice([fake.text(max_nb_chars=random.randint(20, 1000)), ""])
    )


class WmsLayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WmsLayer

    public = factory.Iterator([True, False])
    queryable = factory.Iterator([True, False])
    metadata = factory.SubFactory(MetadataFactory)
    datasource = factory.SubFactory(VectorFactory)
    extent = factory.LazyFunction(
        lambda: ",".join(
            [str(float(x)) for x in fake.latlng()] + [str(float(x)) for x in fake.latlng()]
        )
    )
    extent_wgs84 = factory.LazyFunction(
        lambda: ",".join(
            [str(float(x)) for x in fake.latlng()] + [str(float(x)) for x in fake.latlng()]
        )
    )
