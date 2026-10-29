import pytest
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from georama.core.models.membership import Membership

SUBDOMAIN_REGEX = r"^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?(\.[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?)?$"


@pytest.mark.django_db
def test_membership(membership):
    qs = Membership.objects.organisation_objects(membership.organisation)
    assert qs.count() == 1
    assert all(m.organisation == membership.organisation for m in qs)


@pytest.mark.django_db
def test_membership_global(membership_global):
    qs = Membership.objects.organisation_objects(membership_global.organisation)
    assert qs.count() == 1
    assert all(m.organisation == membership_global.organisation for m in qs)


@pytest.mark.parametrize(
    "value, is_valid",
    [
        ("hello", True),
        ("hello.com", True),
        ("hello_com", False),
        (".hello.com", False),
    ],
)
def test_domain_regex(value, is_valid):
    validator = RegexValidator(SUBDOMAIN_REGEX)
    if not is_valid:
        with pytest.raises(ValidationError):
            validator(value)
    else:
        validator(value)
