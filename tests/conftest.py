from pathlib import Path

import pytest

from georama.core.factories import (
    AdminUserFactory,
    MembershipFactory,
    OrganisationFactory,
    UserFactory,
)
from tests.fixtures import reseed
from tests.fixtures.gis import create_project

pytest_plugins = [
    "tests.fixtures.gis",
    "tests.fixtures.layers",
    "tests.fixtures.personas",
    "tests.fixtures.qsl",
    "tests.fixtures.testmandant",
]


@pytest.fixture(autouse=True)
def seed():
    reseed()


@pytest.fixture(autouse=True)
def data_integration_root(settings, tmp_path) -> Path:
    """Keeps the folders created by the code (organisations, projects) out of the repository."""
    root = tmp_path / "projects"
    (root / settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER).mkdir(parents=True)
    settings.DATA_INTEGRATION_ROOT = root
    return root


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
    return AdminUserFactory.create(
        username=admin_user_name,
        email=admin_email,
        is_staff=True,
        is_superuser=True,
        password=admin_password,
    )


@pytest.fixture
def organisation():
    return OrganisationFactory.create()


@pytest.fixture
def organisation_public_access():
    return OrganisationFactory.create(public_access=True)


@pytest.fixture
def organisation_non_public_access():
    return OrganisationFactory.create(public_access=False)


@pytest.fixture
def project_global_organisation(db):
    return create_project()


@pytest.fixture
def membership(organisation):
    return MembershipFactory.create(organisation=organisation)


@pytest.fixture
def membership_public_organisation(organisation_public_access):
    return MembershipFactory.create(organisation=organisation_public_access)


@pytest.fixture
def membership_global(db):
    return MembershipFactory.create(organisation=None)


@pytest.fixture
def membership_non_public_organisation(organisation_non_public_access):
    return MembershipFactory.create(organisation=organisation_non_public_access)


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
    return UserFactory.create(
        username=user_user_name,
        password=user_password,
        first_name=user_first_name,
        last_name=user_last_name,
        email=user_email,
        is_staff=False,
        is_superuser=False,
        groups=[],
    )


@pytest.fixture
def user_with_membership_global(user, membership_global):
    user.memberships.add(membership_global)
    user.save()
    yield user


@pytest.fixture
def user_with_dedicated_membership_non_public(user, membership_non_public_organisation):
    user.memberships.add(membership_non_public_organisation)
    user.save()
    yield user
