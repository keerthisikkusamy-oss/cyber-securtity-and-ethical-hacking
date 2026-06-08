import hashlib

filename = "test.txt"

with open(filename, "rb") as f:
    data = f.read()

sha256 = hashlib.sha256(data).hexdigest()

print("SHA256:", sha256)