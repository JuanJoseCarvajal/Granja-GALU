# Template Base — Granja GALU

Este repositorio contiene un template inicial para Granja GALU orientado a promover una vida saludable y consumo consciente.

## Propuesta de valor integrada

- **Huevos Mágicos**: gallinas de libre pastoreo con alimentación basada en fermentos, brotes, vegetales y semillas ricas en D3.
- **A la Fresca**: mix de hojas frescas y flores + verduras de temporada según disponibilidad.
- **Pollos Mágicos**: crianza responsable con enfoque de bienestar animal.
- Otros productos: **panes de masa madre** y **bebidas fermentadas**.

## Estructura

```text
src/granja_galu/          # Modelo de dominio + casos de uso
web/                      # Home/Productos/Suscripciones en HTML para navegador
tests/
```

## ¿Qué tengo que hacer? Paso a paso para verlo en el navegador

1. Estar en la raíz del proyecto:
   ```bash
   cd /workspace/Granja-GALU
   ```
2. Levantar la app:
   ```bash
   python run_app.py
   ```
3. Abrir en navegador:
   - Home: `http://127.0.0.1:8000/index.html`
   - Productos: `http://127.0.0.1:8000/productos.html`
   - Suscripciones: `http://127.0.0.1:8000/suscripciones.html`

### Comandos exactos (copiar/pegar)

```bash
cd /workspace/Granja-GALU
python run_app.py
```

Luego abre:

```text
http://127.0.0.1:8000/index.html
```

Para detener el servidor: `Ctrl + C`.

Opcional (si quieres otro puerto):

```bash
python run_app.py --port 8080
```

## Secciones ya modeladas

- **Home**: Huevos Mágicos, A la Fresca, Pollos Mágicos.
- **Productos**: categorías `huevos_magicos`, `a_la_fresca`, `pollos_magicos`, `panes_masa_madre`, `bebidas_fermentadas`.
- **Suscripciones**: Huevos Mágicos, A la Fresca y Vida Saludable.

## Testing

```bash
pytest
```
