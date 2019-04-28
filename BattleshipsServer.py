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


def register_hit(array, global_indx):
    pass


first_connection, addr1 = socket.accept()
first_connection.send(cPickle.dumps("Waiting for player to connect"))

second_connection, addr2 = socket.accept()
first_connection.send(player1BoardArray)
second_connection.send(player2BoardArray)

gameOver = False
while True:
    unparsed_data = first_connection.recv(1024)
    index_to_check = cPickle.loads(unparsed_data)
    register_hit(player2BoardArray, index_to_check)