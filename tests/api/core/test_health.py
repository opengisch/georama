from datetime import UTC, datetime

import pytest
from qgis_server_light.interface.dispatcher.common import Worker
from qgis_server_light.interface.worker.info import EngineInfo, QgisInfo, Status
from rest_framework import status
from rest_framework.test import APIClient

from georama.maps.apps import qsl_redis_queue


class TestHealth:
    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "queue_reachable, alive_workers, expected_status_code, expected_body",
        [
            # everything is there
            (
                True,
                [
                    Worker(
                        id="worker-1",
                        last_seen=datetime(2026, 11, 12, 10, 0, 0, tzinfo=UTC),
                        info=EngineInfo(
                            id="worker-1",
                            qgis_info=QgisInfo(
                                version=34400, version_name="QGIS 3.44", path="/usr/share/qgis"
                            ),
                            status=Status.WAITING,
                            started=0.0,
                        ),
                    )
                ],
                status.HTTP_200_OK,
                {
                    "status": "ok",
                    "checks": {
                        "database": {"status": "ok"},
                        "queue": {"status": "ok"},
                        "workers": {
                            "status": "ok",
                            "workers": [{"id": "worker-1", "last_seen": "2026-11-12T10:00:00Z"}],
                        },
                    },
                },
            ),
            # the queue is up but no worker serves jobs
            (
                True,
                [],
                status.HTTP_503_SERVICE_UNAVAILABLE,
                {
                    "status": "down",
                    "checks": {
                        "database": {"status": "ok"},
                        "queue": {"status": "ok"},
                        "workers": {"status": "down", "workers": []},
                    },
                },
            ),
            # the queue is gone, so are the workers
            (
                False,
                [],
                status.HTTP_503_SERVICE_UNAVAILABLE,
                {
                    "status": "down",
                    "checks": {
                        "database": {"status": "ok"},
                        "queue": {"status": "down"},
                        "workers": {"status": "down", "workers": []},
                    },
                },
            ),
        ],
    )
    def test_status_follows_the_checks(
        self, monkeypatch, queue_reachable, alive_workers, expected_status_code, expected_body
    ):
        # we let the queue answer what the test case wants
        async def is_reachable():
            return queue_reachable

        async def get_alive_workers():
            return alive_workers

        monkeypatch.setattr(qsl_redis_queue, "is_reachable", is_reachable)
        monkeypatch.setattr(qsl_redis_queue, "alive_workers", get_alive_workers)

        response = APIClient().get("/health/?f=json", SERVER_NAME="localhost")
        assert response.status_code == expected_status_code
        # the body is compared as a whole, so the worker info (QGIS version and path)
        # must not show up anywhere
        assert response.json() == expected_body
        assert response["Cache-Control"] == "no-store"

    # no django_db mark on purpose: every database access fails like a database which is
    # down, also the ones outside the health check (session, organisation, permissions)
    def test_html_renders_while_database_is_down(self, monkeypatch):
        async def is_reachable():
            return True

        async def get_alive_workers():
            return []

        monkeypatch.setattr(qsl_redis_queue, "is_reachable", is_reachable)
        monkeypatch.setattr(qsl_redis_queue, "alive_workers", get_alive_workers)

        client = APIClient()
        # a logged in human, the session would be loaded from the database
        client.cookies["sessionid"] = "some-session-key"
        response = client.get(
            "/health/?f=html",
            # an organisation subdomain, the organisation would be looked up in the database
            SERVER_NAME="someorganisation.localhost",
        )

        # we expect the page and not a server error
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert response["Content-Type"] == "text/html; charset=utf-8"
        # the database is down, the reason stays in the log
        assert "database" in response.text
        assert "Database access not allowed" not in response.text
