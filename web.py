import http.server
import socketserver
import ssl
import threading

HOST = "0.0.0.0"   # или "localhost", если нужен только локальный доступ
HTTP_PORT = 80
HTTPS_PORT = 443

Handler = http.server.SimpleHTTPRequestHandler

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run_http():
    with ReusableTCPServer((HOST, HTTP_PORT), Handler) as httpd:
        print(f"HTTP:  http://localhost")
        httpd.serve_forever()

def run_https():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    with ReusableTCPServer((HOST, HTTPS_PORT), Handler) as httpd:
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print(f"HTTPS: https://localhost")
        httpd.serve_forever()

if __name__ == "__main__":
    # Запускаем оба сервера: HTTP и HTTPS
    threading.Thread(target=run_http, daemon=True).start()
    run_https()
