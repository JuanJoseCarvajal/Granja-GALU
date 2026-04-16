from dataclasses import dataclass, field


@dataclass
class Producto:
    """Producto comercializable de Granja GALU."""

    sku: str
    nombre: str
    categoria: str
    descripcion: str
    atributos: list[str] = field(default_factory=list)
