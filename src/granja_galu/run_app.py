"""Lanzador local para ver Granja GALU en navegador."""

from __future__ import annotations

import argparse
import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Servidor local de Granja GALU")
    parser.add_argument("--host", default="127.0.0.1", help="Host de escucha")
    parser.add_argument("--port", type=int, default=8000, help="Puerto de escucha")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    web_dir = Path(__file__).resolve().parents[2] / "web"

    if not web_dir.exists():
        raise FileNotFoundError(f"No existe la carpeta web: {web_dir}")

    os.chdir(web_dir)
    server = ThreadingHTTPServer((args.host, args.port), SimpleHTTPRequestHandler)
    print(f"✅ Granja GALU disponible en http://{args.host}:{args.port}/index.html")
    print("Presiona Ctrl + C para detener el servidor")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
