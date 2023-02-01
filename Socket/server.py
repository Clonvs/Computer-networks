import socket

server = socket.socket()
server.bind(("127.0.0.1", 55555))
server.listen()

print("Соединение установленно!")
name = input("Введите имя: ")
conn, add = server.accept()

client = (conn.recv(1024)).decode()
print(client + " присоединился!")
conn.send(name.encode())

while True:
    message = input("Я: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)


  
