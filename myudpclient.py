#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['ddd','aaaa','eee']:
    s.sendto(data,('127.0.0.1',9999))
    print s.recv(1024)
s.close()
exit()