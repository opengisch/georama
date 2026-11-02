"""Fixture modules, registered through `pytest_plugins` in `tests/conftest.py`."""

import random

import factory.random

SEED = 2056


def reseed():
    """Factories draw from `random` directly, factory_boy and Faker share another generator."""
    random.seed(SEED)
    factory.random.reseed_random(SEED)
