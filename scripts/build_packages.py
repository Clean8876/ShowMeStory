# scripts/build_packages.py
from pathlib import Path
import tempfile
import zipfile

REQUIRED = (
    "SKILL.md",
    "references/research-shows.md",
    "references/spoiler-rules.md",
    "references/comic-format.md",
    "references/review-story.md",
)


def build(root):
    root = Path(root)
    source = root / "plugins/showvilla/skills/tell-story"
    missing = [name for name in REQUIRED if not (source / name).is_file()]
    if missing:
        raise FileNotFoundError("Missing skill files: " + ", ".join(missing))
    files = [
        (path.relative_to(source).as_posix(), path.read_bytes())
        for path in sorted(source.rglob("*")) if path.is_file()
    ]
    output = root / "dist"
    output.mkdir(parents=True, exist_ok=True)
    targets = (
        ("showvilla-claude-skill.zip", "tell-story/"),
        ("showvilla-gemini-skill.zip", ""),
    )
    with tempfile.TemporaryDirectory(dir=output) as temporary:
        staged = []
        for filename, prefix in targets:
            path = Path(temporary) / filename
            with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
                for relative, data in files:
                    archive.writestr(prefix + relative, data)
            staged.append((path, output / filename))
        for path, destination in staged:
            path.replace(destination)
    return [output / filename for filename, _ in targets]


if __name__ == "__main__":
    for path in build(Path(__file__).resolve().parents[1]):
        print(path)
