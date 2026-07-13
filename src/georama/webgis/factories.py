import random

import factory
from faker import Faker

from georama.integration.factories import ProjectFactory, VectorFactory
from georama.webgis.models import Theme
from georama.webgis.models.metadata import Metadata
from georama.webgis.models.wms_layer import WmsLayer

fake = Faker()


class MetadataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Metadata

    title = factory.Faker("word")
    description = factory.LazyAttribute(
        lambda obj: random.choice([fake.text(max_nb_chars=random.randint(20, 1000)), ""])
    )


class ThemeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Theme
        django_get_or_create = ("project",)

    project = factory.SubFactory(ProjectFactory)
    metadata = factory.SubFactory(MetadataFactory)
    ordering = factory.LazyAttribute(
        lambda obj: Theme.objects.last().ordering + 1 if Theme.objects.last() else 0
    )
    public = factory.Iterator([True, False])
    theme_json = {}


class WmsLayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WmsLayer
        django_get_or_create = ("datasource",)

    public = factory.Iterator([True, False])
    metadata = factory.SubFactory(MetadataFactory)
    datasource = factory.SubFactory(VectorFactory)
    theme = factory.SubFactory(ThemeFactory)
