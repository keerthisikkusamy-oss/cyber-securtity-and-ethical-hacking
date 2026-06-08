import psutil

for interface, addresses in psutil.net_if_addrs().items():
    print(f"\nInterface: {interface}")

    for addr in addresses:
        print(" ", addr.address)