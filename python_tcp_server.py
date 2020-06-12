#! /usr/bin/python3
# a simple tcp server
import socket, os
import sys

print("Required usage format : ./python_tcp_server.py port eg: ./python_tcp_server.py 5000 \n")
host = os.popen("ifconfig |grep inet |awk '{print $2}' |grep 192.168.1").read().strip()

if len(sys.argv) > 1:
    port = str(sys.argv[1])
if len(sys.argv) > 2:
    multipleConnection = sys.argv[2]
else:
    multipleConnection = False
print("server " + host + ":" + port)

port = int(port)
# print(port+1)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind((host, port))
    sock.listen(5)
    wait = True
    while multipleConnection:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        print(buf)
        connection.send(buf)
        connection.close()
        wait = False
    sock.close()
except:
    print("Some thing wrong happened")
finally:
    print("socket closed")
    sock.close()
    print("socket closed")
