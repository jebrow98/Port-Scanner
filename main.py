

import socket


class bcolors:
    RED = '\033[91m'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(7)

host = input(bcolors.RED + "Please enter the IP you want to scan: ")
port = int(input(bcolors.RED +"Please enter the port you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print(bcolors.RED + "The port is closed")
    else:
        print(bcolors.RED + "The Port is open")

portScanner(port)