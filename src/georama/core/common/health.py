import asyncio
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from asgiref.sync import sync_to_async
from django.db import connection

logger = logging.getLogger(__name__)

HEALTH_CHECKS: dict[str, "HealthCheck"] = {}


@dataclass
class HealthCheckResult:
    """The answer of a single health check.

    Attributes:
        name: The name of the check which produced this result.
        healthy: Whether the checked resource is usable.
        details: Additional public information of the check, e.g. the alive workers.
    """

    name: str
    healthy: bool
    details: dict = field(default_factory=dict)


class HealthCheck(ABC):
    """Represents a check of a resource Georama depends on. Like the `RemoteAction`
    the checks are registered by the app which owns the resource, so `core` never
    has to import the other apps.

    Attributes:
        name: The unique name of the check, it is the key in the health response.
    """

    name: str

    @abstractmethod
    async def check(self) -> HealthCheckResult:
        pass

    async def run(self, timeout: float) -> HealthCheckResult:
        try:
            return await asyncio.wait_for(self.check(), timeout)
        except Exception:  # noqa: BLE001
            # the details stay in the log, the public answer only says down
            logger.exception(f"Health check failed: {self.name}")
            return HealthCheckResult(name=self.name, healthy=False)


class DatabaseHealthCheck(HealthCheck):
    name = "database"

    async def check(self) -> HealthCheckResult:
        await sync_to_async(self.select_one)()
        return HealthCheckResult(name=self.name, healthy=True)

    @staticmethod
    def select_one():
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")


def register_health_check(check: HealthCheck):
    if check.name not in HEALTH_CHECKS:
        HEALTH_CHECKS[check.name] = check
    else:
        logging.warning(f"Health check was in the list already, skipping: {check.name}")


def get_health_checks() -> list[HealthCheck]:
    return list(HEALTH_CHECKS.values())
