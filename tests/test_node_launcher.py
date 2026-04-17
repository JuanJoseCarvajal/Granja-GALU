import json
from pathlib import Path


def test_package_json_has_dev_script() -> None:
    package_json = json.loads(Path("package.json").read_text(encoding="utf-8"))
    scripts = package_json.get("scripts", {})

    assert scripts.get("dev") == "node server.js"


def test_server_js_serves_web_directory() -> None:
    server_js = Path("server.js").read_text(encoding="utf-8")

    assert "const webDir = path.join(__dirname, 'web')" in server_js
    assert "MAI-Natural style app" in server_js
