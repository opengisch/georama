import json
import os

import pytest

from tests.testing.helpers import TemporaryEnvVar

DEFAULT_TIMEOUT = 5000


# Avoid django.core.exceptions.SynchronousOnlyOperation. Playwright uses an
# event loop, even when using the sync API. Django only checks whether _any_
# event loop is running, but not if _itself_ is running in an even loop.
# see https://github.com/microsoft/playwright-python/issues/439#issuecomment-763339612
# and https://github.com/microsoft/playwright-python/issues/224
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


@pytest.fixture
def page(live_server, new_context, projects_dir):
    context = new_context(base_url=live_server.url)
    context.set_default_timeout(DEFAULT_TIMEOUT)
    page = context.new_page()

    with TemporaryEnvVar("QSL_REDIS_URL", "redis://localhost:6379"):
        with TemporaryGeogirafeConfig(live_server.url):
            yield page

    page.close()
    context.close()


class TemporaryGeogirafeConfig(object):
    """Temporarily modify the GeoGirafe config to use a specific backend URL.

    This context manager is used during E2E tests to update the backend URL in
    the GeoGirafe config with the URL of the live server, which contains a
    dynamic port. When exiting the context manager, the original config is
    restored.
    """

    CFG_PATH = "geogirafe/config.json"

    def __init__(self, backend_url):
        self.backend_url = backend_url

    def __enter__(self):
        self.orig_config = self.read_config()
        self.modify_config(self.backend_url)

    def __exit__(self, type, value, traceback):
        self.restore_config()

    def read_config(self):
        return open(self.CFG_PATH, "r").read()

    def modify_config(self, backend_url):
        config = json.loads(self.orig_config)
        config["themes"]["url"] = f"{backend_url}/webgis/themes.json"
        config["languages"]["translations"]["de"] = [
            "i18n/de.json",
            f"{backend_url}/webgis/translations/de.json",
        ]
        with open(self.CFG_PATH, "w") as cfg:
            json.dump(config, cfg, indent=2)

    def restore_config(self):
        with open(self.CFG_PATH, "w") as cfg:
            cfg.write(self.orig_config)
