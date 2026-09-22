"""Generate small Codex entrypoints; canonical instructions remain in .claude/skills."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- gerado: scripts/sincronizar_skills.py -->"


def expected(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    header = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not header:
        raise ValueError("Frontmatter ausente: " + str(source))
    name = re.search(r"^name: (.+)$", header[1], re.M)
    description = re.search(r"^description: (.+)$", header[1], re.M)
    if not name or not description or name[1] != source.parent.name:
        raise ValueError("Nome/descrição inválido: " + str(source))
    return (f"---\nname: {name[1]}\ndescription: {description[1]}\n---\n\n{MARKER}\n\n"
            f"Leia e siga [as instruções canônicas](../../../.claude/skills/{name[1]}/SKILL.md).\n\n"
            "Resolva os recursos relativos à pasta canônica em .claude/skills, não a esta entrada. "
            "Leia também INSTRUCOES.md e o perfil/projeto pertinente. Os arquivos são compartilhados; as conversas internas não.\n")


def synchronize(root: Path = ROOT, check: bool = False) -> list[str]:
    errors = []
    for source in sorted((root / ".claude/skills").glob("*/SKILL.md")):
        target = root / ".agents/skills" / source.parent.name / "SKILL.md"
        content = expected(source)
        old = target.read_text(encoding="utf-8") if target.exists() else None
        if old == content:
            continue
        if check:
            errors.append("Entrada ausente/desatualizada: " + source.parent.name)
        elif old and MARKER not in old:
            errors.append("Não sobrescrevi entrada personalizada: " + str(target))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8", newline="\n")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    errors = synchronize(check=args.check)
    print("\n".join(errors) if errors else "Entradas de skills conferidas.")
    sys.exit(bool(errors))
