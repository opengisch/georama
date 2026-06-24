import factory
from faker import Faker

from georama.features.models import FeatureLayer
from georama.integration.factories import VectorFactory

fake = Faker()


class FeatureLayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FeatureLayer
        django_get_or_create = ("datasource",)

    datasource = factory.SubFactory(VectorFactory)
