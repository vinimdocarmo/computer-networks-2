import sys
from time import sleep
from ping_client import UDPPingClient
from socket import timeout as socket_timeout

if len(sys.argv) != 3:
    raise TypeError('you need to pass the host as the first argument and the port as the second argument')

HOST = sys.argv[1]
PORT = int(sys.argv[2])

for attempts in range(0, 10):
    with UDPPingClient() as ping:
        try:
            data_bytes, address = ping.ping(attempts, HOST, PORT)
            data = data_bytes.decode()
            timestamp = data.split(' ')[2]

            print('{} PING {} timestamp {}'.format(attempts, HOST, timestamp))
        except socket_timeout:
            print('{} PING {} timed out'.format(attempts, HOST))
        finally:
            sleep(1)

