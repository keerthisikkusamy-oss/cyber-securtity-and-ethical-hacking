import re

COMMON_PASSWORDS = {
    "password",
    "password123",
    "admin",
    "admin123",
    "qwerty",
    "123456",
    "welcome"
}

def validate_password(password):
    errors = []

    if len(password) < 12:
        errors.append("Minimum length is 12 characters")

    if not re.search(r"[A-Z]", password):
        errors.append("Must contain an uppercase letter")

    if not re.search(r"[a-z]", password):
        errors.append("Must contain a lowercase letter")

    if not re.search(r"\d", password):
        errors.append("Must contain a number")

    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        errors.append("Must contain a special character")

    if password.lower() in COMMON_PASSWORDS:
        errors.append("Password is too common")

    return errors


while True:
    password = input("sijimol: ")

    result = validate_password(password)

    if result:
        print("\nPassword rejected:")
        for error in result:
            print("-", error)
    else:
        print("\nPassword accepted")
        break