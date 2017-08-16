import socket
from time import time


class UDPPingClient(socket.socket):
    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_DGRAM)
        self.CRLF = '\r\n'
        self.settimeout(1)

    def ping(self, attempts, host='localhost', port=3000):
        msg = 'PING {} {} {}'.format(attempts, time(), self.CRLF)
        self.connect((host, port))
        self.sendall(bytes(msg, 'UTF-8'))
        return self.recvfrom(1024)
