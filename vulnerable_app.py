import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

cursor.execute("DELETE FROM users")

cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ("admin", "secret123")
)

conn.commit()

username = input("siji: ")

query = f"SELECT * FROM users WHERE username='{siji}'"

print("Executing:")
print(query)

cursor.execute(query)

result = cursor.fetchall()

if result:
    print("User found:", result)
else:
    print("No user found")

conn.close()