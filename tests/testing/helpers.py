import os
import types
from importlib import resources


def asset(module: types.ModuleType, path: str) -> str:
    """Returns the path to a testing asset.

    An asset may be any data file or directory inside the tests/ directory.
    """
    return str(resources.files(module).joinpath(path))


class TemporaryEnvVar(object):
    """Temporarily modify an environment variable during tests.

    This context manager allows to temporarily set / change an env var, and
    restore it to its original value after the context is exited.
    """

    def __init__(self, name, new_value):
        self.name = name
        self.new_value = new_value
        self._orig_value = os.environ.get(name)

    def __enter__(self):
        os.environ[self.name] = self.new_value

    def __exit__(self, type, value, traceback):
        if self._orig_value is not None:
            os.environ[self.name] = self._orig_value
        else:
            del os.environ[self.name]