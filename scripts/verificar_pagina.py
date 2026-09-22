"""Conservative checks for the workshop's script-free local HTML route, not a security audit."""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

TRACKERS = re.compile(r"googletagmanager|google-analytics|fbq\s*\(|fbevents|clarity\.ms|hotjar|leadtracker|pixelyoursite", re.I)
BLOCKED_TAGS = {"script", "iframe", "object", "embed", "base", "link", "svg", "math", "video", "audio", "source", "applet", "portal", "frame", "frameset"}


class Review(HTMLParser):
    def __init__(self, path: Path, approved: set[str]):
        super().__init__(convert_charrefs=True)
        self.path, self.approved = path.resolve(), approved
        self.errors: list[str] = []
        self.ids: set[str] = set()
        self.anchors: list[str] = []
        self.style = False

    def error(self, message: str) -> None:
        self.errors.append(f"Linha {self.getpos()[0]}: {message}")

    def css(self, text: str) -> None:
        compact = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
        if re.search(r"url\s*\(|image(?:-set)?\s*\(|@import|expression\s*\(|\\", compact, re.I):
            self.error("CSS com carregamento/escape: use CSS interno sem url(), import ou código ativo nesta rota.")

    def image(self, source: str) -> None:
        decoded = unquote(source)
        parsed = urlsplit(decoded)
        if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment or "\\" in decoded:
            self.error("Use imagem local autorizada, sem URL externa ou parâmetros.")
            return
        path = self.path.parent / decoded
        if not decoded or Path(decoded).is_absolute() or ".." in Path(decoded).parts:
            self.error("Imagem fora da pasta site.")
            return
        if not path.resolve().is_relative_to(self.path.parent) or any(p.is_symlink() or getattr(p, "is_junction", lambda: False)() for p in [path, *path.parents] if p != self.path.parent):
            self.error("Imagem aponta para fora da pasta ou usa link de arquivo.")
            return
        try:
            data = path.read_bytes()
            png = path.suffix.lower() == ".png" and data.startswith(b"\x89PNG\r\n\x1a\n")
            jpeg = path.suffix.lower() in (".jpg", ".jpeg") and data.startswith(b"\xff\xd8\xff")
            webp = path.suffix.lower() == ".webp" and data.startswith(b"RIFF") and data[8:12] == b"WEBP"
            if not (png or jpeg or webp):
                self.error("Imagem deve ser PNG, JPEG ou WebP local válido.")
        except OSError:
            self.error("Imagem local não encontrada: " + source)

    def handle_starttag(self, tag: str, attrs: list) -> None:
        a = dict(attrs)
        if tag in BLOCKED_TAGS:
            self.error("Elemento não permitido na rota estática sem rastreadores: " + tag)
        if tag == "style":
            self.style = True
        if "id" in a:
            if a["id"] in self.ids:
                self.error("ID duplicado: " + a["id"])
            self.ids.add(a["id"])
        for key, value in attrs:
            if key.startswith("on") or key in ("srcdoc", "ping", "action", "formaction", "background", "srcset", "http-equiv", "manifest"):
                self.error("Atributo ativo/de envio não permitido: " + key)
            if key == "style":
                self.css(value or "")
            if key in ("src", "href", "xlink:href", "data", "poster"):
                if tag == "a" and key == "href":
                    if value and value.startswith("#"):
                        self.anchors.append(value[1:])
                    elif value not in self.approved or urlsplit(value or "").scheme not in ("https", "mailto", "tel"):
                        self.error("Destino deve ser revisado e autorizado explicitamente: " + str(value))
                elif tag == "img" and key == "src":
                    self.image(value or "")
                else:
                    self.error("Carregamento de recurso não permitido: " + tag + "/" + key)
        if tag in ("input", "button", "select", "textarea") and "disabled" not in a:
            self.error("Controle de demonstração precisa estar desabilitado; use links revisados para navegação.")

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self.style = False

    def handle_data(self, data: str) -> None:
        if self.style:
            self.css(data)


def verify(path: Path, approved: set[str] | None = None) -> list[str]:
    content = path.read_text(encoding="utf-8-sig")
    review = Review(path, approved or set())
    review.feed(content)
    review.close()
    review.errors.extend("Âncora sem destino: #" + anchor for anchor in review.anchors if anchor and anchor not in review.ids)
    if TRACKERS.search(content):
        review.errors.append("Há referência a rastreador conhecido no HTML. Remova também códigos comentados.")
    return review.errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Confere HTML local novo; não executa nem limpa uma captura de terceiros.")
    parser.add_argument("arquivo", type=Path)
    parser.add_argument("--permitir-destino", action="append", default=[], help="URL exata revisada pelo dono; repetir para cada contato/link")
    args = parser.parse_args()
    try:
        errors = verify(args.arquivo, set(args.permitir_destino))
        for error in errors:
            print(error)
        if not errors:
            print("Verificações estáticas passaram. Revise conteúdo, licença das imagens, destinos e rede no navegador; isto não é uma auditoria completa.")
        return 1 if errors else 0
    except (OSError, ValueError) as exc:
        print("Não foi possível conferir: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
