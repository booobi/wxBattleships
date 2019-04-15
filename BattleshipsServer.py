import socket
import cPickle

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 12345))
socket.listen(1)

conn, addr = socket.accept()

player1BoardArray = cPickle.dumps([
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '^'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '|'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '|'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'v'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S')])

while True:
    data = conn.recv(1024)
    if "initialize" in data:
        print data
        conn.send(str(player1BoardArray))
    conn, addr = socket.accept()

conn.close()


def populateShips(grid):
    pass
