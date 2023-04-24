import sys;
import random;
import socket;
import struct;

import morse_dictionary as md;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((sys.argv[1], int(sys.argv[2])))
    
    while True:
        msg = input("Enter a message to send to the server: ")
        if msg == "exit":
            break
        msgMorse = md.encode(msg)
        msgBinary = msgMorse.encode()
        sock.send(msg)
        replyBinary = sock.recv(8)
        replyMorse = replyBinary.decode()
        reply = md.decode(replyMorse)
        print(reply)
    