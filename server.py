import sys;
import random;
import socket;
import select;
import struct;

import morse_dictionary as md;

srv = socket(AF_INET, SOCK_STREAM)
srv.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
srv.bind(("0.0.0.0", 5555))
srv.listen()

sockets = [srv]

while True:
    readable, _, _ = select(sockets, [], [], 1)
    for active in readable:
        if active == srv:
            cli, addr = active.accept()
            #print("New client ", addr);
            sockets.append(cli)
        else:
            msgMorse = active.recv(128)
            msgPlain = md.decode(msgMorse)
            if not msgMorse:
                active.close()
                sockets.remove(active)
                #print("Client left");
            else:
                for s in sockets:
                    if s != active and s != srv:
                        msg = md.encode("disconnected")
                        s.send(msg)