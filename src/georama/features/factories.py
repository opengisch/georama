import random

import factory
from faker import Faker

from georama.features.models import FeatureLayer
from georama.features.models.metadata import Metadata
from georama.integration.factories import VectorFactory

fake = Faker()


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
        django_get_or_create = ("datasource",)

    public = factory.Iterator([True, False])
    metadata = factory.SubFactory(MetadataFactory)
    datasource = factory.SubFactory(VectorFactory)
