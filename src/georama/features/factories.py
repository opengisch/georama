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
    description = factory.Faker("word")


class FeatureLayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FeatureLayer
        django_get_or_create = ("datasource",)

    metadata = factory.SubFactory(MetadataFactory)
    datasource = factory.SubFactory(VectorFactory)
