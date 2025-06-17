from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import sys
import os
from urllib.parse import parse_qs, urlparse

try:
    from cipher_forms import show_cipher_form
except ImportError:
    def show_cipher_form(*args, **kwargs):
        pass
try:
    from asym_forms import show_asym_form
except ImportError:
    def show_asym_form(*args, **kwargs):
        pass

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_url = urlparse(self.path)
        
        # Handle cipher form requests
        if parsed_url.path == '/caesar':
            self.send_response(200)
            self.end_headers()
            show_cipher_form("Caesar Cipher")
            return
        elif parsed_url.path == '/vigenere':
            self.send_response(200)
            self.end_headers()
            show_cipher_form("Vigenere Cipher")
            return
        elif parsed_url.path == '/playfair':
            self.send_response(200)
            self.end_headers()
            show_cipher_form("Playfair Cipher")
            return
        elif parsed_url.path == '/railfence':
            self.send_response(200)
            self.end_headers()
            show_cipher_form("Rail Fence Cipher")
            return
        elif parsed_url.path == '/rsa':
            self.send_response(200)
            self.end_headers()
            show_asym_form("RSA Cipher")
            return
        elif parsed_url.path == '/ecc':
            self.send_response(200)
            self.end_headers()
            show_asym_form("ECC Cipher")
            return
        
        # For other paths, serve files as usual
        return SimpleHTTPRequestHandler.do_GET(self)

def run_server():
    # Change to the lab-02 directory where the web files are located
    os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'lab-02'))
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CustomHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
