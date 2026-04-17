from pathlib import Path

from granja_galu import run_app


def test_web_directory_exists() -> None:
    web_dir = Path(run_app.__file__).resolve().parents[2] / "web"
    assert web_dir.exists()


def test_parse_args_defaults(monkeypatch) -> None:
    monkeypatch.setattr("sys.argv", ["run_app.py"])
    args = run_app.parse_args()

    assert args.host == "127.0.0.1"
    assert args.port == 8000
