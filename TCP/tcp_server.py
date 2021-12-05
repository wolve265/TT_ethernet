import socket

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)


HOST = '192.168.0.157'
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
