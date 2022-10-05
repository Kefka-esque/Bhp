import socket

target_host = input("Please enter a target IP: ")
target_port = int(input("Specify a port: "))

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client

client.connect((target_host,target_port))

# Send some data

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data

response = client.recv(4096)

print(response.decode())
client.close()