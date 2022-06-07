import socket
import threading
import sys

server_ip = socket.gethostbyname(socket.gethostname())

port = 6969
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen(21)


class User:
    current_users = []

    def __init__(self, user, user_port, username):
        User.current_users.append(self)
        self.user = user
        self.user_port = user_port
        self.user_ip = user.getsockname()[0]
        self.username = username

    def listen(self):
        self.user.send("Welcome to thunderChat!".encode('utf-8'))
        self.broadcast(f"{self.username} entered the chat !!")
        while True:
            try:
                message = self.user.recv(2048).decode('utf-8')
                if message:
                    curr_message = f"<{self.username}> : {message}"
                    self.broadcast(curr_message)
            except ConnectionResetError:
                User.current_users.remove(self)
                break

    def broadcast(self, message):
        for user in User.current_users:
            if user != self:
                user.user.send(message.encode('utf-8'))


while True:
    user, user_port = server.accept()
    username = user.recv(2048).decode('utf-8')
    new_user = User(user, user_port, username)
    print(f"{username} entered the chat !!")
    curr_user_thread = threading.Thread(target=new_user.listen)

    curr_user_thread.start()
