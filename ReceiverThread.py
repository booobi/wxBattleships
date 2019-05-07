from threading import Thread
from pubsub import pub


class ReceiverThread(Thread):
    def __init__(self, socketObj):
        Thread.__init__(self)
        self.sock = socketObj
        self.start()

    def run(self):
        msg = self.sock.block_wait_data()
        if msg == "wait_connect":
            pub.sendMessage("wait_connect")

        elif type(msg) == list:
            pub.sendMessage("initial", arr=msg)
