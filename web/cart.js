import { products } from './products.js';

const CART_KEY = 'granja_galu_cart';

export function getCart() {
  const raw = localStorage.getItem(CART_KEY);
  return raw ? JSON.parse(raw) : [];
}

export function saveCart(items) {
  localStorage.setItem(CART_KEY, JSON.stringify(items));
}

export function addToCart(productId, qty = 1) {
  const cart = getCart();
  const item = cart.find((it) => it.productId === productId);
  if (item) item.qty += qty;
  else cart.push({ productId, qty });
  saveCart(cart);
}

export function removeFromCart(productId) {
  saveCart(getCart().filter((it) => it.productId !== productId));
}

export function clearCart() {
  saveCart([]);
}

export function getCartDetailed() {
  return getCart().map((item) => {
    const product = products.find((p) => p.id === item.productId);
    return {
      ...item,
      product,
      subtotal: product ? product.price * item.qty : 0,
    };
  });
}

export function formatPrice(value) {
  return new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(value);
}
