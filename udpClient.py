import socket
target_host = "127.0.0.1"
target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"abc", (target_host, target_port))

data, addr = client.recvform(4096)

print(data.decode())
client.clost
