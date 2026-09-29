"""Check Astra's local links and story structure; standard library, read-only."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ASTRA = Path(__file__).resolve().parents[1]
WORKSPACE = ASTRA.parent
STORY = re.compile(r"^### (AST-\d{3}) — (.+)$", re.MULTILINE)
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
EXPECTED = {f"AST-{number:03d}" for number in range(1, 97)}


def prose(text):
    return re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)


def anchors(path):
    text = path.read_text(encoding="utf-8")
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    seen = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def main():
    errors = []
    markdown = sorted(ASTRA.rglob("*.md"))
    # Personal notebooks may contain intentionally unfinished learner links.
    markdown = [path for path in markdown if "work" not in path.relative_to(ASTRA).parts]
    stories = {}
    link_count = 0
    external_source_paths = set()
    anchor_cache = {}
    modules = sorted((ASTRA / "modules").glob("*.md"))
    if len(modules) != 16:
        errors.append(f"Expected 16 modules, found {len(modules)}")

    for path in markdown:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ASTRA)
        if len(re.findall(r"^```", text, re.MULTILINE)) % 2:
            errors.append(f"{relative}: unbalanced code fences")
        table_columns = None
        in_code = False
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.startswith("```"):
                in_code = not in_code
                table_columns = None
                continue
            if in_code:
                continue
            if line.startswith("|"):
                columns = len(re.split(r"(?<!\\)\|", line)) - 2
                if table_columns is None:
                    table_columns = columns
                elif columns != table_columns:
                    errors.append(f"{relative}:{line_number}: table has {columns} columns, expected {table_columns}")
            else:
                table_columns = None
        for raw in LINK.findall(prose(text)):
            target_text = raw.strip().strip("<>")
            parsed = urlsplit(target_text)
            if parsed.scheme or target_text.startswith("//"):
                continue
            link_count += 1
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(WORKSPACE):
                errors.append(f"{relative}: local link leaves workspace: {raw}")
                continue
            if not target.exists():
                errors.append(f"{relative}: missing target: {raw}")
                continue
            if not target.is_relative_to(ASTRA):
                external_source_paths.add(target)
            if parsed.fragment and target.suffix == ".md":
                if target not in anchor_cache:
                    anchor_cache[target] = anchors(target)
                if unquote(parsed.fragment) not in anchor_cache[target]:
                    errors.append(f"{relative}: missing anchor: {raw}")

    required = ("**Mode:**", "**Estimate:**", "**Depends on:**", "**Story:**",
                "**Start here:**", "**Acceptance:**", "**Verify:**", "**Hint / review:**")
    for path in modules:
        text = path.read_text(encoding="utf-8")
        matches = list(STORY.finditer(text))
        if len(matches) != 6:
            errors.append(f"{path.name}: expected six stories, found {len(matches)}")
        for index, match in enumerate(matches):
            story_id, title = match.groups()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            body = text[match.end():end]
            if story_id in stories:
                errors.append(f"Duplicate story: {story_id}")
            stories[story_id] = (path, title)
            for label in required:
                if label not in body:
                    errors.append(f"{story_id}: missing {label}")
            if f'<a id="{story_id.lower()}"></a>' not in text:
                errors.append(f"{story_id}: missing stable anchor")
            dep_match = re.search(r"\*\*Depends on:\*\* ([^\n]+)", body)
            if dep_match:
                dependencies = re.findall(r"AST-\d{3}", dep_match.group(1))
                if not dependencies and dep_match.group(1).strip() != "None":
                    errors.append(f"{story_id}: invalid prerequisite text")
                for dependency in dependencies:
                    if dependency not in EXPECTED or dependency >= story_id:
                        errors.append(f"{story_id}: invalid/later prerequisite {dependency}")
                number = int(story_id[4:])
                expected_dep = [] if number == 1 else [f"AST-{(60 if number > 60 and (number - 1) % 6 == 0 else number - 1):03d}"]
                if dependencies != expected_dep:
                    errors.append(f"{story_id}: expected prerequisites {expected_dep}, found {dependencies}")
            if len(re.findall(r"^- ", body, re.MULTILINE)) < 2:
                errors.append(f"{story_id}: too few explicit acceptance criteria")

    if set(stories) != EXPECTED:
        errors.append(f"Story ids differ: missing {sorted(EXPECTED - set(stories))}; unexpected {sorted(set(stories) - EXPECTED)}")
    for name in ("stories/README.md", "TRACKER.md"):
        path = ASTRA / name
        if not path.exists():
            errors.append(f"Missing navigation file: {name}")
            continue
        ids = re.findall(r"\[(AST-\d{3})\]\(", path.read_text(encoding="utf-8"))
        if set(ids) != EXPECTED or len(ids) != len(EXPECTED):
            errors.append(f"{name}: must link every story exactly once")

    if errors:
        print("Curriculum check FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    words = sum(len(path.read_text(encoding="utf-8").split()) for path in markdown)
    print(f"PASS: {len(markdown)} Markdown files, {len(modules)} modules, {len(stories)} stories")
    print(f"PASS: {link_count} local links/fragments; {len(external_source_paths)} distinct linked application/source paths")
    print("PASS: story fields, prerequisites, stable anchors, index, tracker, tables, and code fences")
    print(f"Approximate Markdown word count: {words:,}")
    print("Application builds/tests and external URLs are outside this checker's scope.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
