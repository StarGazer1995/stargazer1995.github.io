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
    """Load the URL -> local path cache, dropping presigned query strings.

    Notion hands out a fresh presigned S3 URL (with an ``ASIA...`` key id and a
    session token) every time a page is exported. Keying the cache by the whole
    signed URL therefore misses on every run and - worse - commits the tokens
    to git, which GitHub secret scanning reports as a leaked AWS key.
    """
    manifest = {}
    if MANIFEST.exists():
        for url, local in json.loads(MANIFEST.read_text()).items():
            manifest[canonical_url(url)] = local
    return manifest


def canonical_url(url):
    """Identity of a Notion image: host + path, without the signature."""
    return url.split("?", 1)[0].split("#", 1)[0]


def download(url, proxies):
    import requests  # imported lazily so --skip runs work without it

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
            key = canonical_url(url)
            # Manifest paths are site-absolute ("/images/notion/x.png"); they
            # live under static/, not at the repo root.
            local = manifest.get(key)
            if not (local and (ROOT / "static" / local.lstrip("/")).exists()):
                try:
                    resp = download(url, proxies)
                except Exception as exc:
                    failed.append((url, str(exc)))
                    print(f"WARN could not download {url[:90]}: {exc}", file=sys.stderr)
                    continue
                ctype = resp.headers.get("content-type", "").split(";")[0].lower()
                ext = EXT_BY_TYPE.get(ctype, Path(url.split("?")[0]).suffix or ".png")
                # Hash the unsigned URL so a re-export reuses the same file
                # instead of writing a duplicate copy for every sync run.
                name = hashlib.sha1(key.encode()).hexdigest()[:16] + ext
                (IMAGE_DIR / name).write_bytes(resp.content)
                local = f"/images/notion/{name}"
                manifest[key] = local
                downloaded += 1
                print(f"downloaded {local} <- {url[:80]}")
            if url in text:
                text = text.replace(url, local)
                changed = True
                rewritten += 1
        if changed or content_changed:
            path.write_text(text, encoding="utf-8")

    payload = json.dumps(
        dict(sorted(manifest.items())), indent=2, ensure_ascii=False
    )
    # Never cache a presigned URL: it carries an AWS key id + session token.
    leaks = re.findall(r"[?&]X-Amz-[A-Za-z]+=", payload)
    if leaks:
        print(
            f"ERROR refusing to write {len(leaks)} presigned URL(s) to manifest",
            file=sys.stderr,
        )
        sys.exit(1)
    MANIFEST.write_text(payload, encoding="utf-8")
    print(
        f"postprocess: {len(files)} files, {downloaded} images downloaded, "
        f"{rewritten} references rewritten, {len(failed)} failed"
    )
    if failed:
        print("failed images:", failed[:10], file=sys.stderr)


if __name__ == "__main__":
    main()
