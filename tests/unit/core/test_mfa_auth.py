import pytest
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.test import Client, override_settings

CACHES_LOCMEM = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}


@pytest.mark.django_db
def test_login_redirects_to_allauth(client: Client):
    """GET /login returns a 302 redirect to /accounts/login/.

    Validates: Requirements 1.4 (Correctness Property 6)
    """
    response = client.get("/login")
    assert response.status_code == 302
    assert response["Location"] == "/accounts/login/"


@pytest.mark.django_db
def test_admin_login_redirects_to_allauth(client: Client):
    """Unauthenticated access to /admin/login/ redirects to allauth login.

    Validates: Requirement 1.2
    """
    response = client.get("/admin/login/")
    assert response.status_code == 302
    assert response["Location"] == "/accounts/login/"


@pytest.mark.django_db
def test_staff_without_mfa_redirected_to_enrollment(client: Client):
    """Staff user without MFA enrolled is redirected to enrollment page.

    Validates: Requirement 3.1, 3.2 (Correctness Property 2)
    """
    user = User.objects.create_user("staffuser", "staff@test.com", "password123", is_staff=True)
    client.force_login(user)
    response = client.get("/settings")
    assert response.status_code == 302
    assert response["Location"] == "/accounts/2fa/"


@pytest.mark.django_db
def test_non_staff_user_bypasses_mfa_enforcement(client: Client):
    """Non-staff user can access protected views without MFA enrollment.

    Validates: Requirement 3.3 (Correctness Property 3)
    """
    user = User.objects.create_user("regularuser", "user@test.com", "password123")
    client.force_login(user)
    response = client.get("/settings")
    # Non-staff user should NOT be redirected to MFA enrollment
    assert not (response.status_code == 302 and response.get("Location") == "/accounts/2fa/")


@pytest.mark.django_db
def test_social_account_user_bypasses_mfa_enforcement(client: Client):
    """Staff user with linked SocialAccount bypasses MFA enforcement.

    Validates: Requirement 7.2 (Correctness Property 4)
    """
    user = User.objects.create_user("oidcuser", "oidc@test.com", "password123", is_staff=True)
    SocialAccount.objects.create(
        user=user,
        provider="openid_connect",
        uid="keycloak-uid-12345",
        extra_data={"sub": "keycloak-uid-12345"},
    )
    client.force_login(user)
    response = client.get("/settings")
    # Staff user with SocialAccount should NOT be redirected to MFA enrollment
    assert not (response.status_code == 302 and response.get("Location") == "/accounts/2fa/")


@pytest.mark.django_db
def test_post_login_without_csrf_rejected(client: Client):
    """POST to login endpoint without CSRF token is rejected with 403.

    Validates: Requirement 6.4 (Correctness Property 5)
    """
    csrf_client = Client(enforce_csrf_checks=True)
    response = csrf_client.post("/accounts/login/", data={"login": "user", "password": "pass"})
    assert response.status_code == 403


@pytest.mark.django_db
@override_settings(CACHES=CACHES_LOCMEM)
def test_login_throttled_after_exceeding_rate_limit(client: Client):
    """Login is throttled after exceeding rate limit threshold.

    Validates: Requirement 4.2 (Correctness Property 1)
    """
    # Make multiple failed login attempts exceeding the "login_failed" threshold
    # Configuration: "login_failed": "3/5m/ip" means 3 attempts per 5 min per IP
    login_url = "/accounts/login/"

    for i in range(5):
        client.post(login_url, data={
            "login": "nonexistent@test.com",
            "password": "wrongpassword",
        })

    # After exceeding the threshold, allauth should throttle further attempts
    final_response = client.post(login_url, data={
        "login": "nonexistent@test.com",
        "password": "wrongpassword",
    })

    # allauth rate limiting either returns 429 or renders the form with error
    assert final_response.status_code in (200, 429)
    if final_response.status_code == 200:
        content = final_response.content.decode()
        # Allauth includes "too many" in rate limit messages
        assert "too many" in content.lower() or "rate" in content.lower()
