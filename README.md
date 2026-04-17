# Template Base — Granja GALU

Este repositorio contiene un **template inicial** para Granja GALU, inspirado en una arquitectura tipo MAI-Natural, orientado a promover una vida saludable y consumo consciente.

## Propuesta de valor integrada

- **Huevos Mágicos**: gallinas de libre pastoreo con alimentación basada en fermentos, brotes, vegetales y semillas ricas en D3.
- **A la Fresca**: mix de hojas frescas y flores + verduras de temporada según disponibilidad.
- **Pollos Mágicos**: crianza responsable con enfoque de bienestar animal.
- Otros productos: **panes de masa madre** y **bebidas fermentadas**.

## Estructura

```text
src/granja_galu/
  api/                    # Entradas/salidas y builders de contenido
  application/
    use_cases/            # Casos de uso
  domain/
    entities/             # Entidades de negocio
    value_objects/        # Objetos de valor
    ports/                # Interfaces del dominio
  infrastructure/
    config/
    repositories/
tests/
```

## Secciones ya modeladas

El template incluye contenido listo para:

1. **Home**:
   - Sección Huevos Mágicos.
   - Sección A la Fresca.
   - Sección Pollos Mágicos.
2. **Página de productos** con categorías:
   - `huevos_magicos`
   - `a_la_fresca`
   - `pollos_magicos`
   - `panes_masa_madre`
   - `bebidas_fermentadas`
3. **Suscripciones**:
   - Huevos Mágicos.
   - A la Fresca.
   - Vida Saludable (canasta integral).

## Desarrollo

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```
