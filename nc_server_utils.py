import socket

# DEBUG=True
class Communicator():
    HOST = "0.0.0.0"
    PORT = 10000
    connection=None #type: socket.socket
    def __init__(self,DEBUG=True):
        self.DEBUG=DEBUG
        self.init_sock()
    def recv_until_newline(self)->str:
        msg=""
        while True:
            msg+=self.connection.recv(1).decode("utf-8")
            if "\n" in msg:
                return msg.replace("\n","")

    def init_sock(self):
        if self.DEBUG:
            return
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.HOST, self.PORT)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(server_address)
        sock.listen(10)
        self.connection, client_address = sock.accept()
    def input(self,msg=""):
        if self.DEBUG:
            return input(msg)
        else:
            if msg:
                self.print(msg)
            return self.recv_until_newline()
    def print(self,msg : str):
        if self.DEBUG:
            print(msg)
        else:
            self.connection.sendall(str.encode(str(msg)+"\n"))
# if __name__ == "__main__":
#     while True:
#         init_sock()
#         while True:
#             msg=read()
#             send(msg)
