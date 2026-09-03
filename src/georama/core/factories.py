import random

import factory
from django.contrib.auth.models import Group

from georama.core.models.membership import Membership
from georama.core.models.organisation import Organisation
from georama.core.models.user import GeoramaUser

ORGANISATIONS = [
    ("OpenSky", "os"),
    ("OpenEye", "oe"),
    ("OpenWindow", "ow"),
]


class OrganisationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organisation
        django_get_or_create = ("domain",)
        skip_postgeneration_save = True

    name = factory.Sequence(lambda n: ORGANISATIONS[n % len(ORGANISATIONS)][0])
    domain = factory.Sequence(lambda n: ORGANISATIONS[n % len(ORGANISATIONS)][1])


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ("name",)
        skip_postgeneration_save = True

    name = factory.Iterator(
        [
            "Manager",
            "Publisher",
            "ContentReader",
            "ContentEditor",
        ]
    )


class AdminUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GeoramaUser
        django_get_or_create = ("username",)
        skip_postgeneration_save = True

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = "admin"
    is_staff = True
    is_superuser = True
    password = factory.django.Password("admin")


class UserFactory(AdminUserFactory):
    class Meta:
        model = GeoramaUser
        django_get_or_create = ("username",)
        skip_postgeneration_save = True

    username = factory.Faker("user_name")
    is_staff = factory.Iterator([True, False])
    is_superuser = False

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if create:
            self.set_password(extracted if extracted else self.username)
            self.save()

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create or self.is_superuser:
            return
        if extracted:
            # A list of types were passed in, use them
            for group in extracted:
                self.groups.add(group)
        else:
            group = GroupFactory()
            self.groups.set((group,))


class MembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Membership
        django_get_or_create = (
            "user",
            "organisation",
        )
        skip_postgeneration_save = True

    user = factory.SubFactory(UserFactory)
    organisation = factory.LazyAttribute(
        lambda obj: random.choice([None, OrganisationFactory()])
    )
