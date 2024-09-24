#!/usr/bin/python3
import sys
import socket

if len(sys.argv) != 3:
    print("Usage: smtp-enum.py <IP> <User>")
    exit(1)

ip = sys.argv[1]
user = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    s.connect((ip, 25))
    banner = s.recv(1024).decode('utf-8')
    print(f"Banner: {banner}")


    s.sendall(f"VRFY {user}\r\n".encode('utf-8'))
    result = s.recv(1024).decode('utf-8')
    print(f"Result: {result}")
except socket.error as err:
    print(f"Socket error: {err}")
finally:
    s.close()
