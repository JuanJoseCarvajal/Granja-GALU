from granja_galu.domain.entities.lote import Lote
from granja_galu.domain.ports.lote_repository import LoteRepository


class LoteRepositoryMemoria(LoteRepository):
    """Implementación en memoria para desarrollo y pruebas."""

    def __init__(self) -> None:
        self._db: dict[str, Lote] = {}

    def guardar(self, lote: Lote) -> None:
        self._db[lote.id] = lote

    def obtener_por_id(self, lote_id: str) -> Lote | None:
        return self._db.get(lote_id)
