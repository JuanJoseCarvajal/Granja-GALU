from dataclasses import dataclass, field


@dataclass
class Suscripcion:
    """Plan recurrente para productos frescos y de temporada."""

    codigo: str
    nombre: str
    frecuencia: str
    incluye: list[str] = field(default_factory=list)
    beneficio: str = ""
