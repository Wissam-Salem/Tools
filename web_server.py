from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("""
                                <!DOCTYPE html>
                                <html>
                                    <head>
                                        <title>Beta Fake Website</title>
                                    </head>
                                    <body>
                                        <div>
                                            <h1>Hello unconscious client <span style="color: red;">YOU HAVE BEEN HACKED</span></h1>
                                        </div>
                                    </body>
                                </html>
                            """.encode("utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"ERROR 404!\nPage Not Found.")

class httpServer(HTTPServer):
    def __init__(self, host, port):
        server_address = (host, port)
        HTTPServer.__init__(self, server_address, RequestHandler)

def runServer():
    server = httpServer("127.0.0.1", 80)
    server.serve_forever()
    server.socket.close()

runServer()