import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234)) #ip and port of server

msg = s.recv(1024)
print(msg.decode("utf-8"))
sendMsg = input("send a message: ")
s.send(bytes(sendMsg, "utf-8"))
msg = s.recv(1024)
print(f"Server sent back: {msg.decode('utf-8')}")