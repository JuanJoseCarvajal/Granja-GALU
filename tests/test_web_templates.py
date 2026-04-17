from pathlib import Path


WEB_DIR = Path("web")


def test_home_contains_requested_sections() -> None:
    home = (WEB_DIR / "index.html").read_text(encoding="utf-8")

    assert "hero-slide hero-eggs" in home
    assert "Huevos Mágicos" in home
    assert "assets/fried-egg.svg" in home
    assert "Secciones de productos" in home
    assert "home-categories" in home
    assert "Nuestras suscripciones" in home


def test_flow_pages_exist() -> None:
    assert (WEB_DIR / "categorias.html").exists()
    assert (WEB_DIR / "producto.html").exists()
    assert (WEB_DIR / "carrito.html").exists()
    assert (WEB_DIR / "checkout.html").exists()


def test_products_js_contains_categories_products_and_subscriptions() -> None:
    products_js = (WEB_DIR / "products.js").read_text(encoding="utf-8")

    assert "Huevos Mágicos" in products_js
    assert "theme: 'huevos'" in products_js
    assert "theme: 'fresca'" in products_js
    assert "theme: 'pollos'" in products_js
    assert "A la Fresca" in products_js
    assert "Pollos Mágicos" in products_js
    assert "Panes de masa madre" in products_js
    assert "Bebidas fermentadas" in products_js
    assert "Suscripción Quincenal" in products_js


def test_hero_image_asset_exists() -> None:
    assert (WEB_DIR / "assets" / "fried-egg.svg").exists()
