from granja_galu.application.use_cases.catalogo_saludable import CatalogoSaludableUseCase


def build_home_content() -> list[dict]:
    return CatalogoSaludableUseCase().home_sections()


def build_product_categories() -> dict[str, list[dict]]:
    return CatalogoSaludableUseCase().product_categories()


def build_subscriptions() -> list[dict]:
    return CatalogoSaludableUseCase().suscripciones()
