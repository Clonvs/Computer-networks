import socket

client = socket.socket()

name = input("Введите имя: ")
client.connect(("127.0.0.1", 55555))
client.send(name.encode())
socket_name = client.recv(1024)
server_name = socket_name.decode()
print(server_name + " присоединился!")

while True:
    data = (client.recv(1024)).decode()
    print(server_name, ':', data)
    data = input("Я: ")
    client.send(data.encode())