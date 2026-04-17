from pathlib import Path


WEB_DIR = Path("web")


def test_home_contains_requested_sections() -> None:
    home = (WEB_DIR / "index.html").read_text(encoding="utf-8")

    assert "Huevos Mágicos" in home
    assert "A la Fresca" in home
    assert "Pollos Mágicos" in home


def test_productos_contains_requested_categories() -> None:
    productos = (WEB_DIR / "productos.html").read_text(encoding="utf-8")

    assert "huevos_magicos" in productos
    assert "a_la_fresca" in productos
    assert "pollos_magicos" in productos
    assert "panes_masa_madre" in productos
    assert "bebidas_fermentadas" in productos


def test_suscripciones_contains_planes() -> None:
    suscripciones = (WEB_DIR / "suscripciones.html").read_text(encoding="utf-8")

    assert "Suscripción Huevos Mágicos" in suscripciones
    assert "Suscripción A la Fresca" in suscripciones
    assert "Suscripción Vida Saludable" in suscripciones
