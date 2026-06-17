import pytest

from georama.core.models.membership import Membership


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
