import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    msg = clientsocket.recv(1024)
    clientsocket.send(msg)
    print(f"Message from client: {msg.decode('utf-8')}")