import sys
from time import sleep
from pinger_client import PingerClient
from socket import timeout as socket_timeout

if len(sys.argv) != 3:
    raise TypeError('you need to pass the host as the first argument and the port as the second argument')

HOST = sys.argv[1]
PORT = int(sys.argv[2])

for attempts in range(0, 10):
    with PingerClient() as pinger:
        try:
            data_bytes, address = pinger.ping(attempts, HOST, PORT)
            data = data_bytes.decode()
            timestamp = data.split(' ')[2]

            print('{} PING {} timestamp {}'.format(attempts, HOST, timestamp))
        except socket_timeout:
            print('{} PING {} timed out'.format(attempts, HOST))

    sleep(1)
