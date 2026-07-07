"""Root pytest configuration.

Runs before any Django imports so environment variables required by
`django-configurations` are in place when Django is configured.

Kept intentionally small: only side-effect is populating environment
variables that are safe to have a known value in a test context.
"""

import os

# Every `values.SecretValue()` in georama.core.settings reads DJANGO_SECRET_KEY
# from the environment and refuses to boot if missing. The Test configuration
# is only ever used by the pytest runner (pinned in pyproject.toml under
# [tool.pytest.ini_options]), so a fixed, obviously-fake value here is fine
# and keeps the source free of any hardcoded key that could survive into a
# real deployment.
os.environ.setdefault("DJANGO_SECRET_KEY", "pytest-only-not-a-real-secret")
