import sqlite3
import bcrypt

# Create database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password_hash BLOB
)
""")

conn.commit()


# Register user
def register(username, password):
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            "INSERT INTO users VALUES (?, ?)",
            (username, hashed)
        )
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")


# Login user
def login(username, password):
    cursor.execute(
        "SELECT password_hash FROM users WHERE username=?",
        (username,)
    )

    result = cursor.fetchone()

    if result:
        stored_hash = result[0]

        if bcrypt.checkpw(
            password.encode(),
            stored_hash
        ):
            print("Login successful.")
        else:
            print("Invalid password.")
    else:
        print("User not found.")


# Menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        user = input("Username: ")
        pwd = input("Password: ")
        register(user, pwd)

    elif choice == "2":
        user = input("Username: ")
        pwd = input("Password: ")
        login(user, pwd)

    elif choice == "3":
        break

conn.close()