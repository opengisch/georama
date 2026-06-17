import pytest

from georama.core.factories import AdminUserFactory, MembershipFactory, OrganisationFactory


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
