# tests/test_packages.py
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def load_builder():
    spec = importlib.util.spec_from_file_location(
        "showvilla_builder", ROOT / "scripts/build_packages.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "plugins/showvilla/skills/tell-story"
        (self.skill / "references").mkdir(parents=True)
        self.files = {
            "SKILL.md": b"---\nname: tell-story\ndescription: Test\n---\n",
            "references/research-shows.md": b"Research\n",
            "references/spoiler-rules.md": b"Spoilers\n",
            "references/comic-format.md": "Comic \U0001f4a5\n".encode(),
            "references/review-story.md": b"Review\n",
        }
        for name, data in self.files.items():
            (self.skill / name).write_bytes(data)

    def test_complete_archives_and_portable_paths(self):
        paths = load_builder().build(self.root)
        self.assertEqual(
            {p.name for p in paths},
            {"showvilla-claude-skill.zip", "showvilla-gemini-skill.zip"},
        )
        for path in paths:
            prefix = "tell-story/" if "claude" in path.name else ""
            with zipfile.ZipFile(path) as archive:
                self.assertEqual(
                    set(archive.namelist()),
                    {prefix + name for name in self.files},
                )
                self.assertTrue(all("\\" not in n for n in archive.namelist()))
                for name, data in self.files.items():
                    self.assertEqual(archive.read(prefix + name), data)

    def test_rebuild_includes_edited_source(self):
        builder = load_builder()
        builder.build(self.root)
        changed = b"Revised rules\n"
        (self.skill / "references/comic-format.md").write_bytes(changed)
        for path in builder.build(self.root):
            prefix = "tell-story/" if "claude" in path.name else ""
            with zipfile.ZipFile(path) as archive:
                self.assertEqual(
                    archive.read(prefix + "references/comic-format.md"), changed
                )

    def test_missing_guide_preserves_existing_archives(self):
        builder = load_builder()
        paths = builder.build(self.root)
        before = {p: p.read_bytes() for p in paths}
        (self.skill / "references/review-story.md").unlink()
        with self.assertRaises(FileNotFoundError):
            builder.build(self.root)
        for path, data in before.items():
            self.assertEqual(path.read_bytes(), data)


if __name__ == "__main__":
    unittest.main()
