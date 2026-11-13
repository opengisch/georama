"""Reads the QGIS-Server-Light pin of georama and checks its three spots agree.

georama pins QSL in `pyproject.toml` (the package) and twice in `compose.yml` (the worker and
exporter images). The interface is the contract on the queue, so all three have to name the same
QSL state: a release (`@v26.1`, `26.1-worker`), a QSL PR (`@refs/pull/40/head`, `pr-40-worker`) or
QSL main (`@main`, `edge-worker`).

Standard library only, the workflow runs it with the python of the runner.
"""

import argparse
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path


class QslPinError(Exception):
    pass


@dataclass
class QslPin:
    version: str

    IMAGE = "opengisch/qgis-server-light"
    PATTERN = ""

    @staticmethod
    def from_package_ref(ref: str) -> "QslPin":
        """Evaluates the version number from either vX.XX or from refs/pull/xx/head."""
        for pin_type in (QslRelease, QslPullRequest, QslEdge):
            matched = re.fullmatch(pin_type.PATTERN, ref)
            if matched:
                return pin_type(version=matched.group(1))
        raise QslPinError(
            f"the QSL package pin @{ref} is neither a release (@vYY.N), "
            "a QSL PR (@refs/pull/<n>/head) nor QSL main (@main)"
        )

    @property
    def image_tag_prefix(self) -> str:
        raise NotImplementedError

    @property
    def description(self) -> str:
        raise NotImplementedError

    def image(self, variant: str) -> str:
        return f"{self.IMAGE}:{self.image_tag_prefix}-{variant}"


class QslRelease(QslPin):
    PATTERN = r"(v[0-9][^/]*)"

    @property
    def image_tag_prefix(self) -> str:
        return self.version.removeprefix("v")

    @property
    def description(self) -> str:
        return f"QSL release {self.version}"


class QslPullRequest(QslPin):
    PATTERN = r"refs/pull/([0-9]+)/head"

    @property
    def image_tag_prefix(self) -> str:
        return f"pr-{self.version}"

    @property
    def description(self) -> str:
        return f"QSL PR opengisch/qgis-server-light#{self.version}"


class QslEdge(QslPin):
    PATTERN = r"(main)"

    @property
    def image_tag_prefix(self) -> str:
        return "edge"

    @property
    def description(self) -> str:
        return "QSL main"


@dataclass
class QslPinSpots:
    package_ref: str
    image_tags: dict[str, set[str]]

    PACKAGE_URL = "github.com/opengisch/qgis-server-light.git@"
    VARIANTS = ("worker", "exporter")
    IMAGE_PATTERN = re.compile(rf"{QslPin.IMAGE}:([^\"\s]+)-(worker|exporter)\b")

    @classmethod
    def from_project(cls, root: Path) -> "QslPinSpots":
        image_tags = {variant: set() for variant in cls.VARIANTS}
        for prefix, variant in cls.IMAGE_PATTERN.findall((root / "compose.yml").read_text()):
            image_tags[variant].add(prefix)
        return cls(
            package_ref=cls.package_ref_from_pyproject((root / "pyproject.toml").read_text()),
            image_tags=image_tags,
        )

    @classmethod
    def package_ref_from_pyproject(cls, pyproject: str) -> str:
        dependencies = tomllib.loads(pyproject).get("project", {}).get("dependencies", [])
        for dependency in dependencies:
            if cls.PACKAGE_URL in dependency:
                return dependency.split(cls.PACKAGE_URL, 1)[1]
        raise QslPinError("no qgis-server-light git dependency in pyproject.toml")

    @classmethod
    def read_pin(cls, root: Path, require_release: bool = False) -> QslPin:
        spots = cls.from_project(root)
        print(f"pyproject.toml package: @{spots.package_ref}")
        for variant in cls.VARIANTS:
            print(f"compose.yml {variant}: {spots.describe(variant)}")
        return spots.pin(require_release)

    def describe(self, variant: str) -> str:
        if not self.image_tags[variant]:
            return f"no {variant} image"
        return ", ".join(f"{tag}-{variant}" for tag in sorted(self.image_tags[variant]))

    def pin(self, require_release: bool = False) -> QslPin:
        pin = QslPin.from_package_ref(self.package_ref)
        # several services may run the worker image, all of them have to name the pin
        if any(self.image_tags[variant] != {pin.image_tag_prefix} for variant in self.VARIANTS):
            expected = " / ".join(f"{pin.image_tag_prefix}-{variant}" for variant in self.VARIANTS)
            found = " / ".join(self.describe(variant) for variant in self.VARIANTS)
            raise QslPinError(
                f"the QSL pin differs, pyproject.toml @{self.package_ref} expects {expected}, "
                f"compose.yml has {found}"
            )
        # a QSL PR or main pin is fine on a draft or a branch, main and releases run released QSL
        if not isinstance(pin, QslRelease):
            pinned = f"pinned to {pin.description}"
            if require_release:
                raise QslPinError(f"{pinned}, release QSL and bump the pin to it")
            print(f"::notice::{pinned}, it has to become a QSL release before the merge")
        return pin


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--require-release",
        action="store_true",
        help="fail when the pin is a QSL PR and not a release",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="the georama checkout")
    arguments = parser.parse_args()
    try:
        pin = QslPinSpots.read_pin(arguments.root, arguments.require_release)
    except QslPinError as error:
        print(f"::error::{error}")
        return 1
    print(f"QSL pin agrees: {pin.image('worker')}, {pin.image('exporter')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
