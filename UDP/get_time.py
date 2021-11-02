import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "time.nist.gov"
port = 13
s.connect((host, port))
while True:
    data = s.recv(1024)
    if data:
        print(data.decode())
    else:
        break

s.close()
