from georama.core.common.health import HealthCheck, HealthCheckResult
from georama.maps.apps import qsl_redis_queue


class QueueHealthCheck(HealthCheck):
    name = "queue"

    async def check(self) -> HealthCheckResult:
        return HealthCheckResult(name=self.name, healthy=await qsl_redis_queue.is_reachable())


class WorkerHealthCheck(HealthCheck):
    name = "workers"

    async def check(self) -> HealthCheckResult:
        workers = await qsl_redis_queue.alive_workers()
        return HealthCheckResult(
            name=self.name,
            healthy=len(workers) > 0,
            # id and last seen only, the worker info would disclose QGIS details
            details={
                "workers": [{"id": worker.id, "last_seen": worker.last_seen} for worker in workers]
            },
        )
