import socket
import threading
import time

server_ip = '192.168.20.191'
port = 6969
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((server_ip, port))
username = 'Harsha Vardhan V'


def server_listener():
    while True:
        print(server.recv(2048).decode('utf-8'))


server.send(username.encode('utf-8'))

listen_server = threading.Thread(target=server_listener)
listen_server.start()

server.send(username.encode('utf-8'))

while True:
    # server.send('thunderbook'.encode('utf-8'))
    # time.sleep(2)
    pass