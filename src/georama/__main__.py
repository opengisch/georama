"""Run `python -m georama`.

Allow running GeoRama, also by invoking
the python module:

`python -m georama`

This is an alternative to directly invoking the cli that uses python as the
"entrypoint".
"""

from georama.cli import main

if __name__ == "__main__":  # pragma: no cover
    main(prog_name="georama")  # pylint: disable=unexpected-keyword-arg
