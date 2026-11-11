"""Writes the QGIS-Server-Light block in front of the generated notes of a georama release.

It answers "which QSL do I run with this georama": the pinned QSL release, its images and every QSL
release skipped since the previous georama release, so whoever upgrades over several QSL releases
finds each of their notes on the way.

Standard library, `git` and `gh` only, the workflow runs it with the python of the runner.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

from qsl_pin import QslPin, QslPinError, QslPinSpots, QslRelease


class GeoramaReleases:
    @staticmethod
    def previous_tag(tag: str) -> str | None:
        described = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0", "--match", "v*", f"{tag}^"],
            capture_output=True,
            text=True,
            check=False,
        )
        # the very first release has no predecessor
        if described.returncode != 0:
            return None
        return described.stdout.strip()

    @staticmethod
    def qsl_pin_at(tag: str) -> QslPin | None:
        pyproject = subprocess.run(
            ["git", "show", f"{tag}:pyproject.toml"], capture_output=True, text=True, check=True
        ).stdout
        # releases before the QSL release pin carry no pin we could compare with
        try:
            pin = QslPin.from_package_ref(QslPinSpots.package_ref_from_pyproject(pyproject))
        except QslPinError:
            return None
        return pin if isinstance(pin, QslRelease) else None


class QslReleases:
    REPOSITORY = "opengisch/qgis-server-light"
    URL = f"https://github.com/{REPOSITORY}/releases/tag"

    @classmethod
    def tags(cls) -> list[str]:
        listed = subprocess.run(
            [
                "gh",
                "release",
                "list",
                "--repo",
                cls.REPOSITORY,
                "--exclude-drafts",
                "--limit",
                "100",
                "--json",
                "tagName",
                "--jq",
                ".[].tagName",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        return listed.stdout.split()

    @staticmethod
    def version_key(tag: str) -> tuple[int, ...]:
        return tuple(int(number) for number in re.findall(r"[0-9]+", tag))

    @classmethod
    def between(cls, tags: list[str], previous: str, current: str) -> list[str]:
        # after the previous pin, up to and including the new one, in version order
        after, until = cls.version_key(previous), cls.version_key(current)
        return sorted(
            (tag for tag in tags if after < cls.version_key(tag) <= until),
            key=cls.version_key,
        )

    @classmethod
    def link(cls, tag: str) -> str:
        return f"[{tag}]({cls.URL}/{tag})"


class QslReleaseNote:
    def __init__(self, pin: QslPin, previous_tag: str | None, previous_pin: QslPin | None):
        self.pin = pin
        self.previous_tag = previous_tag
        self.previous_pin = previous_pin

    @property
    def qsl_changed(self) -> bool:
        return self.previous_pin is not None and self.previous_pin.version != self.pin.version

    def render(self, qsl_tags: list[str]) -> str:
        lines = [
            "## QGIS-Server-Light",
            "",
            f"Runs with QSL {QslReleases.link(self.pin.version)}:",
            f"- `{self.pin.image('worker')}`",
            f"- `{self.pin.image('exporter')}`",
            "",
        ]
        skipped = []
        if self.qsl_changed:
            skipped = QslReleases.between(qsl_tags, self.previous_pin.version, self.pin.version)
        if skipped:
            links = ", ".join(QslReleases.link(tag) for tag in skipped)
            since = f"since georama {self.previous_tag} (QSL {self.previous_pin.version})"
            lines += [f"QSL changed {since}: {links}.", ""]
        return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tag", required=True, help="the georama release tag, e.g. v26.3")
    parser.add_argument("--output", type=Path, required=True, help="the markdown file to write")
    arguments = parser.parse_args()
    try:
        pin = QslPinSpots.read_pin(Path.cwd(), require_release=True)
    except QslPinError as error:
        print(f"::error::{error}")
        return 1
    previous_tag = GeoramaReleases.previous_tag(arguments.tag)
    previous_pin = GeoramaReleases.qsl_pin_at(previous_tag) if previous_tag else None
    note = QslReleaseNote(pin, previous_tag, previous_pin)
    # only ask GitHub for the QSL releases when there is a range to list
    qsl_tags = QslReleases.tags() if note.qsl_changed else []
    arguments.output.write_text(note.render(qsl_tags))
    print(arguments.output.read_text())
    return 0


if __name__ == "__main__":
    sys.exit(main())
