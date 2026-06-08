import bcrypt

password = input("siji: ").encode()

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("Stored Hash:")
print(hashed.decode())

if bcrypt.checkpw(password, hashed):
    print("Password verified")