import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

from django.http import QueryDict

from georama.core.common.api import GeoramaTemplateViewSet
from georama.core.common.bulk_actions import DeleteBulkAction
from georama.core.common.serializers import BulkActionSerializer


def test_bulk_executes_selected_action():
    delete = DeleteBulkAction()
    queryset = Mock()
    queryset.adelete = AsyncMock()
    view = Mock()
    view._bulk_action_serializer.return_value = BulkActionSerializer(
        data=QueryDict("action=delete&ids=1&ids=abc"), context={"bulk_actions": [delete]}
    )
    # resolving and permission checking is the job of the action, we only see it is asked
    view._resolve_bulk_action = AsyncMock(return_value=(delete, queryset))
    request = SimpleNamespace(accepted_renderer=SimpleNamespace(format="json"))

    response = asyncio.run(GeoramaTemplateViewSet.bulk_action(view, request))

    assert response.status_code == 200
    view._resolve_bulk_action.assert_awaited_once_with({"action": delete, "ids": ["1", "abc"]})
    queryset.adelete.assert_awaited_once()


def test_bulk_reports_invalid_html_action(monkeypatch):
    report_error = Mock()
    monkeypatch.setattr("georama.core.common.api.messages.error", report_error)
    redirect = Mock()
    monkeypatch.setattr("georama.core.common.api.redirect", redirect)
    view = Mock()
    view._bulk_action_serializer.return_value = BulkActionSerializer(
        data=QueryDict("action=unknown&ids=1"), context={"bulk_actions": [DeleteBulkAction()]}
    )
    request = SimpleNamespace(
        accepted_renderer=SimpleNamespace(format="html"),
        GET=QueryDict("search=example"),
    )

    response = asyncio.run(GeoramaTemplateViewSet.bulk_action(view, request))

    assert response is redirect.return_value
    redirect.assert_called_once_with(view.url_name_list)
    assert "action" in report_error.call_args.args[1]
    view._resolve_bulk_action.assert_not_called()
