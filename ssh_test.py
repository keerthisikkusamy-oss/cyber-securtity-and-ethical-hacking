import paramiko

host = "192.168.1.100"
username = "siji"
password = "anamol"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(
        hostname=host,
        username=username,
        password=password,
        timeout=10
    )

    stdin, stdout, stderr = client.exec_command("hostname")

    print("siji:")
    print(stdout.read().decode())

finally:
    client.close()