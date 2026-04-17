import { categories, products, subscriptions } from './products.js';
import { addToCart, clearCart, formatPrice, getCartDetailed, removeFromCart } from './cart.js';

function renderCategoryCards(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = categories.map((category) => `
    <article class="card">
      <img src="${category.image}" alt="${category.name}" class="card-img"/>
      <h3>${category.name}</h3>
      <p>${category.description}</p>
      <a class="btn" href="productos.html?categoria=${category.id}">Ver productos</a>
    </article>
  `).join('');
}

function renderProductsGrid(containerId, filterCategory = null) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const filtered = filterCategory ? products.filter((p) => p.category === filterCategory) : products;
  if (!filtered.length) {
    container.innerHTML = '<p>No hay productos para esta categoría por ahora.</p>';
    return;
  }

  container.innerHTML = filtered.map((product) => `
    <article class="card">
      <img src="${product.image}" alt="${product.name}" class="card-img"/>
      <h3>${product.name}</h3>
      <p>${product.description}</p>
      <p class="price">${formatPrice(product.price)}</p>
      <div class="actions">
        <a class="btn btn-light" href="producto.html?id=${product.id}">Ver detalle</a>
        <button class="btn" data-add-cart="${product.id}">Agregar al carrito</button>
      </div>
    </article>
  `).join('');

  container.querySelectorAll('[data-add-cart]').forEach((btn) => {
    btn.addEventListener('click', () => {
      addToCart(btn.dataset.addCart);
      alert('Producto agregado al carrito');
    });
  });
}

function renderSubscriptions(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = subscriptions.map((plan) => `
    <article class="card">
      <img src="${plan.image}" alt="${plan.name}" class="card-img"/>
      <h3>${plan.name}</h3>
      <p class="price">${formatPrice(plan.price)}</p>
      <ul>${plan.items.map((item) => `<li>${item}</li>`).join('')}</ul>
      <button class="btn">Unirte a la suscripción</button>
    </article>
  `).join('');
}

function renderProductDetail() {
  const container = document.getElementById('product-detail');
  if (!container) return;

  const params = new URLSearchParams(window.location.search);
  const product = products.find((p) => p.id === params.get('id'));
  if (!product) {
    container.innerHTML = '<p>Producto no encontrado.</p>';
    return;
  }

  container.innerHTML = `
    <article class="detail">
      <img src="${product.image}" alt="${product.name}" class="detail-img"/>
      <div>
        <h2>${product.name}</h2>
        <p>${product.description}</p>
        <p class="price">${formatPrice(product.price)}</p>
        <button class="btn" id="add-detail-cart">Agregar al carrito</button>
      </div>
    </article>
  `;

  document.getElementById('add-detail-cart').addEventListener('click', () => {
    addToCart(product.id);
    alert('Producto agregado al carrito');
  });
}

function renderCart() {
  const container = document.getElementById('cart-items');
  const totalEl = document.getElementById('cart-total');
  if (!container || !totalEl) return;

  const items = getCartDetailed();
  if (!items.length) {
    container.innerHTML = '<p>Tu carrito está vacío.</p>';
    totalEl.textContent = formatPrice(0);
    return;
  }

  container.innerHTML = items.map((item) => `
    <article class="cart-row">
      <div>
        <h3>${item.product.name}</h3>
        <p>Cantidad: ${item.qty}</p>
      </div>
      <div>
        <p>${formatPrice(item.subtotal)}</p>
        <button class="btn btn-light" data-remove="${item.productId}">Quitar</button>
      </div>
    </article>
  `).join('');

  const total = items.reduce((acc, item) => acc + item.subtotal, 0);
  totalEl.textContent = formatPrice(total);

  container.querySelectorAll('[data-remove]').forEach((btn) => {
    btn.addEventListener('click', () => {
      removeFromCart(btn.dataset.remove);
      renderCart();
    });
  });
}

function setupCheckoutForm() {
  const form = document.getElementById('checkout-form');
  const summary = document.getElementById('checkout-summary');
  if (!form || !summary) return;

  const items = getCartDetailed();
  const total = items.reduce((acc, item) => acc + item.subtotal, 0);
  summary.innerHTML = `
    <h3>Resumen de compra</h3>
    <p>Items: ${items.length}</p>
    <p>Total: ${formatPrice(total)}</p>
  `;

  if (!items.length) {
    summary.innerHTML += '<p>No tienes productos en el carrito.</p>';
  }

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!items.length) {
      alert('Agrega productos al carrito antes de pagar.');
      window.location.href = 'productos.html';
      return;
    }
    clearCart();
    alert('¡Pago simulado exitoso! Te contactaremos con la confirmación.');
    window.location.href = 'index.html';
  });
}

function main() {
  const page = document.body.dataset.page;
  renderCategoryCards('home-categories');
  renderSubscriptions('home-subscriptions');

  if (page === 'categorias') renderCategoryCards('categories-grid');
  if (page === 'productos') {
    const params = new URLSearchParams(window.location.search);
    renderProductsGrid('products-grid', params.get('categoria'));
  }
  if (page === 'producto') renderProductDetail();
  if (page === 'carrito') renderCart();
  if (page === 'checkout') setupCheckoutForm();
}

main();
