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
        """Looks at the resource. A check does not need to care about failures, it may
        simply raise, `run` turns that into a down.

        Returns:
            The result of the check.
        """
        pass

    async def run(self, timeout: float) -> HealthCheckResult:
        """Runs the check so it can never break the health answer. A resource which
        hangs or raises is just down, what exactly happened is only told to the log,
        the public answer would otherwise disclose hostnames and the like.

        Args:
            timeout: Seconds the check may take before it counts as down.

        Returns:
            The result of the check, unhealthy if it failed or took too long.
        """
        try:
            return await asyncio.wait_for(self.check(), timeout)
        except Exception:  # noqa: BLE001
            # the details stay in the log, the public answer only says down
            logger.exception(f"Health check failed: {self.name}")
            return HealthCheckResult(name=self.name, healthy=False)


class DatabaseHealthCheck(HealthCheck):
    """Asks the default database the simplest question there is. It belongs to `core`
    since every app depends on the database.
    """

    name = "database"

    async def check(self) -> HealthCheckResult:
        """Runs `SELECT 1` on the default database.

        Returns:
            A healthy result, if the database could not answer this raises.
        """
        await sync_to_async(self.select_one)()
        return HealthCheckResult(name=self.name, healthy=True)

    @staticmethod
    def select_one():
        """The ORM is sync only, so the query lives in its own function to be handed to
        `sync_to_async`.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")


def register_health_check(check: HealthCheck):
    """Adds a check to the health answer. Apps call this in their `ready()`, the same
    way they register remote actions. A second check with the same name is skipped,
    the name is the key in the answer and has to stay unique.

    Args:
        check: The check to register.
    """
    if check.name not in HEALTH_CHECKS:
        HEALTH_CHECKS[check.name] = check
    else:
        logging.warning(f"Health check was in the list already, skipping: {check.name}")


def get_health_checks() -> list[HealthCheck]:
    """Hands out the checks the health answer is made of.

    Returns:
        All registered checks in the order they were registered.
    """
    return list(HEALTH_CHECKS.values())
