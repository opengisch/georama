import logging

import pytest

from georama.core.common.login_attempts import LoginAttempts


@pytest.fixture
def two_attempts(settings):
    # a small limit keeps the stories short
    settings.LOGIN_ATTEMPTS_RATE = "2/300s/key"
    settings.LOGIN_ATTEMPTS_BLOCKED_MINUTES = 5
    yield settings.LOGIN_ATTEMPTS_RATE


class TestLoginAttempts:
    def test_username_is_blocked_after_the_limit(self, rf, two_attempts):
        request = rf.get("/", SERVER_NAME="localhost")
        # the first failure doesn't block yet
        LoginAttempts.count_failure(request, "anna")
        assert not LoginAttempts.blocked(request, "anna")
        # the second one reaches the limit
        LoginAttempts.count_failure(request, "anna")
        assert LoginAttempts.blocked(request, "anna")

    def test_usernames_are_counted_separately(self, rf, two_attempts):
        request = rf.get("/", SERVER_NAME="localhost")
        LoginAttempts.count_failure(request, "anna")
        LoginAttempts.count_failure(request, "anna")
        # anna is blocked, bob who comes from the same address is not
        assert LoginAttempts.blocked(request, "anna")
        assert not LoginAttempts.blocked(request, "bob")

    def test_username_is_counted_ignoring_case(self, rf, two_attempts):
        request = rf.get("/", SERVER_NAME="localhost")
        LoginAttempts.count_failure(request, "Anna")
        LoginAttempts.count_failure(request, "ANNA")
        # a guesser doesn't get more attempts by changing the case
        assert LoginAttempts.blocked(request, "anna")

    def test_clients_behind_one_proxy_dont_block_each_other(self, rf, two_attempts):
        # twelve people behind the same proxy mistype their password once each
        for number in range(12):
            LoginAttempts.count_failure(rf.get("/", REMOTE_ADDR="10.0.0.2"), f"user{number}")
        # nobody is blocked, there is no limit per ip in Georama
        assert not LoginAttempts.blocked(rf.get("/", REMOTE_ADDR="10.0.0.2"), "user0")

    def test_get_requests_are_counted(self, rf, two_attempts):
        # HTTP Basic arrives as GET mostly (GetMap, GetFeature), allauth's public helper
        # would skip those
        request = rf.get("/maps/ows?REQUEST=GetMap", SERVER_NAME="localhost")
        LoginAttempts.count_failure(request, "anna")
        LoginAttempts.count_failure(request, "anna")
        assert LoginAttempts.blocked(request, "anna")

    def test_reaching_the_limit_is_logged_once(self, rf, caplog, two_attempts):
        request = rf.get(
            "/", SERVER_NAME="localhost", REMOTE_ADDR="10.0.0.2", HTTP_X_FORWARDED_FOR="203.0.113.7"
        )
        with caplog.at_level(logging.WARNING, logger="georama.core.common.login_attempts"):
            LoginAttempts.count_failure(request, "anna")
            # nothing to tell before the limit
            assert caplog.text == ""
            LoginAttempts.count_failure(request, "anna")
        # the operator finds the username and where the attempts came from
        assert caplog.messages == [
            "Too many failed login attempts for anna, blocked for up to 5 minutes. "
            "Remote address: 10.0.0.2, X-Forwarded-For: '203.0.113.7'"
        ]
