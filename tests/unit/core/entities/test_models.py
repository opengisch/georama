from typing import get_type_hints

from georama.core.entities.models import PermissionInterface


def test_permission_interface_attributes():
    type_hints = get_type_hints(PermissionInterface)
    expected = {
        "published_as_type": str,
        "action": str,
        "target_identifier": str,
        "target_name": str,
    }
    assert set(type_hints.keys()) == set(expected.keys())
    for field_name, expected_type in expected.items():
        assert type_hints[field_name] == expected_type


def test_permission_interface_codename():
    interface = PermissionInterface(
        published_as_type="maps", action="read", target_identifier="abc", target_name="maps"
    )
    assert isinstance(interface.codename, str)
    assert (
        interface.codename
        == f"{interface.published_as_type}_{interface.action}_{interface.target_identifier}"
    )


def test_permission_interface_readable_name():
    interface = PermissionInterface(
        published_as_type="maps", action="read", target_identifier="abc", target_name="maps"
    )
    target_readable_identifier = "12346"
    readable_name = interface.readable_name(target_readable_identifier)
    assert isinstance(readable_name, str)
    assert (
        readable_name
        == f"Can {interface.action} {interface.target_name} ({target_readable_identifier})"
    )
