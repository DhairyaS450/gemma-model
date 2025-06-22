
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')  # Or replace * with your domain
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    # Handle preflight requests (OPTIONS)
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

# Start server
if __name__ == '__main__':
    port = 8000
    httpd = HTTPServer(('0.0.0.0', port), CORSRequestHandler)
    print(f"Serving on port {port} with CORS enabled")
    httpd.serve_forever()
