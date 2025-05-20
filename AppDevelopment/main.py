import http.server
httpd = http.server.HTTPServer(("", 8000), http.server.SimpleHTTPRequestHandler)

httpd.serve_forever()