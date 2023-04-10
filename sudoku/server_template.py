from http.server import HTTPServer, BaseHTTPRequestHandler

# DEFAULT_PATH = "/Index.html"

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.path = DEFAULT_PATH
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()
