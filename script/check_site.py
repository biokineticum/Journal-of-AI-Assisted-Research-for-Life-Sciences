#!/usr/bin/env python3
"""Check the built site: internal links, draft notice, and Markdown sources."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
BASE = sys.argv[2] if len(sys.argv) > 2 else ""
BASE = BASE.rstrip("/")
REPO = Path(__file__).resolve().parents[1]
ERRORS = []


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hrefs = []
        self.assets = []
        self.lang = None
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "html":
            self.lang = data.get("lang")
        if tag == "a" and "href" in data:
            self.hrefs.append(data["href"])
        if tag == "link" and "stylesheet" in (data.get("rel") or ""):
            self.assets.append(data.get("href", ""))
        if tag in {"img", "script", "iframe", "source"} and data.get("src"):
            self.assets.append(data["src"])
        if data.get("id"):
            self.ids.add(data["id"])


def page_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        suffix = "/"
    elif rel.endswith("/index.html"):
        suffix = "/" + rel[: -len("index.html")]
    else:
        suffix = "/" + rel
    return f"{BASE}{suffix}"


def file_for(url_path: str):
    if BASE and url_path.startswith(BASE + "/"):
        rel = url_path[len(BASE) + 1 :]
    elif BASE and url_path == BASE:
        rel = ""
    elif url_path.startswith("/"):
        rel = url_path.lstrip("/")
    else:
        return None
    if rel == "" or rel.endswith("/"):
        return ROOT / rel / "index.html"
    return ROOT / rel


def resolve_md(source_rel: str, href: str):
    href = href.split("#", 1)[0].split("?", 1)[0].strip()
    if not href.endswith(".md") or href.startswith(("http://", "https://", "/")):
        return None
    parts = list(Path(source_rel).parent.parts)
    for part in Path(href).parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if parts:
                parts.pop()
        else:
            parts.append(part)
    return str(Path(*parts)) if parts else ""


def markdown_links(text: str):
    links = []
    start = 0
    while True:
        closer = text.find("](", start)
        if closer < 0:
            break
        opener = text.rfind("[", start, closer)
        end = text.find(")", closer + 2)
        if opener >= 0 and end > closer and "\n" not in text[opener:end]:
            links.append(text[closer + 2 : end].strip())
            start = end + 1
        else:
            start = closer + 2
    return links


def output_url(source_rel: str):
    stem = Path(source_rel).with_suffix("")
    directory = ROOT / stem / "index.html"
    flat = ROOT / f"{stem}.html"
    if directory.is_file():
        return f"{BASE}/{stem.as_posix()}/"
    if flat.is_file():
        return f"{BASE}/{stem.as_posix()}.html"
    return None


def main():
    if not ROOT.is_dir():
        sys.exit(f"missing build directory: {ROOT}")

    html_files = sorted(ROOT.rglob("*.html"))
    if not html_files:
        sys.exit("no HTML files were built")

    built = {}
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        if "<script" in lowered:
            ERRORS.append(f"{path}: contains a script")
        for blocked in ("fonts.googleapis", "googletagmanager", "google-analytics", "cdn.jsdelivr", "unpkg.com"):
            if blocked in lowered:
                ERRORS.append(f"{path}: external resource {blocked}")
        if "@" in text:
            ERRORS.append(f"{path}: unexpected @ (do not invent an email address)")

        parser = Collector()
        parser.feed(text)
        url = page_url(path)
        built[url] = (path, parser, text)
        base_for_join = url if url.endswith("/") else url.rsplit("/", 1)[0] + "/"

        if parser.lang == "pl":
            if "nie przyjmuje jeszcze zgłoszeń" not in text and path.name != "404.html":
                ERRORS.append(f"{path}: missing the Polish submissions notice")
        elif "not yet accepting submissions" not in text and path.name != "404.html":
            ERRORS.append(f"{path}: missing the English submissions notice")

        for href in parser.hrefs + parser.assets:
            if href == BASE:
                ERRORS.append(f"{path}: link points at the bare base path ({href})")
            if href.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            if href.startswith("#"):
                anchor = href[1:]
                if anchor and anchor not in parser.ids:
                    ERRORS.append(f"{path}: missing anchor {href}")
                continue
            target = urljoin(base_for_join, href)
            parsed = urlparse(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = file_for(unquote(parsed.path))
            if destination is None or not destination.is_file():
                ERRORS.append(f"{path}: broken internal link {href}")
            if unquote(parsed.path).endswith(".md"):
                ERRORS.append(f"{path}: Markdown link was not rewritten: {href}")

    source_docs = sorted((REPO / "docs").rglob("*.md"))
    if len(source_docs) != 14:
        ERRORS.append(f"expected 14 policy files, found {len(source_docs)}")

    for source in source_docs:
        rel = source.relative_to(REPO).as_posix()
        page = output_url(rel)
        if page is None or page not in built:
            ERRORS.append(f"{rel}: no HTML page was built")
            continue
        html = built[page][2]
        for href in markdown_links(source.read_text(encoding="utf-8")):
            target = resolve_md(rel, href)
            if target is None:
                continue
            expected = output_url(target)
            if expected is None:
                ERRORS.append(f"{rel}: link target missing for {href}")
            elif expected not in html and expected.rstrip("/") not in html:
                ERRORS.append(f"{rel}: {href} was not rewritten to {expected}")

    origin = "https://biokineticum.github.io"
    en_home = built.get(f"{BASE}/")
    pl_home = built.get(f"{BASE}/pl/")
    if en_home is None or pl_home is None:
        ERRORS.append("home pages are missing")
    else:
        en_text = en_home[2]
        pl_text = pl_home[2]
        title = en_text.split("<title>", 1)[1].split("</title>", 1)[0].strip()
        expected_title = "Journal of AI-Assisted Research for Life Sciences"
        if title != expected_title:
            ERRORS.append(f"English home title is {title!r}")
        pl_title = pl_text.split("<title>", 1)[1].split("</title>", 1)[0].strip()
        if pl_title != expected_title:
            ERRORS.append(f"Polish home title is {pl_title!r}")
        for href in (
            f"{BASE}/docs/en/aims-and-scope/",
            f"{BASE}/docs/en/ai-use-and-disclosure-policy/",
            f"{BASE}/docs/en/ai-disclosure-statement/",
            f"{BASE}/docs/en/peer-review-policy/",
            f"{BASE}/docs/en/author-guidelines/",
            f"{BASE}/docs/en/publication-ethics/",
            f"{BASE}/docs/en/launch-roadmap/",
            f"{BASE}/pl/",
        ):
            if f'href="{href}"' not in en_text:
                ERRORS.append(f"English home is missing href {href}")
        for href in (
            f"{BASE}/docs/pl/aims-and-scope/",
            f"{BASE}/docs/pl/launch-roadmap/",
            f"{BASE}/",
        ):
            if f'href="{href}"' not in pl_text:
                ERRORS.append(f"Polish home is missing href {href}")
        if f'hreflang="pl" href="{origin}{BASE}/pl/"' not in en_text:
            ERRORS.append("English home language switch does not point at the Polish home")
        if f'hreflang="en" href="{origin}{BASE}/"' not in pl_text:
            ERRORS.append("Polish home language switch does not point at the English home")
        for title in (
            "Human-conducted empirical research",
            "AI-assisted writing from real data",
            "Humans are the only authors",
            "Mandatory AI disclosure",
            "AI preliminary review, then human peer review",
            "Gold open access",
        ):
            if title not in en_text:
                ERRORS.append(f"English home is missing principle: {title}")
        for title in (
            "Badanie empiryczne przeprowadzone przez ludzi",
            "Pisanie wspomagane przez AI na podstawie rzeczywistych danych",
            "Autorami są wyłącznie ludzie",
            "Obowiązkowe ujawnienie AI",
            "Wstępna recenzja AI, potem recenzja ekspercka człowieka",
            "Złoty otwarty dostęp",
        ):
            if title not in pl_text:
                ERRORS.append(f"Polish home is missing principle: {title}")
        if 'lang="en"' not in en_text or 'lang="pl"' not in pl_text:
            ERRORS.append("language switcher is missing a language")
        if en_home[1].lang != "en" or pl_home[1].lang != "pl":
            ERRORS.append("home page lang attributes are wrong")

    aims = ROOT / "docs/en/aims-and-scope/index.html"
    if aims.is_file():
        text = aims.read_text(encoding="utf-8")
        polish = f'{origin}{BASE}/docs/pl/aims-and-scope/'
        if f'hreflang="pl" href="{polish}"' not in text:
            ERRORS.append("English aims page does not switch to the Polish aims page")
        if f'href="{BASE}/docs/pl/aims-and-scope/"' not in text:
            ERRORS.append("English aims page is missing the in-document Polish link")
        if 'href="/Journal-of-AI-Assisted-Research-for-Life-Sciences/docs/en/aims-and-scope/" aria-current="page"' not in text and f'href="{BASE}/docs/en/aims-and-scope/" aria-current="page"' not in text:
            ERRORS.append("English aims page does not mark itself current in the navigation")
    else:
        ERRORS.append("English aims page was not built")

    roadmap_text_source = (REPO / "docs/en/launch-roadmap.md").read_text(encoding="utf-8")
    if "see [Publication ethics](publication-ethics.md)" not in roadmap_text_source:
        ERRORS.append("expected the roadmap task-list link used to guard the rewriter")

    roadmap = ROOT / "docs/en/launch-roadmap/index.html"
    if not roadmap.is_file():
        roadmap = ROOT / "docs/en/launch-roadmap.html"
    if roadmap.is_file():
        text = roadmap.read_text(encoding="utf-8")
        for token in (
            "[EDITOR-IN-CHIEF NAME]",
            "[EMAIL]",
            "[PUBLISHER LEGAL NAME]",
            "[DEPUTY EDITOR NAME]",
            "[FUNDING SOURCE]",
        ):
            if token not in text:
                ERRORS.append(f"placeholder missing from the roadmap: {token}")
    else:
        ERRORS.append("English launch roadmap was not built")

    if ERRORS:
        print(f"{len(ERRORS)} problem(s):", file=sys.stderr)
        for error in ERRORS:
            print(f"  {error}", file=sys.stderr)
        sys.exit(1)

    print(f"Checked {len(html_files)} HTML pages and {len(source_docs)} Markdown sources.")


if __name__ == "__main__":
    main()
