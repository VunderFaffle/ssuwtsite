from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import time
from bs4 import BeautifulSoup as bs

HOST = "192.168.0.12"
PORT = 80

# SimpleHTTPRequestHandler автоматически отдаст index.html из текущей папки
with HTTPServer((HOST, PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Сервер запущен: http://{HOST}:{PORT}")
    httpd.serve_forever()

