export const categories = [
  { id: 'huevos', name: 'Huevos Mágicos', image: 'assets/huevos.svg', description: 'Cajas de 12 y 30 huevos de libre pastoreo.' },
  { id: 'fresca', name: 'A la Fresca', image: 'assets/fresca.svg', description: 'Mix de hojas, flores y verduras de temporada.' },
  { id: 'pollos', name: 'Pollos Mágicos', image: 'assets/pollo.svg', description: 'Pollo de crianza responsable y nutrición consciente.' },
  { id: 'panes', name: 'Panes de masa madre', image: 'assets/pan.svg', description: 'Panes de fermentación lenta y artesanal.' },
  { id: 'bebidas', name: 'Bebidas fermentadas', image: 'assets/bebida.svg', description: 'Bebidas vivas de temporada.' },
];

export const products = [
  { id: 'hm-12', category: 'huevos', name: 'Caja Huevos Mágicos x12', price: 15000, image: 'assets/huevos.svg', description: '12 huevos de gallinas libres de jaulas, ricas en D3.' },
  { id: 'hm-30', category: 'huevos', name: 'Caja Huevos Mágicos x30', price: 27000, image: 'assets/huevos.svg', description: '30 huevos para consumo familiar semanal.' },
  { id: 'af-mix', category: 'fresca', name: 'A la Fresca Mix Estacional', price: 22000, image: 'assets/fresca.svg', description: 'Hojas frescas, flores y vegetales según disponibilidad.' },
  { id: 'pm-entero', category: 'pollos', name: 'Pollo Mágico Entero', price: 42000, image: 'assets/pollo.svg', description: 'Pollo de crianza natural con trazabilidad.' },
  { id: 'pan-clasico', category: 'panes', name: 'Pan masa madre clásico', price: 18000, image: 'assets/pan.svg', description: 'Pan artesanal de fermentación natural.' },
  { id: 'beb-kefir', category: 'bebidas', name: 'Bebida fermentada de temporada', price: 16000, image: 'assets/bebida.svg', description: 'Bebida viva con probióticos naturales.' },
];

export const subscriptions = [
  { id: 'sus-quin', name: 'Suscripción Quincenal', price: 120000, items: ['12 huevos', 'Vegetales de temporada', '1 pan de masa madre'], image: 'assets/pan.svg' },
  { id: 'sus-men', name: 'Suscripción Mensual', price: 65000, items: ['12 huevos', 'Vegetales de temporada', '1 bebida fermentada'], image: 'assets/fresca.svg' },
  { id: 'sus-per', name: 'Suscripción Personalizada', price: 65000, items: ['Canasta según preferencia', 'Ajustes por temporada'], image: 'assets/bebida.svg' },
];
