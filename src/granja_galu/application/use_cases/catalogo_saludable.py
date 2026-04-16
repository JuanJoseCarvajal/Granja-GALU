from dataclasses import asdict, dataclass

from granja_galu.domain.entities.producto import Producto
from granja_galu.domain.entities.suscripcion import Suscripcion


@dataclass(frozen=True)
class SeccionHome:
    clave: str
    titulo: str
    descripcion: str
    destacados: list[str]


class CatalogoSaludableUseCase:
    """Entrega contenido para Home, Productos y Suscripciones."""

    def home_sections(self) -> list[dict]:
        sections = [
            SeccionHome(
                clave="huevos_magicos",
                titulo="Huevos Mágicos",
                descripcion=(
                    "Gallinas de libre pastoreo con alimentación basada en fermentos, brotes, "
                    "vegetales y semillas ricas en vitamina D3."
                ),
                destacados=["Caja de 12", "Caja de 30", "Producción ética y regenerativa"],
            ),
            SeccionHome(
                clave="a_la_fresca",
                titulo="A la Fresca",
                descripcion=(
                    "Mix de hojas frescas y flores, más verduras de temporada según disponibilidad."
                ),
                destacados=["Hojas vivas", "Flores comestibles", "Cosecha semanal"],
            ),
            SeccionHome(
                clave="pollos_magicos",
                titulo="Pollos Mágicos",
                descripcion=(
                    "Pollos criados en bienestar, con enfoque natural y trazabilidad de campo a mesa."
                ),
                destacados=["Libre pastoreo", "Nutrición consciente", "Producción responsable"],
            ),
        ]
        return [asdict(section) for section in sections]

    def product_categories(self) -> dict[str, list[dict]]:
        productos = [
            Producto(
                sku="HM-12",
                nombre="Huevos Mágicos x12",
                categoria="huevos_magicos",
                descripcion="Docena de huevos de gallinas de libre pastoreo.",
                atributos=["fermentos", "brotes", "vitamina D3 natural"],
            ),
            Producto(
                sku="HM-30",
                nombre="Huevos Mágicos x30",
                categoria="huevos_magicos",
                descripcion="Caja familiar de 30 huevos para consumo semanal.",
                atributos=["libre pastoreo", "alto valor nutricional"],
            ),
            Producto(
                sku="AF-001",
                nombre="A la Fresca — Mix estacional",
                categoria="a_la_fresca",
                descripcion="Hojas, flores y verduras de temporada según disponibilidad.",
                atributos=["cosecha local", "sin almacenamiento prolongado"],
            ),
            Producto(
                sku="PM-001",
                nombre="Pollo Mágico Entero",
                categoria="pollos_magicos",
                descripcion="Pollo de crianza natural y bienestar animal.",
                atributos=["trazabilidad", "crianza responsable"],
            ),
            Producto(
                sku="PMS-001",
                nombre="Pan de masa madre",
                categoria="panes_masa_madre",
                descripcion="Pan artesanal de fermentación lenta.",
                atributos=["masa madre viva", "fermentación natural"],
            ),
            Producto(
                sku="BF-001",
                nombre="Bebida fermentada de temporada",
                categoria="bebidas_fermentadas",
                descripcion="Bebidas vivas con sabores que cambian según temporada.",
                atributos=["probióticos naturales", "lote pequeño"],
            ),
        ]

        categorias: dict[str, list[dict]] = {}
        for producto in productos:
            categorias.setdefault(producto.categoria, []).append(asdict(producto))
        return categorias

    def suscripciones(self) -> list[dict]:
        planes = [
            Suscripcion(
                codigo="SUS-HM",
                nombre="Suscripción Huevos Mágicos",
                frecuencia="semanal o quincenal",
                incluye=["Caja de 12 o 30", "Entrega programada"],
                beneficio="Precio preferencial y prioridad en disponibilidad.",
            ),
            Suscripcion(
                codigo="SUS-AF",
                nombre="Suscripción A la Fresca",
                frecuencia="semanal",
                incluye=["Mix de hojas", "Flores comestibles", "Verduras de temporada"],
                beneficio="Rotación estacional para mayor diversidad nutricional.",
            ),
            Suscripcion(
                codigo="SUS-FAMILIA",
                nombre="Suscripción Vida Saludable",
                frecuencia="semanal",
                incluye=[
                    "Huevos Mágicos",
                    "A la Fresca",
                    "Pollo Mágico (según ciclo)",
                    "Pan de masa madre o bebida fermentada",
                ],
                beneficio="Canasta integral con ahorro y planificación mensual.",
            ),
        ]
        return [asdict(plan) for plan in planes]
