from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import time
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
    
        ts= time.time()
        message = "Timestamp: " +str(ts) + '<br>' + 'Hostname: '+socket.gethostname() 
        self.wfile.write(bytes(message, "utf8"))
       

with HTTPServer(('', 8080), handler) as server:
    server.serve_forever()
