from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import vault
from sincronizar_skills import synchronize
from verificar_pagina import verify
from verificar_preparo import report


@contextmanager
def empty_vault():
    with tempfile.TemporaryDirectory(prefix="primia teste com espaços ") as temp:
        root = Path(temp)
        (root / "CLAUDE.md").write_bytes((ROOT / "CLAUDE.md").read_bytes())
        yield root


def fixture(kind: str, name: str = "perfil") -> dict:
    return json.loads((ROOT / "exemplos" / kind / (name + ".json")).read_text(encoding="utf-8"))


class ProfileAndProjectTests(unittest.TestCase):
    def test_two_businesses_complete_first_project_and_resume(self):
        for kind in ("servicos", "infoproduto"):
            with self.subTest(kind=kind), empty_vault() as root:
                profile, project = fixture(kind), fixture(kind, "projeto")
                before = sorted(p.name for p in root.iterdir())
                self.assertEqual(vault.apply_profile(root, profile)["status"], "previa")
                self.assertEqual(before, sorted(p.name for p in root.iterdir()))
                self.assertEqual(vault.apply_profile(root, profile, True)["status"], "criado")
                profile_bytes = (root / "perfil.json").read_bytes()
                self.assertEqual(vault.apply_profile(root, profile, True)["status"], "preservado")
                self.assertEqual(profile_bytes, (root / "perfil.json").read_bytes())
                preview = vault.create_project(root, project)
                path = Path(preview["arquivo"])
                self.assertFalse(path.exists())
                self.assertTrue(path.is_relative_to(root / profile["pastas"]["projetos"]))
                created = vault.create_project(root, project, True)
                self.assertEqual(created["status"], "criado")
                content = path.read_text(encoding="utf-8")
                for key in ("oferta", "publico", "problema", "objetivo", "proximo_passo"):
                    self.assertIn(project[key], content)
                self.assertEqual(vault.create_project(root, project, True)["status"], "preservado")
                self.assertEqual(1, len(list(root.rglob("projeto.md"))))
                self.assertEqual([], list((root / profile["pastas"]["diario"]).iterdir()))

    def test_conflicting_profile_or_project_is_not_overwritten(self):
        with empty_vault() as root:
            profile, project = fixture("servicos"), fixture("servicos", "projeto")
            vault.apply_profile(root, profile, True)
            note = Path(vault.create_project(root, project, True)["arquivo"])
            before = {p: p.read_bytes() for p in (root / "perfil.json", note)}
            profile["tom"] = "Outro tom"
            project["objetivo"] = "Outra decisão"
            with self.assertRaises(ValueError):
                vault.apply_profile(root, profile, True)
            with self.assertRaises(ValueError):
                vault.create_project(root, project, True)
            for path, data in before.items():
                self.assertEqual(data, path.read_bytes())

    def test_existing_notes_git_and_obsidian_preferences_are_preserved(self):
        with empty_vault() as root:
            originals = {".git/config": "remote sem alterar", ".obsidian/app.json": '{"theme":"dark"}',
                         "clientes/cliente.md": "nota existente", "diario/ontem.md": "pendência real"}
            for name, text in originals.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            vault.apply_profile(root, fixture("servicos"), True)
            for name, text in originals.items():
                self.assertEqual(text, (root / name).read_text(encoding="utf-8"))

    def test_partial_legacy_profile_requires_review(self):
        with empty_vault() as root:
            original = "# Meu perfil\n## Quem Sou\nNome: Clara\nPúblico: [PREENCHA]\n"
            (root / "CLAUDE.md").write_text(original, encoding="utf-8")
            with self.assertRaises(ValueError):
                vault.apply_profile(root, fixture("servicos"), True)
            self.assertFalse((root / "perfil.json").exists())
            self.assertEqual(original, (root / "CLAUDE.md").read_text(encoding="utf-8"))

    def test_unsafe_windows_and_traversal_paths_fail_before_writes(self):
        invalid = ("../fora", "C:/fora", "/fora", "pasta\\fora", "CON", "nul.txt", "pasta.", "a//b", ".git", "a:b")
        for name in invalid:
            with self.subTest(name=name), empty_vault() as root:
                profile = fixture("servicos")
                profile["pastas"]["projetos"] = name
                with self.assertRaises(ValueError):
                    vault.apply_profile(root, profile, True)
                self.assertFalse((root / "perfil.json").exists())

    def test_overlapping_folders_and_file_collisions_fail(self):
        with empty_vault() as root:
            profile = fixture("servicos")
            profile["pastas"]["clientes"] = "projetos/clientes"
            with self.assertRaises(ValueError):
                vault.apply_profile(root, profile, True)
            (root / "projetos").write_text("preservar", encoding="utf-8")
            with self.assertRaises(ValueError):
                vault.apply_profile(root, fixture("servicos"), True)
            self.assertEqual("preservar", (root / "projetos").read_text())
            self.assertFalse((root / "perfil.json").exists())

    def test_link_cannot_redirect_profile_writes(self):
        with empty_vault() as root, tempfile.TemporaryDirectory() as other:
            try:
                (root / "projetos").symlink_to(other, target_is_directory=True)
            except OSError:
                self.skipTest("Sistema sem permissão de symlink; CI Linux/macOS também cobre este caso")
            with self.assertRaises(ValueError):
                vault.apply_profile(root, fixture("servicos"), True)
            self.assertEqual([], list(Path(other).iterdir()))

    def test_cli_handles_unicode_spaces_and_preview(self):
        with empty_vault() as root:
            input_path = root / "perfil fictício.json"
            input_path.write_text(json.dumps(fixture("infoproduto"), ensure_ascii=False), encoding="utf-8")
            command = [sys.executable, str(ROOT / "scripts/vault.py"), "perfil", "--vault", str(root), "--entrada", str(input_path)]
            self.assertEqual(0, subprocess.run(command, capture_output=True).returncode)
            self.assertFalse((root / "perfil.json").exists())
            self.assertEqual(0, subprocess.run(command + ["--confirmar"], capture_output=True).returncode)
            self.assertTrue((root / "Meus Projetos").is_dir())


class PageTests(unittest.TestCase):
    def check(self, html: str, approved: set[str] | None = None):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "index.html"
            path.write_text(html, encoding="utf-8")
            return verify(path, approved)

    def test_local_template_passes(self):
        self.assertEqual([], verify(ROOT / "modelos/pagina-minima.html"))

    def test_trackers_scripts_resources_and_forms_fail(self):
        cases = ["<script>console.log('ui')</script>", '<script src="https://x.test/a.js"></script>',
                 '<img src="https://x.test/pixel.png">', '<iframe src="https://x.test"></iframe>',
                 '<style>@im/**/port "https://x.test/a.css";</style>', '<style>body{background:uRl(https://x.test/p)}</style>',
                 '<style>@\\69mport "a.css";</style>', '<a href="https://x.test" ping="https://x.test/p">x</a>',
                 '<style>body{background:image-set("https://x.test/pixel.png" 1x)}</style>',
                 '<button onclick="fetch(1)">Enviar</button>', '<form action="https://x.test"><input></form>',
                 '<meta http-equiv="refresh" content="1;url=https://x.test">', '<svg><use href="https://x.test"></use></svg>',
                 '<!-- fbq(123) -->']
        for html in cases:
            with self.subTest(html=html):
                self.assertTrue(self.check(html))

    def test_only_exact_reviewed_destinations_pass(self):
        link = '<a href="https://example.com/contato">Contato</a>'
        self.assertTrue(self.check(link))
        self.assertEqual([], self.check(link, {"https://example.com/contato"}))
        self.assertTrue(self.check(link, {"https://example.com/"}))
        self.assertTrue(self.check('<a href="javascript:alert(1)">x</a>', {"javascript:alert(1)"}))
        self.assertTrue(self.check('<a href="#ausente">x</a>'))
        self.assertEqual([], self.check('<a href="#a">x</a><section id="a">ok</section>'))

    def test_local_images_cannot_escape_site_or_hide_active_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "foto.png").write_bytes(b"\x89PNG\r\n\x1a\n")
            path = root / "index.html"
            path.write_text('<img src="foto.png" alt="foto autorizada">')
            self.assertEqual([], verify(path))
            (root / "foto.png").write_text('<svg onload="fetch(1)"></svg>')
            self.assertTrue(verify(path))
            for source in ("../privado.png", "%2e%2e/privado.png", "//example.com/p.png", "ausente.png"):
                path.write_text('<img src="' + source + '">')
                self.assertTrue(verify(path))


class DiscoveryAndPrepTests(unittest.TestCase):
    def test_every_entry_points_to_one_canonical_skill(self):
        self.assertEqual([], synchronize(ROOT, check=True))
        canonical = {p.parent.name for p in (ROOT / ".claude/skills").glob("*/SKILL.md")}
        entries = {p.parent.name for p in (ROOT / ".agents/skills").glob("*/SKILL.md")}
        self.assertEqual(canonical, entries)
        self.assertFalse(list((ROOT / ".claude/commands").glob("*.md")))
        for entry in (ROOT / ".agents/skills").glob("*/SKILL.md"):
            target = re.search(r"\]\((\.\./[^)]+)\)", entry.read_text(encoding="utf-8"))[1]
            self.assertEqual((ROOT / ".claude/skills" / entry.parent.name / "SKILL.md").resolve(), (entry.parent / target).resolve())
            self.assertTrue((entry.parent / target).is_file())

    def test_manual_preparation_does_not_depend_on_cli_or_codex(self):
        for name in ("preparo-windows.json", "preparo-macos-sem-code.json"):
            data = json.loads((ROOT / "tests/fixtures" / name).read_text())
            result = report(data["sistema"], data["apps"], data["extensoes"])
            self.assertEqual("nenhuma", result["alteracoes"])
            self.assertTrue(result["suporte_do_verificador"])
            self.assertEqual(4, len([s for s in result["etapas"] if not s.get("opcional")]))
            self.assertEqual(1, len([s for s in result["etapas"] if s.get("opcional")]))
            run = subprocess.run([sys.executable, str(ROOT / "scripts/verificar_preparo.py"), "--simular", str(ROOT / "tests/fixtures" / name)], capture_output=True)
            self.assertEqual(0, run.returncode, run.stderr)

    def test_preserve_custom_codex_entry(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / ".claude/skills/exemplo/SKILL.md"
            source.parent.mkdir(parents=True)
            source.write_text("---\nname: exemplo\ndescription: teste\n---\nTexto\n", encoding="utf-8")
            target = root / ".agents/skills/exemplo/SKILL.md"
            target.parent.mkdir(parents=True)
            target.write_text("instrução pessoal", encoding="utf-8")
            self.assertTrue(synchronize(root))
            self.assertEqual("instrução pessoal", target.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
