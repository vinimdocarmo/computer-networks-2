import socket
from socket import timeout as socket_timeout
from time import time


class ReliableUDPSender(socket.socket):
    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_DGRAM)
        self.CRLF = '\r\n'
        self.settimeout(1)

    def ping(self, attempts, host='localhost', port=3000):
        msg = 'PING {} {} {}'.format(attempts, time(), self.CRLF)

        data_bytes = None
        address = None
        received = False

        while received is False:
            try:
                self.connect((host, port))
                self.sendall(bytes(msg, 'UTF-8'))
                data_bytes, address = self.recvfrom(1024)
                received = True
            except socket_timeout:
                continue

        return data_bytes, address
