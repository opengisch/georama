import pytest
from django.conf import settings
from django.test import Client
from rest_framework import status

from tests.i18n.declarations import (
    DEFAULT_LANGUAGE,
    INDEX_HEADING,
    INDEX_PATH,
    SET_LANGUAGE_PATH,
    TRANSLATED_LANGUAGE,
)


def get_index(client: Client, **headers):
    response = client.get(INDEX_PATH, SERVER_NAME="localhost", **headers)
    assert response.status_code == status.HTTP_200_OK
    return response.content.decode()


class TestLanguageSelection:
    @pytest.mark.django_db
    def test_accept_language_header_selects_language(self):
        content = get_index(Client(), HTTP_ACCEPT_LANGUAGE=TRANSLATED_LANGUAGE)
        assert f'<html lang="{TRANSLATED_LANGUAGE}"' in content
        assert INDEX_HEADING[TRANSLATED_LANGUAGE] in content

    @pytest.mark.django_db
    def test_language_selector_sets_cookie_which_wins_over_header(self):
        client = Client()
        response = client.post(
            SET_LANGUAGE_PATH,
            {"language": TRANSLATED_LANGUAGE, "next": INDEX_PATH},
            SERVER_NAME="localhost",
        )
        assert response.status_code == status.HTTP_302_FOUND
        assert client.cookies[settings.LANGUAGE_COOKIE_NAME].value == TRANSLATED_LANGUAGE

        content = get_index(client, HTTP_ACCEPT_LANGUAGE=DEFAULT_LANGUAGE)
        assert INDEX_HEADING[TRANSLATED_LANGUAGE] in content
