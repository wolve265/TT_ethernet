import socket
from bs4 import BeautifulSoup as bs


HOST = '192.168.0.157'  # The server's hostname or IP address
PORT = 80        # The port used by the server

html_content = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET /INDEX.HTM HTTP 1.0')
    while True:
        data = s.recv(1024)
        if not data:
            break
        html_content.append(data.decode())

html_string = ' '.join(html_content)

bs_html = bs(html_string, 'html.parser')
# print(bs_html.prettify())
print(bs_html.body.get_text())
