import pytest

from tests.api.data import ApiData, create_api_data, module_transaction
from tests.fixtures.gis import Gis


@pytest.fixture(scope="module")
def api_data(django_db_setup, django_db_blocker, tmp_path_factory, gis: Gis) -> ApiData:
    """The data shared by the tests of a module, see `data.py`."""
    with module_transaction(django_db_blocker, tmp_path_factory):
        yield create_api_data(gis)


@pytest.fixture
def backends(monkeypatch, posted_jobs, render_job_result):
    """QSL renders, and the item writes of pygeoapi answer without touching the shared table."""
    posted_jobs.answer = render_job_result
    monkeypatch.setattr(
        "pygeoapi.api.itemtypes.manage_collection_item",
        lambda *args, **kwargs: ({}, 200, "application/json"),
    )
