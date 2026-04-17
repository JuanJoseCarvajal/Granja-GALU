from granja_galu.application.use_cases.crear_lote import CrearLoteInput
from granja_galu.api.service import build_crear_lote_use_case


def test_crear_lote_ok() -> None:
    use_case = build_crear_lote_use_case()
    lote = use_case.ejecutar(CrearLoteInput(id="L-01", nombre="Norte", hectareas=12.5))

    assert lote.id == "L-01"
    assert lote.nombre == "Norte"
    assert lote.hectareas == 12.5


def test_crear_lote_hectareas_invalidas() -> None:
    use_case = build_crear_lote_use_case()

    try:
        use_case.ejecutar(CrearLoteInput(id="L-02", nombre="Sur", hectareas=0))
        assert False, "Se esperaba ValueError"
    except ValueError as exc:
        assert "hectáreas" in str(exc).lower()
