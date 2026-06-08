import pyshark

capture = pyshark.FileCapture('capture.pcapng')

packet_count = 0

for packet in capture:
    packet_count += 1

    try:
        print(f"\nPacket #{packet_count}")
        print(f"Protocol: {packet.highest_layer}")
        print(f"Source: {packet.ip.src}")
        print(f"Destination: {packet.ip.dst}")
    except AttributeError:
        pass

print(f"\nTotal packets analyzed: {packet_count}")