#!/usr/bin/env python3

import socket
import sys
import os
import json

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/var/run/user/1000/leftwm/leftwm.sock'
sock.connect(server_address)

def read_socket():
    try:
        data = sock.recv(1024)
        return json.loads(data)
    except json.decoder.JSONDecodeError as err:
        return None


while True:
    data = read_socket()
    print(data)
