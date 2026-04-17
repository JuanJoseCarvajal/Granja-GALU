from pathlib import Path


WEB_DIR = Path("web")


def test_main_js_has_cart_and_checkout_flow() -> None:
    main_js = (WEB_DIR / "main.js").read_text(encoding="utf-8")

    assert "renderCart" in main_js
    assert "setupCheckoutForm" in main_js
    assert "window.location.href = 'index.html'" in main_js


def test_cart_js_uses_local_storage() -> None:
    cart_js = (WEB_DIR / "cart.js").read_text(encoding="utf-8")

    assert "localStorage" in cart_js
    assert "addToCart" in cart_js
    assert "getCartDetailed" in cart_js
