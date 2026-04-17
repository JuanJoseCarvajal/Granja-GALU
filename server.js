import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webDir = path.join(__dirname, 'web');

const mimeTypes = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
};

function resolvePath(urlPath) {
  const parsed = new URL(urlPath || '/', `http://${host}:${port}`);
  const pathname = parsed.pathname;
  if (pathname === '/' || pathname === '') return path.join(webDir, 'index.html');
  const normalized = path.normalize(pathname).replace(/^(\.\.(\/|\\|$))+/, '');
  const absolute = path.resolve(webDir, `.${normalized}`);
  const webRoot = path.resolve(webDir);
  if (!absolute.startsWith(webRoot)) return path.join(webDir, 'index.html');
  return absolute;
}

const port = Number(process.env.PORT || 3000);
const host = process.env.HOST || '127.0.0.1';

const server = http.createServer((req, res) => {
  const target = resolvePath(req.url || '/');

  fs.stat(target, (statErr, stats) => {
    if (statErr) {
      res.statusCode = 404;
      res.setHeader('Content-Type', 'text/plain; charset=utf-8');
      res.end('Archivo no encontrado');
      return;
    }

    const finalTarget = stats.isDirectory() ? path.join(target, 'index.html') : target;
    fs.readFile(finalTarget, (err, content) => {
      if (err) {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain; charset=utf-8');
        res.end('Archivo no encontrado');
        return;
      }

      const ext = path.extname(finalTarget).toLowerCase();
      res.statusCode = 200;
      res.setHeader('Content-Type', mimeTypes[ext] || 'application/octet-stream');
      res.end(content);
    });
  });
});

server.listen(port, host, () => {
  console.log(`✅ MAI-Natural style app en http://${host}:${port}`);
  console.log('Rutas: /, /categorias.html, /productos.html, /producto.html?id=hm-12, /carrito.html, /checkout.html, /suscripciones.html');
});
