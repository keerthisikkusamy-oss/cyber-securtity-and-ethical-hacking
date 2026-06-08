import subprocess

vpn_exe = r"C:\Program Files\OpenVPN\bin\openvpn.exe"
config_file = r"C:\VPN\client.ovpn"

try:
    process = subprocess.Popen(
        [vpn_exe, "--config", config_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    print("Starting VPN...")

    for line in process.stdout:
        print(line.strip())

except Exception as e:
    print("Error:", e)