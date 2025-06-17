from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

def run_server():
    # Change to the test directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running at http://localhost:8000")
    
    # Open the browser automatically
    webbrowser.open('http://localhost:8000')
    
    # Start the server
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
