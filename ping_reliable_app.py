import sys
from time import sleep
from reliable_udp_sender import ReliableUDPSender

if len(sys.argv) != 3:
    raise TypeError('you need to pass the host as the first argument and the port as the second argument')

HOST = sys.argv[1]
PORT = int(sys.argv[2])

for attempts in range(0, 10):
    with ReliableUDPSender() as ping:
        data_bytes, address = ping.ping(attempts, HOST, PORT)
        data = data_bytes.decode()
        timestamp = data.split(' ')[3]

        print('{} PING {} timestamp {}'.format(attempts, HOST, timestamp))

        sleep(1)

