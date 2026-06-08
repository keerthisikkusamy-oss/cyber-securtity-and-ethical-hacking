import socket

target = "127.0.0.1"

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    if sock.connect_ex((target, port)) == 0:
        print(f"Open port: {port}")

    sock.close()