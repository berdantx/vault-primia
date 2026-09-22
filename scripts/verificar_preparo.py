"""Read-only preparation check. Does not install, authenticate, or edit settings."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

EXTENSIONS = {
    "Claude Code": "anthropic.claude-code",
    "Live Server": "ritwickdey.liveserver",
    "Codex (opcional)": "openai.chatgpt",
}


def report(system: str, apps: dict, extensions: list[str] | None) -> dict:
    installed = {name.lower() for name in extensions} if extensions is not None else None
    steps = []
    for label in ("VS Code", "Obsidian"):
        steps.append({"item": label, "estado": "encontrado" if apps.get(label) else "conferir manualmente",
                      "proximo_passo": "Abra o aplicativo e confirme que funciona. A localização sozinha não prova compatibilidade."})
    for label, identifier in EXTENSIONS.items():
        found = installed is not None and identifier in installed
        steps.append({"item": label, "estado": "instalada" if found else "conferir em Extensões no VS Code",
                      "opcional": label.startswith("Codex"),
                      "proximo_passo": ("Confira se está habilitada. " + ("Envie uma mensagem no painel com sua conta." if identifier != "ritwickdey.liveserver" else "O teste Go Live será feito com a pasta site."))})
    return {"sistema": system, "suporte_do_verificador": system in ("Windows", "Darwin"),
            "alteracoes": "nenhuma", "etapas": steps,
            "observacoes": ["Conta, limites, login e habilitação exigem conferência manual.",
                            "A extensão do Claude/Codex não exige que o comando de terminal esteja instalado.",
                            "Se code não estiver no PATH, use o painel Extensões. Isso não bloqueia a aula.",
                            "Nenhum aplicativo, extensão ou plugin foi instalado por este verificador."]}


def inspect_local() -> dict:
    system = platform.system()
    code = shutil.which("code")
    if system == "Windows":
        local = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData/Local")))
        program = Path(os.environ.get("ProgramFiles", "C:/Program Files"))
        vscode_paths = [local / "Programs/Microsoft VS Code/Code.exe", program / "Microsoft VS Code/Code.exe"]
        obsidian_paths = [local / "Obsidian/Obsidian.exe", program / "Obsidian/Obsidian.exe"]
    elif system == "Darwin":
        vscode_paths = [Path("/Applications/Visual Studio Code.app"), Path.home() / "Applications/Visual Studio Code.app"]
        obsidian_paths = [Path("/Applications/Obsidian.app"), Path.home() / "Applications/Obsidian.app"]
    else:
        vscode_paths, obsidian_paths = [], []
    apps = {"VS Code": bool(code) or any(p.exists() for p in vscode_paths),
            "Obsidian": bool(shutil.which("obsidian")) or any(p.exists() for p in obsidian_paths)}
    extensions = None
    if code:
        try:
            result = subprocess.run([code, "--list-extensions"], capture_output=True, text=True, timeout=20,
                                    encoding="utf-8", errors="replace")
            if result.returncode == 0:
                extensions = result.stdout.splitlines()
        except (OSError, subprocess.TimeoutExpired):
            pass
    return report(system, apps, extensions)


def main() -> int:
    parser = argparse.ArgumentParser(description="Conferência opcional e somente leitura; o guia manual sempre funciona sem Python.")
    parser.add_argument("--simular", type=Path, help="JSON de teste com sistema, apps e extensoes; não inspeciona este computador")
    args = parser.parse_args()
    try:
        if args.simular:
            data = json.loads(args.simular.read_text(encoding="utf-8-sig"))
            result = report(data["sistema"], data["apps"], data.get("extensoes"))
        else:
            result = inspect_local()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print("Não foi possível conferir. Siga COMECE-AQUI.md: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
