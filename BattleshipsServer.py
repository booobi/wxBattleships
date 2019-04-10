import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost',12345))
socket.listen(1)

conn, addr = socket.accept()
while True:
    data = conn.recv(1024)
    if "initialize" in data:
        print data
        conn.send("initializationData")
    conn, addr = socket.accept()

conn.close()

def populateShips(grid):
    pass