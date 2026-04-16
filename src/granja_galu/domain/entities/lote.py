from dataclasses import dataclass


@dataclass
class Lote:
    """Representa un lote productivo dentro de la granja."""

    id: str
    nombre: str
    hectareas: float

    def validar(self) -> None:
        if self.hectareas <= 0:
            raise ValueError("Las hectáreas deben ser mayores a cero")
