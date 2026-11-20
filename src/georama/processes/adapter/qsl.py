from collections.abc import Iterable

from qgis_server_light.interface.dispatcher.common import JobState
from qgis_server_light.interface.job.common.input import ExecutionMode
from qgis_server_light.interface.job.process.description import (
    ProcessDescription,
    ProcessDescriptions,
    ProcessWarning,
)
from qgis_server_light.interface.job.process.input import QslJobParameterExecuteProcess

from georama.processes.apps import qsl_redis_state_queue
from georama.processes.processes_config import Config


async def process_descriptions() -> ProcessDescriptions:
    return await qsl_redis_state_queue.process_descriptions()


async def process_descriptions_by_algorithm_id(
    algorithm_ids: Iterable[str],
) -> dict[str, ProcessDescription]:
    algorithm_ids = set(algorithm_ids)
    return {
        process_description.id: process_description
        for process_description in (await process_descriptions()).processes
        if process_description.id in algorithm_ids
    }


async def process_description(algorithm_id: str) -> ProcessDescription | None:
    return (await process_descriptions_by_algorithm_id([algorithm_id])).get(algorithm_id)


async def process_warnings_by_algorithm_id(
    algorithm_ids: Iterable[str],
) -> dict[str, ProcessWarning]:
    algorithm_ids = set(algorithm_ids)
    return {
        process_warning.process_id: process_warning
        for process_warning in (await process_descriptions()).warnings
        if process_warning.process_id in algorithm_ids
    }


async def process_warning(algorithm_id: str) -> ProcessWarning | None:
    return (await process_warnings_by_algorithm_id([algorithm_id])).get(algorithm_id)


async def served_algorithm_ids() -> set[str]:
    return {
        process_description.id for process_description in (await process_descriptions()).processes
    }


def non_published_process_descriptions(
    process_descriptions: ProcessDescriptions,
    published_algorithm_ids: set[str],
    search: str,
) -> list[ProcessDescription]:
    return [
        process_description
        for process_description in process_descriptions.processes
        if process_description.id not in published_algorithm_ids
        and (not search or search in process_description.id.lower())
    ]


async def submit_job(
    job_id: str,
    job_parameter: QslJobParameterExecuteProcess,
    execution_mode: ExecutionMode = ExecutionMode.ASYNC,
) -> None:
    await qsl_redis_state_queue.submit(job_id, job_parameter, execution_mode)


async def job_state(job_id: str) -> JobState | None:
    return await qsl_redis_state_queue.state(job_id)


async def wait_for_job(job_id: str) -> JobState | None:
    return await qsl_redis_state_queue.wait(job_id, to=Config().sync_execute_timeout)
