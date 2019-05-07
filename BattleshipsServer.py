import socket
import cPickle
import time

HOST = "127.0.0.1"
PORT = 12345

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)

print "Server started on", HOST, PORT

# make this whole thing a function and use start_new_thread to unblock server
player1BoardArray = cPickle.dumps([
    ('1', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '^'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '|'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '|'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'v'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S')])

player2BoardArray = cPickle.dumps([
    ('2', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '^'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '|'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '', '|'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'v'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'), ('S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S')])


def register_hit(array, global_indx):
    pass


first_connection, addr1 = socket.accept()
first_connection.sendall(cPickle.dumps("wait_connect"))

second_connection, addr2 = socket.accept()
second_connection.sendall(player2BoardArray)
first_connection.sendall(player1BoardArray)

game_over = False

first_connection.sendall(cPickle.dumps("go_turn"))
second_connection.sendall(cPickle.dumps("wait_turn"))

while not game_over:
    pass
    #
    # index_to_check = cPickle.loads(first_connection.recv(1024))
    # register_hit(player2BoardArray, index_to_check)
    # #do calcs to measure if game is over
    #
    # first_connection, second_connection = second_connection, first_connection