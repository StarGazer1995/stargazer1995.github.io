#!/usr/bin/env python3
"""Reject ambiguous article sources before commit and deployment."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


CONTENT_ROOTS = ("content/posts", "content/tech")
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", re.DOTALL)
SCALAR_FIELD = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
NOTION_ID = re.compile(r"^[0-9a-fA-F]{32}$")


def git_output(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return [item for item in result.stdout.decode("utf-8").split("\0") if item]


def selected_paths(args: argparse.Namespace) -> list[str]:
    if args.files:
        return args.files
    if args.all:
        return sorted(
            path
            for path in git_output("ls-files", "-z", "--", *CONTENT_ROOTS)
            if path.endswith(".md")
        )
    return sorted(
        path
        for path in git_output(
            "diff",
            "--cached",
            "--name-only",
            "--diff-filter=ACMR",
            "-z",
            "--",
            *CONTENT_ROOTS,
        )
        if path.endswith(".md")
    )


def staged_content(path: str) -> str:
    result = subprocess.run(
        ["git", "show", f":{path}"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8")


def scalar_fields(front_matter: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in front_matter.splitlines():
        match = SCALAR_FIELD.match(line)
        if not match:
            continue
        key, value = match.groups()
        if key not in {"id", "slug", "source"}:
            continue
        fields[key] = value.strip().strip("'\"")
    return fields


def validate(path: str, content: str) -> list[str]:
    match = FRONT_MATTER.match(content)
    if not match:
        return ["missing YAML front matter"]

    fields = scalar_fields(match.group(1))
    notion_id = fields.get("id", "").replace("-", "")
    source = fields.get("source", "").lower()

    if notion_id and source == "local":
        return ["has both a Notion id and `source: local`"]
    if notion_id:
        if not NOTION_ID.fullmatch(notion_id):
            return ["Notion `id` must contain 32 hexadecimal characters"]
        return []
    if source == "local":
        return []
    return [
        "source is ambiguous: add a real Notion `id` or explicit `source: local`"
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--all", action="store_true", help="check all tracked content")
    mode.add_argument("--files", nargs="+", help="check explicit files")
    args = parser.parse_args()

    paths = selected_paths(args)
    staged = not args.all and not args.files
    failures: list[tuple[str, str]] = []

    for path in paths:
        if Path(path).name == "_index.md":
            continue
        try:
            content = staged_content(path) if staged else Path(path).read_text("utf-8")
        except (OSError, UnicodeDecodeError, subprocess.CalledProcessError) as error:
            failures.append((path, f"cannot read file: {error}"))
            continue
        for message in validate(path, content):
            failures.append((path, message))

    if not failures:
        print(f"content source check passed ({len(paths)} files)")
        return 0

    for path, message in failures:
        print(f"{path}: {message}", file=sys.stderr)
    print(
        "Content source check failed. Every article needs either a real Notion "
        "`id` or explicit `source: local`.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
