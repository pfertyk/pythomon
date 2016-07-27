import socket
import sys
HOST="0.0.0.0"
HOST="localhost"
PORT=10000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)
sock.listen(10)
def recv_until_newline(connection : socket.socket)->str:
    msg=""
    while True:
        msg+=connection.recv(1).decode("utf-8")
        if "\n" in msg:
            return msg
def init_sock():
    pass


def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent
while True:
    connection, client_address = sock.accept()
    flo = connection.makefile()
    try:
        print('client connected: %s'%(client_address,))
        while True:
            # flo.write("sup")
            # flo.flush()
            msg=recv_until_newline(connection)
            # mysend(sock,str.encode("recved %s"%msg))
            connection.sendall(str.encode("recved %s"%msg))
            # if data:
            #     connection.sendall(data)
            # else:
            #     break
    except Exception as e:
        print(e)
        connection.close()
    finally:
        connection.close()