import pytest
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse


@pytest.fixture
def fred():
    # fred signed in through keycloak, so his provider account exists
    fred = get_user_model().objects.create(username="fred.flintstone")
    SocialAccount.objects.create(user=fred, provider="keycloak", uid="f3c1e0a2-fred")
    yield fred
    fred.delete()


@pytest.fixture
def admin_client(admin_user):
    client = Client()
    client.force_login(admin_user)
    yield client


class TestUserAdmin:
    @pytest.mark.parametrize(
        "provider_account,listed,not_listed",
        [
            # limu only has a local account, the one to look at before the first
            # provider login with the same email
            ("not_linked", "limu", "fred.flintstone"),
            ("linked", "fred.flintstone", "limu"),
        ],
    )
    @pytest.mark.django_db
    def test_users_are_filtered_by_provider_account(
        self, admin_client, user, fred, provider_account, listed, not_listed
    ):
        response = admin_client.get(
            f"{reverse('admin:core_georamauser_changelist')}?provider_account={provider_account}",
            SERVER_NAME="localhost",
        )
        users = [user.username for user in response.context["cl"].result_list]
        assert listed in users
        assert not_listed not in users

    @pytest.mark.django_db
    def test_linked_provider_is_shown(self, admin_client, user, fred):
        response = admin_client.get(
            reverse("admin:core_georamauser_changelist"), SERVER_NAME="localhost"
        )
        # fred shows keycloak, limu the dash of a local account
        assert "keycloak" in response.text
        assert "–" in response.text
