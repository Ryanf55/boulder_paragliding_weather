import socket

# Source
s_port = 50222
s_ip = "255.255.255.255"

# Destination
d_ip = "3.21.114.123"
d_port = 50202

print("UDP target IP:", d_ip)
print("UDP target port:", d_port)


sockRX = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sockRX.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sockRX.bind((s_ip, s_port))

while True:
    data, addr = sockRX.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)

    sockTX = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sockTX.sendto(data, (d_ip, d_port))