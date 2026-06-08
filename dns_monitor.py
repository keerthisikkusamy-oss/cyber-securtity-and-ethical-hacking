from scapy.all import sniff
from scapy.layers.dns import DNS, DNSQR

def dns_packet_callback(packet):
    if packet.haslayer(DNS) and packet.haslayer(DNSQR):

        dns = packet[DNS]

        # DNS Query
        if dns.qr == 0:
            query_name = packet[DNSQR].qname.decode(errors="ignore")
            print(f"[DNS Query] {query_name}")

        # DNS Response
        elif dns.qr == 1:
            query_name = packet[DNSQR].qname.decode(errors="ignore")
            print(f"[DNS Response] {query_name}")

            for i in range(dns.ancount):
                try:
                    answer = dns.an[i]
                    print(f"  -> {answer.rdata}")
                except:
                    pass

print("Monitoring DNS traffic... Press Ctrl+C to stop.")

sniff(
    filter="udp port 53",
    prn=dns_packet_callback,
    store=False
)