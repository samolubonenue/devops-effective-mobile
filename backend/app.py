#!/usr/bin/env python3
"""Simple HTTP server for Effective Mobile test task."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = int(os.environ.get("PORT", 8080))


class RequestHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests."""

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/health":
            self._send_response(200, "OK")
        elif self.path == "/":
            self._send_response(200, "Hello from Effective Mobile!")
        else:
            self._send_response(404, "Not Found")

    def _send_response(self, status_code: int, message: str):
        """Send HTTP response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def log_message(self, format, *args):
        """Suppress logging for health checks."""
        if "/health" not in args[0]:
            super().log_message(format, *args)


def main():
    """Start the HTTP server."""
    server = HTTPServer(("0.0.0.0", PORT), RequestHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
