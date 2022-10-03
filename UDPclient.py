import socket

target_host = "127.0.0.1"
target_port = 9997

# Create socket object

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data

client.sendto(b"AAABBBCCC", (target_host,target_port))

# Receive

data, addr = client.recvfrom(4096)

# Output data
print(data.decode())
client.close()