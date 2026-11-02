import pytest


@pytest.fixture
def backends(monkeypatch, posted_jobs, render_job_result):
    """QSL renders, and the item writes of pygeoapi answer without touching the shared table."""
    posted_jobs.answer = render_job_result
    monkeypatch.setattr(
        "pygeoapi.api.itemtypes.manage_collection_item",
        lambda *args, **kwargs: ({}, 200, "application/json"),
    )
