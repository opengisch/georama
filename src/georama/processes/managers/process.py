from django.db import models

from georama.core.common.managers import PublicOrProtectedManager
from georama.core.common.querysets import OrganisationalQuerySet
from georama.processes.adapter.qsl import process_descriptions_by_algorithm_id


class ProcessQuerySet(OrganisationalQuerySet):
    async def adescribed(self) -> list:
        processes = [process async for process in self]
        process_descriptions = await process_descriptions_by_algorithm_id(
            process.algorithm_id for process in processes
        )
        for process in processes:
            process.process_description = process_descriptions.get(process.algorithm_id)
        return processes


class ProcessManager(PublicOrProtectedManager.from_queryset(ProcessQuerySet)):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return (
            super()
            .get_queryset()
            .prefetch_related(
                # "jobs",
            )
        )
