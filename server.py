import http.server
import socketserver
import os

PORT = 8001

class CachedSimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        path = self.translate_path(self.path)
        if os.path.isfile(path):
            ext = os.path.splitext(path)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.woff', '.woff2', '.ttf', '.css', '.js']:
                # Cache static assets for 1 year (Standard Lighthouse recommendation)
                self.send_header('Cache-Control', 'public, max-age=31536000, immutable')
            elif ext in ['.html']:
                # Do not cache HTML to ensure updates are seen immediately
                self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

# Allow port reuse to avoid 'Address already in use' socket errors on restarts
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), CachedSimpleHTTPRequestHandler) as httpd:
    print(f"Serving with Cache-Control headers at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
