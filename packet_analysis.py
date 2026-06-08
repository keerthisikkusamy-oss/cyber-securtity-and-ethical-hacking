from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

# Capture 10 packets
sniff(prn=process_packet, count=10)