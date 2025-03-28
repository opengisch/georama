#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

this_file_location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))


def version_msg():
    """georama version, location and Python version.

    Get message about georama version, location
    and Python version.
    """
    python_version = sys.version[:3]
    message = "GeoRama %(version)s from {} (Python {})"
    location = os.path.dirname(this_file_location)
    return message.format(location, python_version)


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "georama.core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
