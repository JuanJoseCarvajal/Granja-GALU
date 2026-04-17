from abc import ABC, abstractmethod

from granja_galu.domain.entities.lote import Lote


class LoteRepository(ABC):
    """Puerto de persistencia para lotes."""

    @abstractmethod
    def guardar(self, lote: Lote) -> None:
        raise NotImplementedError

    @abstractmethod
    def obtener_por_id(self, lote_id: str) -> Lote | None:
        raise NotImplementedError
