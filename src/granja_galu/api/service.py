"""Punto de composición de dependencias (composition root)."""

from granja_galu.application.use_cases.crear_lote import CrearLoteUseCase
from granja_galu.infrastructure.repositories.lote_repository_mem import LoteRepositoryMemoria


def build_crear_lote_use_case() -> CrearLoteUseCase:
    repository = LoteRepositoryMemoria()
    return CrearLoteUseCase(repository)
