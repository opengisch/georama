import logging
from dataclasses import dataclass, field

from django.db import models

REMOTE_ACTIONS: dict[type[models.Model], list["RemoteAction"]] = {}


@dataclass
class RemoteAction:
    """Represents an action which can be registered on models. An action is considered
    a fully qualified view name which corresponding endpoint accepts the primary key of
    an instance of the model it was registered for.

    With Georama we have a collection of separated apps which should stay in isolation
    as much as possible. The direction of usage should be always from app `core` over
    the app `integration` to the others. To enable a more dynamic GUI this approach was
    implemented.

    The registration of actions should always be done in the apps.py of the app which
    wants to register actions upwards the chain. For instance, if the app `webgis` want's
    to allow projects (model in the app `integration`) to be published as a theme
    (model in the app `webgis`), it can register an action on the model `project`,
    a button might then be installed in the list and detail template to execute this
    action.

    Attributes:
        target: The fully qualified view name. This means
    """

    target: str
    name: str
    help_text: str
    origin: str
    icon_classes: str | None = field(default=None)
    permissions: list[str] = field(default_factory=list)


def register_remote_action(model: type[models.Model], action: RemoteAction):
    if model not in REMOTE_ACTIONS:
        REMOTE_ACTIONS[model] = []
    if action not in REMOTE_ACTIONS[model]:
        REMOTE_ACTIONS[model].append(action)
    else:
        logging.warning(
            f"Remote Action was in the list alredy, skipping: {model._meta.model_name} {action}"
        )


def get_remote_action(model: type[models.Model]):
    return REMOTE_ACTIONS.get(model, [])
