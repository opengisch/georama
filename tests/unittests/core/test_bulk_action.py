import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

from django.http import QueryDict

from georama.core.common.api import GeoramaTemplateViewSet


def test_bulk_deletes_selected_form_ids():
    queryset = Mock()
    queryset.filter.return_value.adelete = AsyncMock()
    view = Mock()
    view.afilter_queryset = AsyncMock(return_value=queryset)
    view._check_bulk_permissions = AsyncMock()
    request = SimpleNamespace(
        data=QueryDict("action=delete&ids=1&ids=abc"),
        accepted_renderer=SimpleNamespace(format="json"),
    )

    response = asyncio.run(GeoramaTemplateViewSet.bulk_action(view, request))

    assert response.status_code == 200
    view._check_bulk_permissions.assert_awaited_once_with("delete")
    queryset.filter.assert_called_once_with(pk__in=["1", "abc"])
    queryset.filter.return_value.adelete.assert_awaited_once()


def test_bulk_reports_invalid_html_action(monkeypatch):
    report_error = Mock()
    monkeypatch.setattr("georama.core.common.api.messages.error", report_error)
    redirect = Mock()
    monkeypatch.setattr("georama.core.common.api.redirect", redirect)
    view = Mock()
    request = SimpleNamespace(
        data=QueryDict("action=unknown&ids=1"),
        accepted_renderer=SimpleNamespace(format="html"),
        GET=QueryDict("search=example"),
    )

    response = asyncio.run(GeoramaTemplateViewSet.bulk_action(view, request))

    assert response is redirect.return_value
    redirect.assert_called_once_with(view.url_name_list)
    assert "action" in report_error.call_args.args[1]
    view.afilter_queryset.assert_not_called()
