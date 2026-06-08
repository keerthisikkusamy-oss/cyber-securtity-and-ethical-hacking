from scapy.all import sniff, TCP, Raw, IP

def analyze_http(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        try:
            payload = packet[Raw].load.decode('utf-8', errors='ignore')

            http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]

            if any(payload.startswith(method) for method in http_methods):
                print("\n=== HTTP Request Detected ===")
                print(f"Source IP      : {packet[IP].src}")
                print(f"Destination IP : {packet[IP].dst}")

                lines = payload.split("\r\n")

                print(f"Request Line   : {lines[0]}")

                for line in lines:
                    if line.lower().startswith("host:"):
                        print(f"Host           : {line[5:].strip()}")
                        break

        except Exception:
            pass

# Listen for HTTP traffic on port 80
sniff(filter="tcp port 80", prn=analyze_http, store=False)