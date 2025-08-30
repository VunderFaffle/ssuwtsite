from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 80

# SimpleHTTPRequestHandler автоматически отдаст index.html из текущей папки
with HTTPServer((HOST, PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Сервер запущен: http://{HOST}:{PORT}")
    httpd.serve_forever()

