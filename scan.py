from scapy.all import sniff, IP

def process_packet(packet):
    if IP in packet:
        print(f"Source: {packet[IP].src}")
        print(f"Destination: {packet[IP].dst}")
        print("-" * 40)

sniff(filter="ip", prn=process_packet, count=20)