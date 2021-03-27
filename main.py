import psutil as pu
import cpuinfo
import socket
from tkinter import *
from tkinter.ttk import *
from threading import Thread
from time import time
from time import sleep


class Computer:

    def __init__(self):
        self.fr = Frame()
        self.params = []

    def set_params(self, params: dict):
        for i in self.params:
            i.destroy()
            self.params.remove(i)
        for i in params:
            self.params.append(Label(self.fr, text=f'{i}: {params[i]}'))

    def pack(self):
        self.fr.pack()
        for i in self.params:
            i.pack()

class App(socket.socket):

    def __init__(self, root, addres: tuple = ('localhost', 8080), *args, **kwargs):
        super().__init__()
        self.addr = addres
        self.run = True
        self.computers = {}
        self.root = root

    def start_clinent(self):
        while self.run:
            info = ''
            self.send(info.encode())
            sleep(10)


    def accept_info(self, sock: socket.socket):
        while self.run:
            msg = sock.recv(1024).decode()
            msg = msg.split("  ")
            print(msg)

    def listener(self):
        while self.run:
            addr, sock = self.accept()
            print(addr)
            Thread(target=self.accept_info(sock)).start()

    def start_server(self, root):
        Thread(target=self.listen).start()
        self.bind(self.addr)
        self.listener()
        addrs = {}
        while self.run:
            for i in self.computers:
                if i not in addrs:
                    addrs[i] = []

            self.root.update()
            pass

print(pu.virtual_memory().total/8/1024/1024, pu.virtual_memory().used/8/1024/1024)
print(cpuinfo.get_cpu_info())

root = Tk()
sock = App(root)

def start_server():
    sock.start_server(root)

bt_server = Button(text='Главный')
bt_client = Button(text='Подкл')
bt_server.pack()
bt_client.pack()

root.mainloop()