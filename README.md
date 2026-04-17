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

## ¿Qué tengo que hacer? Paso a paso para verlo en el navegador (estilo MAI-Natural)

1. Estar en la raíz del proyecto:
   ```bash
   cd /workspace/Granja-GALU
   ```
2. Levantar la app web:
   ```bash
   npm run dev
   ```
3. Abrir en navegador:
   - Home: `http://127.0.0.1:3000/`
   - Categorías: `http://127.0.0.1:3000/categorias.html`
   - Productos: `http://127.0.0.1:3000/productos.html`
   - Detalle: `http://127.0.0.1:3000/producto.html?id=hm-12`
   - Carrito: `http://127.0.0.1:3000/carrito.html`
   - Checkout: `http://127.0.0.1:3000/checkout.html`
   - Suscripciones: `http://127.0.0.1:3000/suscripciones.html`

### Comandos exactos (copiar/pegar)

```bash
cd /workspace/Granja-GALU
npm run dev
```

Luego abre:

```text
http://127.0.0.1:3000/
```

Para detener el servidor: `Ctrl + C`.

Opcional (si quieres otro puerto/host):

```bash
HOST=0.0.0.0 PORT=8080 npm run dev
```

## Secciones ya modeladas

- **Home**: Huevos Mágicos, A la Fresca, Pollos Mágicos.
- **Categorías y Productos**: cards por categoría, listado de productos con imagen, detalle por producto.
- **E-commerce base**: carrito (localStorage) y flujo de checkout simulado.
- **Suscripciones**: cards de planes para compra recurrente.

## Testing

```bash
pytest
```
