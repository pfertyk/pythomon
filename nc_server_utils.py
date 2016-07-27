import socket
HOST="0.0.0.0"
PORT=10000
# DEBUG=True
connection=None
def recv_until_newline(connection : socket.socket)->str:
    msg=""
    while True:
        msg+=connection.recv(1).decode("utf-8")
        if "\n" in msg:
            return msg.replace("\n","")

def init_sock(DEBUG : bool):
    if DEBUG:
        return
    global connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)
    sock.listen(10)
    connection, client_address = sock.accept()
def read(DEBUG : bool):
    if DEBUG:
        return input()
    else:
        return recv_until_newline(connection)
def send(msg : str, DEBUG: bool):
    if DEBUG:
        print(msg)
    else:
        connection.sendall(str.encode(msg))
if __name__ == "__main__":
    while True:
        init_sock()
        while True:
            msg=read()
            send(msg)
