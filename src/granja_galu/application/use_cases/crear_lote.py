from dataclasses import dataclass

from granja_galu.domain.entities.lote import Lote
from granja_galu.domain.ports.lote_repository import LoteRepository


@dataclass
class CrearLoteInput:
    id: str
    nombre: str
    hectareas: float


class CrearLoteUseCase:
    def __init__(self, repository: LoteRepository) -> None:
        self.repository = repository

    def ejecutar(self, payload: CrearLoteInput) -> Lote:
        lote = Lote(
            id=payload.id,
            nombre=payload.nombre,
            hectareas=payload.hectareas,
        )
        lote.validar()
        self.repository.guardar(lote)
        return lote
