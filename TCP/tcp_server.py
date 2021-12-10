import socket

HOST = '192.168.0.10'
PORT = 80
print(f'The Web server URL for this would be http://{HOST}:{PORT}/')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(b'HTTP/1.0 200 OK\n')
            conn.send(b'Content-Type: text/html\n')
            conn.send(b'\n')
            conn.send(b"""<html>
                      <head>
                      <title>TCP/IP Comp Web page</title>
                      </head>
                      <body>
                      <b>Hello World</b>
                      <p>How are you today?</p>
                      </body>
                      </html>""")
            break
