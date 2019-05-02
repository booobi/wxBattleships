import socket
import cPickle


class SocketClient(object):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def initialize_connection(self, addr):
        """Initializes a socket connection to a given host and port"""
        self.socket.connect(addr)

    def send_data(self, data):
        """Sends any type of data using cPicke"""
        self.socket.sendall(cPickle.dumps(data))

    def block_wait_data(self):
        """Blocks execution, waits and then returns received data"""
        return cPickle.loads(self.socket.recv(1024))
