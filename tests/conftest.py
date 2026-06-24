import pytest

from georama.core.factories import (
    AdminUserFactory,
    MembershipFactory,
    OrganisationFactory,
    UserFactory,
)
from georama.integration.factories import CollectionFactory, ProjectFactory, VectorFactory


@pytest.fixture
def admin_user_name():
    yield "admin"


@pytest.fixture
def admin_password():
    yield "admin"


@pytest.fixture
def admin_email():
    yield "admin@example.org"


@pytest.fixture
def admin_user(admin_user_name, admin_password, admin_email):
    admin = AdminUserFactory.create(
        username=admin_user_name,
        email=admin_email,
        is_staff=True,
        is_superuser=True,
        password=admin_password,
    )
    yield admin
    admin.delete()


@pytest.fixture
def organisation():
    organisation = OrganisationFactory.create()
    yield organisation
    organisation.delete()


@pytest.fixture
def organisation_public_access():
    organisation = OrganisationFactory.create(public_access=True)
    yield organisation
    organisation.delete()


@pytest.fixture
def membership(organisation):
    membership = MembershipFactory.create(organisation=organisation)
    yield membership
    membership.delete()


@pytest.fixture
def membership_public_organisation(organisation_public_access):
    membership = MembershipFactory.create(organisation=organisation_public_access)
    yield membership
    membership.delete()


@pytest.fixture
def membership_global():
    membership = MembershipFactory.create(organisation=None)
    yield membership
    membership.delete()


@pytest.fixture
def user_user_name():
    yield "limu"


@pytest.fixture
def user_first_name():
    yield "Lieschen"


@pytest.fixture
def user_last_name():
    yield "Müller"


@pytest.fixture
def user_password():
    yield "oh-my-secret"


@pytest.fixture
def user_email(user_user_name):
    yield f"{user_user_name}@example.org"


@pytest.fixture
def user(user_user_name, user_first_name, user_last_name, user_email, user_password):
    user = UserFactory.create(
        username=user_user_name,
        password=user_password,
        first_name=user_first_name,
        last_name=user_last_name,
        email=user_email,
        is_staff=False,
        is_superuser=False,
    )
    yield user
    user.delete()


@pytest.fixture
def user_with_membership_global(user, membership_global):
    user.memberships.add(membership_global)
    user.save()
    yield user


@pytest.fixture
def collection_global_organisation():
    collection = CollectionFactory.create(
        name="Streets",
        organisation=None,
    )
    yield collection
    collection.delete()


@pytest.fixture
def collection_dedicated_organisation(organisation):
    collection = CollectionFactory.create(
        name="Rails",
        organisation=organisation,
    )
    yield collection
    collection.delete()


@pytest.fixture
def collections(collection_global_organisation, collection_dedicated_organisation):
    collections = [collection_dedicated_organisation, collection_global_organisation]
    yield collections


@pytest.fixture
def project_global_organisation(collection_global_organisation):
    project = ProjectFactory.create(collection=collection_global_organisation)
    yield project
    project.delete()


@pytest.fixture
def global_vector_dataset(project_global_organisation):
    vector = VectorFactory.create(project=project_global_organisation)
    yield vector
    vector.delete()
