import socket
import cPickle

HOST = "127.0.0.1"
PORT = 12345

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)

print "Server started on", HOST, PORT

# make this whole thing a function and use start_new_thread to unblock server
player1BoardArray = cPickle.dumps([
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '^'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '|'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '|'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'v'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S')])

player2BoardArray = cPickle.dumps([
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '^'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '|'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '|'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'v'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S')])

conn1, addr1 = socket.accept()
conn1.send(cPickle.dumps("Waiting for player to connect"))

conn2, addr2 = socket.accept()
conn1.send(player1BoardArray)
conn2.send(player2BoardArray)

while True:
    pass


# while True:
#     data = conn1.recv(1024)
#     if "initialize" in data:
#         conn1.send(cPickle.dumps("waiting for player"))
#     print data, addr1
#
# conn.close()


def populateShips(grid):
    pass
