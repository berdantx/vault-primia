"""Optional, local-only helpers for reviewed profiles and project notes. Python 3.10+."""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys
import unicodedata

DEFAULT_FOLDERS = {
    "projetos": "projetos", "clientes": "clientes", "inbox": "inbox",
    "diario": "diario", "reunioes": "reunioes", "pesquisa": "pesquisa",
    "conteudo": "conteudo", "arquivo": "arquivo", "pessoal": "pessoal",
}
PROFILE_FIELDS = ("nome", "negocio", "publico", "oferta", "regiao", "objetivos", "tom", "escopo")
PROJECT_FIELDS = ("nome", "oferta", "publico", "problema", "objetivo", "proximo_passo")
RESERVED = re.compile(r"^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)", re.I)


def path_parts(relative: str) -> list[str]:
    """Validate portable relative syntax independently of the current directory."""
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("Use caminho relativo com /, dentro do vault.")
    parts = relative.split("/")
    if PurePosixPath(relative).is_absolute() or any(
        p in ("", ".", "..") or p.startswith(".") or p.endswith((".", " "))
        or any(c in p for c in '<>:"|?*') or any(ord(c) < 32 for c in p)
        or RESERVED.match(p) for p in parts
    ):
        raise ValueError("Caminho inválido ou incompatível com Windows: " + relative)
    return parts


def safe_path(root: Path, relative: str) -> Path:
    """Keep portable paths inside the vault and reject symlinks/junctions."""
    parts = path_parts(relative)
    root = root.resolve(strict=True)
    target = root
    for part in parts:
        target /= part
        if target.is_symlink() or getattr(target, "is_junction", lambda: False)():
            raise ValueError("O destino contém um link de pasta/arquivo: " + relative)
    if not target.resolve().is_relative_to(root):
        raise ValueError("O destino sai do vault.")
    return target


def read_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("O arquivo de entrada precisa conter um objeto JSON.")
    return data


def text_fields(data: dict, fields: tuple) -> dict:
    result = {}
    for name in fields:
        value = data.get(name)
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Preencha o campo " + name + " com texto (ou 'a definir').")
        if "\x00" in value:
            raise ValueError("Texto inválido no campo " + name)
        result[name] = value.strip()
    return result


def validate_profile(data: dict) -> dict:
    result = text_fields(data, PROFILE_FIELDS)
    extra = set(data) - set(PROFILE_FIELDS) - {"pastas"}
    if extra:
        raise ValueError("Campos não reconhecidos: " + ", ".join(sorted(extra)))
    folders = data.get("pastas", DEFAULT_FOLDERS.copy())
    if not isinstance(folders, dict) or set(folders) != set(DEFAULT_FOLDERS):
        raise ValueError("pastas deve mapear todas as categorias do modelo de perfil.")
    # Validate syntax independently of whether the directories exist yet.
    for name in folders.values():
        path_parts(name)
    values = [v.casefold() for v in folders.values()]
    for i, a in enumerate(values):
        if any(a == b or a.startswith(b + "/") or b.startswith(a + "/") for b in values[i + 1:]):
            raise ValueError("Cada categoria precisa ter uma pasta separada, sem sobreposição.")
    result["pastas"] = folders
    return result


def apply_profile(root: Path, data: dict, confirm: bool = False) -> dict:
    """Create-only: never overwrite or merge an existing personal profile."""
    normalized = validate_profile(data)
    destination = safe_path(root, "perfil.json")
    folders = [safe_path(root, value) for value in normalized["pastas"].values()]
    for folder in folders:
        if folder.exists() and not folder.is_dir():
            raise ValueError("Uma pasta necessária está ocupada por um arquivo: " + str(folder))
    if destination.exists():
        if read_json(destination) == normalized:
            return {"status": "preservado", "arquivo": str(destination)}
        raise ValueError("Já existe perfil.json. Leia e revise a alteração com o dono; este comando não sobrescreve perfis.")
    # An older customized CLAUDE.md is evidence of an existing profile, not a blank kit.
    legacy = root / "CLAUDE.md"
    if legacy.exists():
        content = legacy.read_text(encoding="utf-8-sig")
        if "## Quem Sou" in content:
            raise ValueError("Há um perfil antigo em CLAUDE.md. Migre com revisão, preservando o original.")
    plan = {"status": "previa", "arquivo": str(destination), "pastas": [str(p) for p in folders]}
    if not confirm:
        return plan
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(normalized, ensure_ascii=False, indent=2) + "\n")
    return {**plan, "status": "criado"}


def slug(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:70].rstrip("-")
    if not value or RESERVED.match(value):
        raise ValueError("Use um nome de projeto com letras/números e que não seja reservado pelo sistema.")
    return value


def project_note(data: dict) -> str:
    d = text_fields(data, PROJECT_FIELDS)
    if set(data) - set(PROJECT_FIELDS) - {"definido", "hipoteses", "pendencias"}:
        raise ValueError("O projeto contém campos não reconhecidos.")
    sections = []
    for field, title in [("definido", "O que está definido"), ("hipoteses", "Hipóteses"), ("pendencias", "Pendências")]:
        values = data.get(field, [])
        if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
            raise ValueError(field + " deve ser uma lista de textos.")
        sections.append("## " + title + "\n\n" + ("\n".join("- " + v.strip() for v in values) or "Não registrado nesta revisão."))
    return (f"# Projeto: {d['nome']}\n\nStatus: revisado pelo participante antes de salvar.\n\n"
            f"## O que ofereço ou quero desenvolver\n\n{d['oferta']}\n\n"
            f"## Para quem\n\n{d['publico']}\n\n## Qual problema resolve\n\n{d['problema']}\n\n"
            f"## Objetivo deste projeto\n\n{d['objetivo']}\n\n" + "\n\n".join(sections) +
            f"\n\n## Próximo passo\n\n{d['proximo_passo']}\n\n"
            "## Materiais relacionados\n\nAcrescente aqui os caminhos da pesquisa, oferta, direção visual e página conforme forem criados.\n")


def create_project(root: Path, data: dict, confirm: bool = False) -> dict:
    profile = validate_profile(read_json(safe_path(root, "perfil.json")))
    content = project_note(data)
    relative = profile["pastas"]["projetos"] + "/" + slug(data["nome"]) + "/projeto.md"
    destination = safe_path(root, relative)
    if destination.exists():
        if destination.read_text(encoding="utf-8") == content:
            return {"status": "preservado", "arquivo": str(destination)}
        raise ValueError("Esse projeto já existe. Revise a nota existente; não sobrescreva nem crie uma cópia sem necessidade.")
    if not confirm:
        return {"status": "previa", "arquivo": str(destination), "conteudo": content}
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(content)
    return {"status": "criado", "arquivo": str(destination)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Salvar perfil/projeto revisado, sem instalar ou enviar nada. Sem --confirmar, só mostra a prévia.")
    parser.add_argument("acao", choices=["perfil", "projeto"])
    parser.add_argument("--vault", type=Path, default=Path.cwd())
    parser.add_argument("--entrada", type=Path, required=True)
    parser.add_argument("--confirmar", action="store_true", help="Usar apenas após a revisão do participante")
    args = parser.parse_args()
    try:
        root = args.vault.resolve(strict=True)
        if not root.is_dir():
            raise ValueError("--vault deve indicar uma pasta existente.")
        result = (apply_profile if args.acao == "perfil" else create_project)(root, read_json(args.entrada), args.confirmar)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print("Não alterei o perfil/projeto: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
