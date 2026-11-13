from georama.core.common.health import HealthCheck, HealthCheckResult
from georama.maps.apps import qsl_redis_queue


class QueueHealthCheck(HealthCheck):
    """Checks whether the QSL queue (redis) answers. Without it no map can be rendered,
    so `maps` owns this check.
    """

    name = "queue"

    async def check(self) -> HealthCheckResult:
        """Pings the queue through the QSL dispatcher, which keeps the redis details
        to itself.

        Returns:
            Healthy if the queue answered.
        """
        return HealthCheckResult(name=self.name, healthy=await qsl_redis_queue.is_reachable())


class WorkerHealthCheck(HealthCheck):
    """Checks whether at least one QSL worker is alive. A reachable queue alone does not
    help much if nobody takes the jobs out of it.
    """

    name = "workers"

    async def check(self) -> HealthCheckResult:
        """Asks the QSL dispatcher for the alive workers, what alive means (heartbeat age,
        not crashed) is decided by QSL.

        Returns:
            Healthy if at least one worker is alive, the alive workers as details.
        """
        workers = await qsl_redis_queue.alive_workers()
        return HealthCheckResult(
            name=self.name,
            healthy=len(workers) > 0,
            # id and last seen only, the worker info would disclose QGIS details
            details={
                "workers": [{"id": worker.id, "last_seen": worker.last_seen} for worker in workers]
            },
        )
