#!/usr/bin/env python3
"""Download Notion-hosted images into the Hugo site and rewrite links.

The Notion sync action leaves temporary S3 URLs in Markdown and front matter.
Those URLs expire, so this script mirrors them under static/images/notion/
and rewrites every reference to a stable local path.
"""
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIRS = [ROOT / "content" / "posts", ROOT / "content" / "tech"]
IMAGE_DIR = ROOT / "static" / "images" / "notion"
MANIFEST = IMAGE_DIR / "manifest.json"

URL_RE = re.compile(
    r"https://(?:prod-files-secure\.s3\.[^/\s]+\.amazonaws\.com"
    r"|s3\.[^/\s]+\.amazonaws\.com/secure\.notion-static\.com"
    r"|app\.notion\.com/images)/[^\s)\"'<>]+"
)

EXT_BY_TYPE = {
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
}


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {}


def download(url, proxies):
    last = None
    for _ in range(2):
        try:
            r = requests.get(url, timeout=45, proxies=proxies)
            r.raise_for_status()
            return r
        except Exception as exc:  # transient S3/TLS issues
            last = exc
    raise last


def normalize_math(text):
    """Make Notion/KaTeX math blocks valid for KaTeX.

    Notion exports multi-line equations with ``\\newline``, which KaTeX does
    not understand. Convert those to ``\\\\`` and wrap the block in a
    ``gathered`` environment. Also undo Markdown's ``\\_`` escaping.
    """

    def repl(match):
        body = match.group(1)
        had_newline = "\\newline" in body
        body = body.replace("\\newline", "\\\\")
        body = body.replace("\\_", "_")
        body = body.replace("…", "\\dots").replace("...", "\\dots")
        body = re.sub(r"\\\\\s*$", "", body.strip())
        if had_newline:
            body = "\\begin{gathered}\n" + body + "\n\\end{gathered}"
        return "{{< math >}}\n" + body + "\n{{< /math >}}"

    # Do not re-wrap blocks that are already inside the shortcode.
    parts = re.split(r"(\{\{<\s*math\s*>\}\}.*?\{\{<\s*/math\s*>\}\})", text, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"\$\$(.*?)\$\$", repl, parts[i], flags=re.S)
    return "".join(parts)


COVER_RE = re.compile(r"(?m)^cover:[ \t]*(\S.*?)[ \t]*$")


def normalize_cover(text):
    """PaperMod reads ``cover.image``; the Notion action emits a bare string."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    head, rest = text[:end], text[end:]

    def repl(match):
        value = match.group(1).strip()
        if value.startswith("{") or value.startswith("|"):
            return match.group(0)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        return f'cover:\n  image: "{value}"\n  alt: ""'

    return COVER_RE.sub(repl, head) + rest


def main():
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    proxy = os.environ.get("NOTION_IMAGE_PROXY")
    proxies = {"http": proxy, "https": proxy} if proxy else None

    files = []
    for folder in CONTENT_DIRS:
        if folder.exists():
            files.extend(sorted(folder.rglob("*.md")))

    downloaded = 0
    rewritten = 0
    failed = []

    for path in files:
        text = path.read_text(encoding="utf-8")
        original = text
        # The Notion action does not understand these container blocks and
        # emits their type name as a paragraph. Drop the stray label.
        text = re.sub(
            r"(?m)^\s*\[(?:link_to_page|table_of_contents)\]\([^)]*\)\s*$\n?",
            "",
            text,
        )
        text = re.sub(r"(?m)^\s*(?:link_to_page|table_of_contents)\s*$\n?", "", text)
        text = normalize_math(text)
        text = normalize_cover(text)
        content_changed = text != original
        urls = [] if os.environ.get("SKIP_IMAGE_DOWNLOAD") == "1" else sorted(set(URL_RE.findall(text)))
        if not urls and not content_changed:
            continue
        changed = False
        for url in urls:
            if url in manifest and (ROOT / manifest[url].lstrip("/")).exists():
                local = manifest[url]
            else:
                try:
                    resp = download(url, proxies)
                except Exception as exc:
                    failed.append((url, str(exc)))
                    print(f"WARN could not download {url[:90]}: {exc}", file=sys.stderr)
                    continue
                ctype = resp.headers.get("content-type", "").split(";")[0].lower()
                ext = EXT_BY_TYPE.get(ctype, Path(url.split("?")[0]).suffix or ".png")
                name = hashlib.sha1(url.encode()).hexdigest()[:16] + ext
                (IMAGE_DIR / name).write_bytes(resp.content)
                local = f"/images/notion/{name}"
                manifest[url] = local
                downloaded += 1
                print(f"downloaded {local} <- {url[:80]}")
            if url in text:
                text = text.replace(url, local)
                changed = True
                rewritten += 1
        if changed or content_changed:
            path.write_text(text, encoding="utf-8")

    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        f"postprocess: {len(files)} files, {downloaded} images downloaded, "
        f"{rewritten} references rewritten, {len(failed)} failed"
    )
    if failed:
        print("failed images:", failed[:10], file=sys.stderr)


if __name__ == "__main__":
    main()
