"""Cookiecutter post-generation hook."""

from __future__ import annotations

import shutil
from pathlib import Path


def remove_template_artifacts() -> None:
    project_directory = Path.cwd()
    license_support_dir = project_directory / "_licenses"
    if license_support_dir.exists():
        shutil.rmtree(license_support_dir)


def main() -> None:
    remove_template_artifacts()


if __name__ == "__main__":
    main()
