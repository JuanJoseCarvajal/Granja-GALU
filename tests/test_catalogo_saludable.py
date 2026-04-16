from granja_galu.api.content import (
    build_home_content,
    build_product_categories,
    build_subscriptions,
)


def test_home_sections_contiene_lineas_principales() -> None:
    sections = build_home_content()
    claves = {section["clave"] for section in sections}

    assert {"huevos_magicos", "a_la_fresca", "pollos_magicos"}.issubset(claves)


def test_product_categories_contiene_nuevas_categorias() -> None:
    categorias = build_product_categories()

    assert "huevos_magicos" in categorias
    assert "a_la_fresca" in categorias
    assert "pollos_magicos" in categorias
    assert "panes_masa_madre" in categorias
    assert "bebidas_fermentadas" in categorias


def test_subscriptions_contiene_plan_vida_saludable() -> None:
    planes = build_subscriptions()
    nombres = {plan["nombre"] for plan in planes}

    assert "Suscripción Vida Saludable" in nombres
